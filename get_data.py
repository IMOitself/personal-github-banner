from datetime import datetime
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
        days_streak = 0

        query = "query { viewer { contributionsCollection { contributionYears } } }"
        contribution_years = self.query_graphql(query)['data']['viewer']['contributionsCollection']['contributionYears']

        # TODO: check if latest contributed year is under current year. return 0 immediately

        for contribution_year in contribution_years:
            start = f"{contribution_year}-01-01T00:00:00Z"
            end = f"{contribution_year}-12-31T23:59:59Z"

            is_future_date = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ") > datetime.now()
            date_today = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            if(is_future_date): end = date_today

            query = Path('graphql/days-streak.graphql').read_text()
            variables = {"start": start, "end": end}
            contribution_weeks = self.query_graphql(query, variables)['data']['viewer']['contributionsCollection']['contributionCalendar']['weeks']
            contribution_weeks.reverse() # current week first

            isToday = True
            isTodayHasNoContribution = False

            for week in contribution_weeks:
                days = week['contributionDays']
                days.reverse() # latest day first
                
                
                for day in days:
                    contribution = day['contributionCount']
                    
                    # skip if today has no contribution
                    # to still count days_streaks before this day
                    if (isToday) and (contribution == 0): 
                        isTodayHasNoContribution = True
                        continue
                    isToday = False
                    # -_-_-_-_-_-_-_-_-_-_-_

                    isStreakPaused = (days_streak > 0) and (isTodayHasNoContribution)

                    if (contribution == 0): return (days_streak, isStreakPaused)
                    days_streak += 1
    
    def get_recent_repo(self):
        query = Path('graphql/recent_repo.graphql').read_text()
        repo = self.query_graphql(query, {"viewerId": self.viewerId})['data']['viewer']['repositories']['nodes'][0]
        # name
        # isArchived
        # description
        # primaryLanguage
        #   name
        #   color

        repo['lastUpdateDate'] = repo['defaultBranchRef']['target']['history']['nodes'][0]['committedDate']
        return repo
    
    def get_recent_repo_commit_additions_and_deletions(self):
        query = Path('graphql/recent_repo_commits.graphql').read_text()
        commits = self.query_graphql(query, {"viewerId": self.viewerId})['data']['viewer']['repositories']['nodes'][0]['defaultBranchRef']['target']['history']['nodes']

        commit_additions_and_deletions = []
        i = 1
        for commit in commits:
            if(commit['parents']['totalCount'] > 1): continue # exclude merge commits
            commit_additions_and_deletions.append((commit['additions'], commit['deletions']))
            if(i == 5): break
            i += 1
        return commit_additions_and_deletions