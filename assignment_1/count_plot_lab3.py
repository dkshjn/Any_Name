import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/dj/Desktop/Acads/Sem 6/STT/Labs/lab3/cs202_miner/ollama_results/ollama_commits_info.csv"
df = pd.read_csv(file_path)

code_extensions = (".go", ".c", ".h", ".cmake", "CMakeLists.txt", ".sh", ".ts", ".ps1", ".psm1", ".cpp", ".py", ".iss",".rc")

# Classify them into code and non-code
def categorize_file(path):
    if isinstance(path, str):
        if path.endswith(code_extensions):
            return "code"
        else:
            return "non_code"

df["type"] = df["old_file path"].apply(categorize_file)

# Count them
matches_code = df[(df["Matches"] == "Yes") & (df["type"] == "code")].shape[0]
no_matches_code = df[(df["Matches"] == "No") & (df["type"] == "code")].shape[0]
matches_non_code = df[(df["Matches"] == "Yes") & (df["type"] == "non_code")].shape[0]
no_matches_non_code = df[(df["Matches"] == "No") & (df["type"] == "non_code")].shape[0]

# Print results
print("Matches for Non-Code Artifacts:", matches_non_code)
print("No Matches for Non-Code Artifacts:", no_matches_non_code)
print("Matches for Code Artifacts:", matches_code)
print("No Matches for Code Artifacts:", no_matches_code)

# Plot
categories = [ "Matches (Non-Code)", "No Matches (Non-Code)","Matches (Code)", "No Matches (Code)"]
values = [1527, 28, 1139, 81]

plt.figure(figsize=(10, 8))
plt.bar(categories, values, color=["blue", "red", "green", "purple"])
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Comparison of Matches and No Matches in Code and Non-Code Artifacts")
plt.show()
