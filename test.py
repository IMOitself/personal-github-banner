from get_data import GetData
from pathlib import Path

GetData = GetData()
output = GetData.query_graphql(Path('graphql/recent_repo.graphql').read_text(), {"viewerId": GetData.viewerId})
print(output)


print("\n\n")
