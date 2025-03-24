import json
import os
import pandas as pd

# Repositories
REPOS = ["transformers", "youtube-dl", "scikit-learn"]

def process_bandit_reports(repo_name):
    print(f"\nProcessing Bandit results for {repo_name}...")

    reports_path = os.path.join(repo_name, "bandit_reports")
    commit_data = []

    for report_file in os.listdir(reports_path):
        if not report_file.endswith(".json"):
            continue

        report_path = os.path.join(reports_path, report_file)
        commit_hash = report_file.replace("bandit_report_", "").replace(".json", "")

        with open(report_path, "r") as f:
            data = json.load(f)

        confidence_levels = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
        severity_levels = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
        cwe_list = set()

        # Confidence and Severity
        for file, metrics in data.get("metrics", {}).items():
            confidence_levels["HIGH"] += metrics.get("CONFIDENCE.HIGH", 0)
            confidence_levels["MEDIUM"] += metrics.get("CONFIDENCE.MEDIUM", 0)
            confidence_levels["LOW"] += metrics.get("CONFIDENCE.LOW", 0)

            severity_levels["HIGH"] += metrics.get("SEVERITY.HIGH", 0)
            severity_levels["MEDIUM"] += metrics.get("SEVERITY.MEDIUM", 0)
            severity_levels["LOW"] += metrics.get("SEVERITY.LOW", 0)

        # Unique CWE IDs
        for issue in data.get("results", []):
            if "issue_cwe" in issue and "id" in issue["issue_cwe"]:
                cwe_list.add(issue['issue_cwe']['id'])
            else:
                cwe_list.add("Unknown")

        commit_data.append(
            {
                "Commit Hash": commit_hash,
                "High Confidence": confidence_levels["HIGH"],
                "Medium Confidence": confidence_levels["MEDIUM"],
                "Low Confidence": confidence_levels["LOW"],
                "High Severity": severity_levels["HIGH"],
                "Medium Severity": severity_levels["MEDIUM"],
                "Low Severity": severity_levels["LOW"],
                "Unique CWEs": list(cwe_list),
            }
        )

    df = pd.DataFrame(commit_data)
    csv_path = os.path.join(repo_name, "bandit_summary.csv")
    df.to_csv(csv_path, index=False)
    print(f"Saved summary to {csv_path}.")

for repo in REPOS:
    process_bandit_reports(repo)

print("Data extracted successfully.")
