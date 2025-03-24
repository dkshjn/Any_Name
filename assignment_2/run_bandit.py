import git
import os
import subprocess

# Repositories
REPOS = ["transformers", "youtube-dl", "scikit-learn"]


def run_bandit_analysis(repo_name):
    print(f"\nProcessing repository: {repo_name}")

    repo_path = os.path.abspath(repo_name)
    repo = git.Repo(repo_path)

    reports_path = os.path.join(repo_path, "bandit_reports")
    os.makedirs(reports_path, exist_ok=True)

    commits = [
        (commit.hexsha, commit.committed_datetime)
        for commit in repo.iter_commits("main", max_count=100, no_merges=True)
    ]

    for commit_hash, timestamp in commits:
        print(f"Analyzing commit: {commit_hash} ({timestamp})")

        repo.git.checkout(commit_hash)
        report_file = os.path.join(reports_path, f"bandit_report_{commit_hash}.json")

        # Run Bandit
        subprocess.run(
            ["bandit", "-r", ".", "-f", "json", "-o", report_file], cwd=repo_path
        )

        with open(os.path.join(reports_path, "commit_timeline.txt"), "a") as f:
            f.write(f"{commit_hash} {timestamp}\n")

    repo.git.checkout("main")
    print(f"Repository processed: {repo_name}")


for repo in REPOS:
    run_bandit_analysis(repo)

print("Bandit analysis completed.")
