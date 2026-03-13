import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path

class GetData:
    def __init__(self):
        load_dotenv()
        self.TOKEN = os.getenv("ACCESS_TOKEN")
        self.viewerId = self.get_viewer_id()

    def query_graphql(self, query, variables={}):
        headers = {"Authorization": f"Bearer {self.TOKEN}"}
        URL = "https://api.github.com/graphql"
        response = requests.post(URL, json={'query': query, 'variables': variables }, headers=headers)
        return eval(str(response.json()))
    # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    
    def get_viewer_id(self):
        query = "query { viewer { id } }"
        return self.query_graphql(query)['data']['viewer']['id']
    
    def get_overall_commits(self):
        overall_commits = 0

        commit_count_strings = [
            ('graphql/commits-on-own-repo.graphql', 'repositories'),
            ('graphql/commits-on-other-repo.graphql', 'repositoriesContributedTo')
        ]

        for graphql_path, repo_tag in commit_count_strings:
            query = Path(graphql_path).read_text()
            repos = self.query_graphql(query, {"viewerId": self.viewerId})['data']['viewer'][repo_tag]['nodes']

            for repo in repos:
                name = repo['nameWithOwner']
                total_count = repo['defaultBranchRef']['target']['history']['totalCount']
                print(total_count, name)
                overall_commits += int(total_count)

        return overall_commits
    
    def get_days_streak(self):
        query = Path('graphql/days-streak.graphql').read_text()
        return self.query_graphql(query)['data']['viewer']['contributionsCollection']['contributionCalendar']['totalContributions']