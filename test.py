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

def asDict(s):
    return eval(str(s))


overall_commits = 0


names = ["IMOaswell", "IMOitself"]

for name in names:
    query = "query { user(login: \""+name+"\") { id } }"
    output = query_graphql(query)
    id = asDict(output)['data']['user']['id']

    query = Path("graphql/test.graphql").read_text()
    output = query_graphql(query, {"viewerId": id})
    print(output)


if(True): exit()



# get github id
query = "query { viewer { id } }"
output = query_graphql(query)
viewerId = asDict(output)['data']['viewer']['id']

commit_count_strings = [
    ('graphql/commits-on-own-repo.graphql', 'repositories'),
    ('graphql/commits-on-other-repo.graphql', 'repositoriesContributedTo')
]

for graphql_path, repo_tag in commit_count_strings:
    query = Path(graphql_path).read_text()
    output = query_graphql(query, {"viewerId": viewerId})
    repos = asDict(output)['data']['viewer'][repo_tag]['nodes']

    for repo in repos:
        name = asDict(repo)['nameWithOwner']
        total_count = asDict(repo)['defaultBranchRef']['target']['history']['totalCount']
        print(total_count, name)
        overall_commits += int(total_count)

print("OVERALL:", overall_commits)
