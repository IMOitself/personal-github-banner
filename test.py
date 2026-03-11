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

overall_commits = 0

# get github id
query = "query { viewer { id } }"
output = query_graphql(query)
viewerId = eval(str(output))['data']['viewer']['id']

# commit count on own repo
query = Path('graphql/commits-on-own-repo.graphql').read_text()
output = query_graphql(query, {"viewerId": viewerId})

repos = eval(str(output))['data']['viewer']['repositories']['nodes']

for repo in repos:
    name = eval(str(repo))['nameWithOwner']
    total_count = eval(str(repo))['defaultBranchRef']['target']['history']['totalCount']
    print(total_count, name)
    overall_commits += int(total_count)

# commits count on other people's repo
query = Path('graphql/commits-on-other-repo.graphql').read_text()
output = query_graphql(query, {"viewerId": viewerId})
repos = eval(str(output))['data']['viewer']['repositoriesContributedTo']['nodes']

for repo in repos:
    name = eval(str(repo))['nameWithOwner']
    total_count = eval(str(repo))['defaultBranchRef']['target']['history']['totalCount']
    print(total_count, name)
    overall_commits += int(total_count)

print("OVERALL:", overall_commits)
