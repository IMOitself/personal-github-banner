from get_data import GetData
from pathlib import Path

GetData = GetData()
output = GetData.query_graphql(Path('graphql/test.graphql').read_text(), {"viewerId": GetData.viewerId})
print(output)


print("\n\n")

commit_change = [10, 12, 35, 20, 15]
max_commit_change = max(commit_change)

for commit_change in commit_change:
    percentage = commit_change / max_commit_change
    print(percentage * 200)
