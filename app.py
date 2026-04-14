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
from PIL import Image

st.set_page_config(page_title="Arcs Card Generator", layout="wide")

st.title("Arcs Card Generator")

st.markdown("Edit card templates and generate card images from your browser, preview and download the results.")

# Help link
st.markdown("How to use: [Open project README on GitHub](https://github.com/Laurens1234/Arcs-Leader-Generator/)")
st.markdown("You can ask for help here: [Discord channel](https://discord.com/channels/1459242411325919317/1482161901067833364)")
st.markdown("For more features and customization, you can set up and run the generator locally on your PC (see the README for setup instructions).")
st.markdown("Check out my website: [Arcs Arsenal](https://laurens1234.github.io/arcs-arsenal/)")

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
    "Eddifice": {
        "script": "batchLoreCards.py",
        "module": "eddificeFormatted",
        "path": Path("scripts") / "eddificeFormatted.py",
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
    card_type = st.selectbox("Card type to generate", list(TEMPLATE_MAP.keys()))
    args = st.text_input("Arguments (optional)", value="")

    # prepare template editing for the selected card type (always custom override)
    mapping = TEMPLATE_MAP[card_type]
    template_module = mapping["module"]
    repo_path = mapping["path"]
    try:
        if repo_path.exists():
            template_text = extract_top_list_entry(repo_path)
        else:
            template_text = "# template not found"
    except Exception:
        template_text = "# failed to read template"

    template_text = st.text_area(f"Edit {template_module}.py (temporary override)", value=template_text, height=300)
    run_button = st.button("Run")

    uploaded = st.file_uploader(
        "Upload PNG images to use with generator (optional)",
        type=["png"],
        accept_multiple_files=True,
    )
    st.info("Uploaded PNG filename must match the card name (without .png). Example: leadername.png for card name 'leadername'.")
    if uploaded:
        UPLOAD_MAP = {
            "Leader": "leaderImages",
            "Guild": "guildImages",
            "Lore": "loreImages",
            "Eddifice": "loreImages",
            "Vox": "voxImages",
        }
        dest_dir = Path("cardAssets") / UPLOAD_MAP.get(card_type, "captured")
        dest_dir.mkdir(parents=True, exist_ok=True)
        saved = []
        for f in uploaded:
            # Save everything as PNG to ensure generator compatibility
            try:
                img = Image.open(f)
            except Exception as e:
                st.error(f"Failed to open uploaded file '{f.name}': {e}")
                continue

            base_name = Path(f.name).stem
            target = dest_dir / f"{base_name}.png"
            if target.exists():
                target = dest_dir / f"{base_name}_{int(time.time())}.png"
            try:
                # Convert to RGBA then save as PNG
                img.convert("RGBA").save(target, format="PNG")
                saved.append(target)
            except Exception as e:
                st.error(f"Failed to save '{f.name}' as PNG: {e}")

        if saved:
            st.success(f"Saved {len(saved)} uploaded PNG file(s) to {display_rel(dest_dir)}")
            for t in saved:
                st.write(display_rel(t))
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
        # sort newest-first by mtime
        new_paths_sorted = sorted(new_paths, key=lambda p: after[p], reverse=True)
        if new_paths_sorted:
            st.subheader("New images generated")
            for path_str in new_paths_sorted:
                p = Path(path_str)
                cols = st.columns([1, 4])
                with cols[0]:
                    try:
                        st.image(str(p), width=250)
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
        else:
            st.info("No new images found in the results folder.")

# Removed 'show latest' quick action: UI now only displays images generated by the last run.
