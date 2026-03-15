from get_data import GetData
from pathlib import Path

GetData = GetData()
print(GetData.query_graphql(Path('graphql/test.graphql').read_text()))