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

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["High Severity"], label="High Severity", marker='o')
    plt.plot(df.index, df["Medium Severity"], label="Medium Severity", marker='s')
    plt.plot(df.index, df["Low Severity"], label="Low Severity", marker='^')

    plt.xlabel("Commit Index (Last 100)")
    plt.ylabel("Number of Issues")
    plt.title(f"Severity Trends Over Time - {repo_name}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
