from get_data import GetData
from pathlib import Path

GetData = GetData()
output = GetData.query_graphql(Path('graphql/test.graphql').read_text(), {"viewerId": GetData.viewerId})
print(output['data']['viewer']['repositories']['nodes'][0]['defaultBranchRef']['target']['history']['nodes'][0]['committedDate'])