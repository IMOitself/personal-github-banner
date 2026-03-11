import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

TOKEN = os.getenv("ACCESS_TOKEN")
if(TOKEN is None):
    print("access token is None")
    exit()

def query_graphql(query, variables=None):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    URL = "https://api.github.com/graphql"
    if(variables is None):
        variables = {}
    response = requests.post(URL, json={'query': query, 'variables': variables }, headers=headers)
    return response.json()

query = Path('graphql/test.graphql').read_text()
print(query_graphql(query, {"number_of_repos": 3}))

query = Path('graphql/help.graphql').read_text()
Path("graphql/help-output.json").write_text(json.dumps(query_graphql(query), indent=2))
