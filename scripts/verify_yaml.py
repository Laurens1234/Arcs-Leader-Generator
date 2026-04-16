import glob
import os

import yaml

base = os.path.dirname(__file__)
data_dir = os.path.join(base, "data")
paths = glob.glob(os.path.join(data_dir, "*.yml"))
if not paths:
    print("No YAML files found in", data_dir)
    raise SystemExit(1)

for p in sorted(paths):
    try:
        with open(p, encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(p, "-> ERROR loading:", e)
        continue
    count = None
    if isinstance(data, list):
        count = len(data)
    elif isinstance(data, dict):
        count = len(data.keys())
    else:
        count = 1
    print(os.path.basename(p), "-> type:", type(data).__name__, "count:", count)
