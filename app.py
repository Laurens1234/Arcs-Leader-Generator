import ast
import io
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
import zipfile
from pathlib import Path
from typing import List, Set

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title="Arcs Card Generator", layout="wide")

st.title("Arcs Card Generator")

st.markdown(
        """
        <div style='border:1px solid #ccc;padding:12px;border-radius:8px;background:transparent'>
            <strong>Edit Arcs card templates and generate card images directly in your browser.</strong>
            <div style='margin-top:12px; line-height:1.8;'>
                    <ul style='margin:0;padding-left:18px;'>
                        <li>How to use: <a href='https://github.com/Laurens1234/Arcs-Leader-Generator/' target='_blank'>Read the project README on GitHub</a></li>
                        <li>For advanced features, follow the setup instructions in the README to run the generator locally on your PC.</li>
                        <li>Need help or want to report a bug? <a href='https://discord.com/channels/1459242411325919317/1482161901067833364' target='_blank'>Open support Discord channel</a></li>
                        <li>Explore more Arcs tools and resources my other website: <a href='https://laurens1234.github.io/arcs-arsenal/' target='_blank'>Arcs Arsenal</a></li>
                        <li>Browse my Custom Cards created with this tool: <a href='https://laurens1234.github.io/arcs-arsenal/custom-cards' target='_blank'>Browse Custom Cards</a></li>
                    </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
)

TEMPLATE_MAP = {
    "Leader": {
        "script": "batchLeaderCards.py",
        "module": "leadersFormatted",
        "path": Path("scripts") / "leadersFormatted.py",
    },
    "Guild / Artifact": {
        "script": "batchGuildCards.py",
        "module": "guildCardsFormatted",
        "path": Path("scripts") / "guildCardsFormatted.py",
    },
    "Lore": {
        "script": "batchLoreCards.py",
        "module": "loreCardsFormatted",
        "path": Path("scripts") / "loreCardsFormatted.py",
    },
    "Edifice": {
        "script": "batchLoreCards.py",
        "module": "edificeFormatted",
        "path": Path("scripts") / "edificeFormatted.py",
    },
    "Vox": {
        "script": "batchVoxCards.py",
        "module": "voxCardsFormatted",
        "path": Path("scripts") / "voxCardsFormatted.py",
    },
}


def find_images(root: Path) -> List[Path]:
    exts = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
    files = []
    if not root.exists():
        return []
    for p in root.rglob("*"):
        if p.suffix.lower() in exts and p.is_file():
            files.append(p)
    return files


def snapshot_images(root: Path) -> Set[str]:
    return {str(p.resolve()) for p in find_images(root)}


def snapshot_images_mtime(root: Path):
    """Return a mapping of resolved path -> mtime for images under root."""
    return {str(p.resolve()): p.stat().st_mtime for p in find_images(root)}


results_root = Path("results")


def display_rel(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(Path.cwd()))
    except Exception:
        return str(p)


def extract_top_list_entry(path: Path) -> str:
    """Return a short module string containing only the top entry of the first top-level list assignment.

    Falls back to returning the whole file on failure.
    """
    try:
        src = path.read_text(encoding="utf-8")
        tree = ast.parse(src)
        for node in tree.body:
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.List) and node.value.elts:
                # get the target name if possible
                target = node.targets[0]
                var_name = target.id if isinstance(target, ast.Name) else None
                first_elt = node.value.elts[0]
                # Try to extract the exact source segment for the first element to preserve formatting
                first_src = None
                try:
                    first_src = ast.get_source_segment(src, first_elt)
                except Exception:
                    first_src = None
                if not first_src:
                    # Fallback: grab the relevant lines
                    lines = src.splitlines()
                    try:
                        first_src_lines = lines[first_elt.lineno - 1 : first_elt.end_lineno]
                        first_src = "\n".join(first_src_lines)
                    except Exception:
                        first_src = ast.unparse(first_elt) if hasattr(ast, "unparse") else repr(first_elt)

                # Dedent the extracted source and re-indent inside a single-entry list for clarity
                first_src = textwrap.dedent(first_src).rstrip()
                # Ensure it ends with a comma
                if not first_src.endswith(","):
                    first_src = first_src + ","

                indented = textwrap.indent(first_src + "\n", "    ")
                if var_name:
                    return f"{var_name} = [\n{indented}]\n"
                return f"[\n{indented}]\n"
    except Exception:
        pass
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return "# failed to read template"

with st.container():
    # Place the card type selector in a narrow column so it doesn't span full width
    col_small, col_large = st.columns([1, 4])
    with col_small:
        card_type = st.selectbox("Card type to generate", list(TEMPLATE_MAP.keys()))
    with col_large:
        args = st.text_input("Arguments (optional)", value="")

    # prepare template editing for the selected card type (always custom override)
    mapping = TEMPLATE_MAP[card_type]
    template_module = mapping["module"]
    repo_path = mapping["path"]
    try:
        if repo_path.exists():
            file_template_text = extract_top_list_entry(repo_path)
        else:
            file_template_text = "# template not found"
    except Exception:
        file_template_text = "# failed to read template"

    # Persist user edits per-template in a central dict so switching card types
    # doesn't lose edits. We keep a separate widget key per-module so Streamlit
    # manages the widget state, and copy that value into the dict after the
    # widget is created.
    overrides_key = "template_overrides"
    if overrides_key not in st.session_state:
        st.session_state[overrides_key] = {}

    widget_key = f"template_override_{template_module}"
    # Initialize the widget key only if missing, using either an existing override
    # or the file's template text.
    if widget_key not in st.session_state:
        st.session_state[widget_key] = st.session_state[overrides_key].get(template_module, file_template_text)

    # Auto-size the text area height to show all lines of the stored template
    # when switching card types or opening a type.
    stored_template = st.session_state[widget_key]
    lines = stored_template.count("\n") + 1
    pixels_per_line = 20
    extra_lines = 3
    computed_height = max(180, min(1600, lines * pixels_per_line + 20 + extra_lines * pixels_per_line))

    # Create the text area widget bound to the widget_key. Streamlit will store
    # the current text in `st.session_state[widget_key]`.
    template_text = st.text_area(
        f"Edit {template_module}.py (temporary override)",
        height=computed_height,
        key=widget_key,
    )

    # Mirror the widget value into the central overrides dict so it's easy to
    # access and persists across switches.
    st.session_state[overrides_key][template_module] = st.session_state[widget_key]
    run_button = st.button("Run")

    # Show a custom label so the default Streamlit uploader caption
    # (e.g. "200MB per file • PNG") is not displayed to the user.
    st.markdown("Upload PNG images to use with generator (optional)")
    uploaded = st.file_uploader(
        "",
        type=["png"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )
    # (Saved filenames will be displayed after uploads are processed.)
    if uploaded:
        # Always keep all uploaded files; add numeric suffixes as needed to avoid
        # name collisions. This avoids prompting and keeps behavior simple.
        name_map: dict[str, list] = {}
        for f in uploaded:
            base = Path(f.name).stem
            name_map.setdefault(base, []).append(f)

        upload_tmpdir = tempfile.mkdtemp(prefix="adk_upload_")
        saved = []
        saved_entries = []  # list of (original_filename, saved_path)

        for base_name, files in name_map.items():
            for idx, f in enumerate(files):
                try:
                    img = Image.open(f)
                except Exception as e:
                    st.error(f"Failed to open uploaded file '{f.name}': {e}")
                    continue

                # First file gets the plain name; subsequent files get numeric suffixes
                target = Path(upload_tmpdir) / f"{base_name}.png"
                if target.exists() or idx > 0:
                    i = 1
                    while True:
                        candidate = Path(upload_tmpdir) / f"{base_name}_{i}.png"
                        if not candidate.exists():
                            target = candidate
                            break
                        i += 1

                try:
                    img.convert("RGBA").save(target, format="PNG")
                    saved.append(target)
                    saved_entries.append((f.name, target))
                except Exception as e:
                    st.error(f"Failed to save '{f.name}' as PNG: {e}")

        if saved:
            st.session_state["adk_upload_dir"] = upload_tmpdir
            # Store display info so the UI can show saved filenames below the uploader.
            st.session_state["adk_upload_display"] = [(orig, str(p.name)) for orig, p in saved_entries]
            # Do not show a separate success box; the outlined list shows saved files
            st.write(display_rel(Path(upload_tmpdir)))
            # Render the saved names inside the outlined box so they appear
            # immediately after processing the upload.
            html = "<div style='border:2px solid #666;padding:10px;border-radius:6px;background:transparent;display:block;max-width:100%'>"
            html += "<strong>Saved upload filenames</strong><br/>"
            for original_name, path_obj in saved_entries:
                saved_name = str(path_obj.name)
                if Path(original_name).name != saved_name:
                    html += f"{original_name} &rarr; {saved_name}<br/>"
                else:
                    html += f"{saved_name}<br/>"
            html += "</div>"
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.info("No valid images were uploaded.")

if run_button:
    script = mapping["script"]
    cmd = [sys.executable, os.path.join("scripts", script)]
    if args:
        try:
            cmd += shlex.split(args)
        except Exception:
            st.error("Failed to parse arguments")
            st.stop()

    st.info(f"Running: {' '.join(cmd)}")
    before = snapshot_images_mtime(results_root)
    # prepare environment and temporary template module (always use edited template)
    tempdir = None
    env = os.environ.copy()
    # If the user uploaded images in this session, pass their tempdir to the subprocess
    upload_dir = st.session_state.get("adk_upload_dir") if hasattr(st, "session_state") else None
    if upload_dir:
        env["ADK_UPLOAD_DIR"] = str(upload_dir)
    if template_module and template_text:
        try:
            tempdir = tempfile.mkdtemp(prefix="adk_template_")
            target = Path(tempdir) / f"{template_module}.py"
            target.write_text(template_text, encoding="utf-8")
            # prepend tempdir to PYTHONPATH (harmless when using --source-file)
            env_py = env.get("PYTHONPATH", "")
            env["PYTHONPATH"] = str(tempdir) + os.pathsep + env_py if env_py else str(tempdir)
            st.info(f"Using edited template for module '{template_module}' from temporary path: {target}")
        except Exception as e:
            st.error(f"Failed to write temporary template: {e}")
            tempdir = None

    # If we wrote a temporary template file, tell the batch script to load it via --source-file
    if tempdir and template_module:
        target = Path(tempdir) / f"{template_module}.py"
        cmd.append(f"--source-file={str(target)}")

    with st.spinner("Running script..."):
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd(), timeout=600, env=env)
        except FileNotFoundError as e:
            st.error(f"Failed to run script: {e}")
            proc = None
        except subprocess.TimeoutExpired:
            st.error("Script timed out (600s)")
            proc = None
        finally:
            if tempdir:
                try:
                    shutil.rmtree(tempdir)
                except Exception:
                    pass
            # Clean up any session upload tempdir after the run
            upload_dir = st.session_state.get("adk_upload_dir") if hasattr(st, "session_state") else None
            if upload_dir:
                try:
                    shutil.rmtree(upload_dir)
                except Exception:
                    pass
                try:
                    del st.session_state["adk_upload_dir"]
                except Exception:
                    pass

    if proc:
        output = "".join([proc.stdout or "", proc.stderr or ""]) or "(no output)"
        st.subheader("Script output")
        st.code(output)
        if proc.returncode == 0:
            st.success("Script finished successfully")
        else:
            st.error(f"Script exited with code {proc.returncode}")

        after = snapshot_images_mtime(results_root)
        # consider a file 'new' if it didn't exist before or its mtime increased
        new_paths = [p for p, m in after.items() if (p not in before) or (m > before.get(p, 0))]
        # sort oldest-first by mtime so new images are appended below previous ones
        new_paths_sorted = sorted(new_paths, key=lambda p: after[p])
        if new_paths_sorted:
            # Anchor target for auto-scroll so we can jump to the new images area
            st.markdown("<div id='adk_new_images'></div>", unsafe_allow_html=True)
            st.subheader("New images generated")
            for path_str in new_paths_sorted:
                p = Path(path_str)
                cols = st.columns([1, 4])
                with cols[0]:
                    try:
                        # Display the full-resolution image (no width constraint)
                        st.image(str(p))
                    except Exception:
                        st.write(p.name)
                with cols[1]:
                    st.write(display_rel(p))
                    try:
                        with open(p, "rb") as f:
                            data = f.read()
                            st.download_button("Download", data, file_name=p.name)
                    except Exception:
                        st.write("(failed to read file for download)")

            # offer a ZIP download for all newly generated images
            try:
                buf = io.BytesIO()
                with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                    for path_str in new_paths_sorted:
                        pth = Path(path_str)
                        # write file into archive using its filename
                        zf.write(pth, arcname=pth.name)
                buf.seek(0)
                st.download_button(
                    "Download All",
                    data=buf.getvalue(),
                    file_name="generated_cards.zip",
                    mime="application/zip",
                )
            except Exception as e:
                st.warning(f"Failed to create ZIP archive: {e}")

            # Attempt to smoothly scroll the page to the new images anchor.
            try:
                components.html(
                    "<script>const el = window.parent.document.getElementById('adk_new_images'); if(el){el.scrollIntoView({behavior:'smooth', block:'start'});}</script>",
                    height=0,
                )
            except Exception:
                pass
        else:
            st.info("No new images found in the results folder.")

# Removed 'show latest' quick action: UI now only displays images generated by the last run.
