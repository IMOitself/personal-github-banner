from get_data import GetData
from pathlib import Path
import json

GetData = GetData()
output = GetData.query_graphql(Path('graphql/commits-on-own-repo.graphql').read_text(), {"viewerId": GetData.viewerId})
Path("test.json").write_text(json.dumps(output), encoding='utf-8')


print("\n\n")
