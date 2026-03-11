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

def query_graphql(query, variables={}):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    URL = "https://api.github.com/graphql"
    response = requests.post(URL, json={'query': query, 'variables': variables }, headers=headers)
    return response.json()

query = "query { viewer { id } }"
output = query_graphql(query)
viewerId = eval(str(output))['data']['viewer']['id']

query = Path('graphql/commits-on-own-repo.graphql').read_text()
output = query_graphql(query, {"viewerId": viewerId})
print(output)

query = Path('graphql/commits-on-other-repo.graphql').read_text()
output = query_graphql(query, {"viewerId": viewerId})
print(output)