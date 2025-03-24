"""ORIGINAL CODE"""

# import sys
# import csv
# from pydriller import Repository
# from pydriller.metrics.process.code_churn import CodeChurn
# from pydriller.metrics.process.commits_count import CommitsCount
# from pydriller.metrics.process.hunks_count import HunksCount

# columns = ['SHA','Message','Diff']

# rows = []
# count=0
# last_n=100

# commits = []
# for x in Repository(sys.argv[1],only_no_merge=True,order='reverse').traverse_commits():
#   if (x.in_main_branch==True):
#     count=count+1
#     commits.append(x)
#     if count == last_n:
#       break

# in_order = []
# for value in range(len(commits)):
#   in_order.append(commits.pop())

# commits=in_order
# i=-1
# for commit in commits:
#   i+=1
#   print('[{}/{}] Mining commit {}.{}'.format(i+1,len(commits),sys.argv[1],commit.hash))
#   diff = []
#   for m in commit.modified_files:
#     diff.append(m.diff_parsed)
      
#   if (i>=1):   
#     rows.append([commit.hash,commit.msg,diff])
#   elif (i==0):
#     rows.append([commit.hash,commit.msg,''])
       
# with open(sys.argv[1]+'_results/commits_info.csv', 'a') as csvFile:
#   writer = csv.writer(csvFile)
#   writer.writerow(columns)
#   writer.writerows(rows)

"""MODIFIED CODE"""

import sys
import csv
from pydriller import Repository

# New Columns
columns = [
    'old_file path',
    'new_file path',
    'commit SHA',
    'parent commit SHA',
    'commit message',
    'diff_myers',
    'diff_hist',
    'Matches'
]

last_n = 500
repo_path = sys.argv[1]

# diff_myers obtained with histogram_diff=False
commits_myers = []
count = 0
for commit in Repository(repo_path, only_no_merge=True, order='reverse', histogram_diff=False).traverse_commits():
    if commit.in_main_branch:
        count += 1
        commits_myers.append(commit)
        if count == last_n:
            break

in_order_myers = []
for _ in range(len(commits_myers)):
    in_order_myers.append(commits_myers.pop())

commits_myers=in_order_myers

# diff_hist obtained with histogram_diff=True
commits_hist = []
count = 0
for commit in Repository(repo_path, only_no_merge=True, order='reverse', histogram_diff=True).traverse_commits():
    if commit.in_main_branch:
        count += 1
        commits_hist.append(commit)
        if count == last_n:
            break


in_order_hist = []
for _ in range(len(commits_hist)):
    in_order_hist.append(commits_hist.pop())

commits_hist=in_order_hist

rows = []
for i, (commit_myers, commit_hist) in enumerate(zip(commits_myers, commits_hist)):
    print('[{}/{}] Mining commit {}.{}'.format(i+1,len(commits_myers),sys.argv[1],commit.hash))
    for modified_file_myers, modified_file_hist in zip(commit_myers.modified_files, commit_hist.modified_files):
        parent_commit = commit_myers.parents[0] if commit_myers.parents else None

        # Skip if parent commit not available
        if not parent_commit or not modified_file_myers.old_path:
            continue

        diff_myers = modified_file_myers.diff
        diff_hist = modified_file_hist.diff

        # Match the two diffs to get Yes/No value
        match = "Yes" if (diff_myers.strip() if diff_myers else "") == (diff_hist.strip() if diff_hist else "") else "No"

        rows.append([
            modified_file_myers.old_path,
            modified_file_myers.new_path,
            commit_myers.hash,
            parent_commit,
            commit_myers.msg.strip(),
            diff_myers.strip() if diff_myers else '',
            diff_hist.strip() if diff_hist else '',
            match
        ])

# Now write the output to a csv file
with open(sys.argv[1]+'_results/commits_info.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(columns)
    writer.writerows(rows)

