import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

repo_paths = {
    "Transformers": "transformers/bandit_summary.csv",
    "YouTube-DL": "youtube-dl/bandit_summary.csv",
    "Scikit-Learn": "scikit-learn/bandit_summary.csv",
}

for repo_name, path in repo_paths.items():
    df = pd.read_csv(path)
    cwe_counter = Counter()

    for cwe_list in df["Unique CWEs"]:
        cwes = eval(cwe_list)
        cwe_counter.update(cwes)

    # Top 10 CWEs
    top_cwes = cwe_counter.most_common(10)

    sorted_cwes = sorted(top_cwes, key=lambda x: int(x[0]))
    cwe_ids = [f"CWE-{cwe[0]}" for cwe in sorted_cwes]
    counts = [cwe[1] for cwe in sorted_cwes]

    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(cwe_ids, counts)
    plt.xlabel("CWE")
    plt.ylabel("Frequency")
    plt.title(f"Top 10 CWEs - {repo_name}")
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()
