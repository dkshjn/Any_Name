import matplotlib.pyplot as plt

categories = [ "Matches (Non-Code)", "No Matches (Non-Code)","Matches (Code)", "No Matches (Code)"]
values = [1527, 28, 1139, 81]

# Plot
plt.figure(figsize=(10, 8))
plt.bar(categories, values, color=["blue", "red", "green", "purple"])
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Comparison of Matches and No Matches in Code and Non-Code Artifacts")
plt.show()
