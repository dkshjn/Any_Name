import json
from collections import defaultdict
import pandas as pd

# Load JSON file
with open("fastapi/fastapi/full_deps.json", "r") as f:
    data = json.load(f)

fan_out = {}
fan_in = defaultdict(int)

# Fan-in and Fan-out
for module, props in data.items():
    imports = props.get("imports", [])
    fan_out[module] = len(imports)
    for imported in imports:
        fan_in[imported] += 1

df = pd.DataFrame(
    {
        "Module": list(fan_out.keys()),
        "Fan-In": [fan_in.get(m, 0) for m in fan_out],
        "Fan-Out": [fan_out[m] for m in fan_out],
    }
)

df_sorted = df.sort_values(by=["Fan-In", "Fan-Out"], ascending=False, ignore_index=True)

# Save results to a csv file
df_sorted.to_csv("fan_in_out_analysis.csv", index=False)
