import pandas as pd
import matplotlib.pyplot as plt

file_paths = {
    "Transformers": "transformers/bandit_summary.csv",
    "YouTube-DL": "youtube-dl/bandit_summary.csv",
    "Scikit-Learn": "scikit-learn/bandit_summary.csv",
}

# Plots for each repository
for repo_name, file_path in file_paths.items():
    df = pd.read_csv(file_path)

    plt.figure(figsize=(12, 7))
    plt.plot(df.index, df["High Severity"], marker='o', linestyle='-')
    plt.xlabel("Commit Index (Last 100)")
    plt.ylabel("Number of High Severity Issues")
    plt.title(f"High Severity Vulnerabilities Over Time - {repo_name}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
