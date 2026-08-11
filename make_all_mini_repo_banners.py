from pathlib import Path
from get_data import GetData
from edit_banner import EditBanner
from make_mini_repo_banner import MakeMiniRepoBanner

GetData = GetData()

def generate_mini_repo_banners():
    # TODO: move the getting of data to get_data
    target_graphql_strings = [
        ('graphql/commits-on-own-repo.graphql', 'repositories'),
        ('graphql/commits-on-other-repo.graphql', 'repositoriesContributedTo')
    ]

    target_graphql_index = 0

    for graphql_path, repo_tag in target_graphql_strings:
        query = Path(graphql_path).read_text()
        cursor = None
        while True:
            result = GetData.query_graphql(query, {"viewerId": GetData.viewerId, "cursor": cursor})
            data = result['data']['viewer'][repo_tag]
            repos = data['nodes']

            for repo in repos:
                reference_svg = Path(MakeMiniRepoBanner.base_svg_path).read_text(encoding='utf-8')

                try: repo['name']
                except: repo['name'] = repo['nameWithOwner']
                if(repo['description'] is None): repo['description'] = "<i>No description.</i>"
                repo['commitCount'] = repo['defaultBranchRef']['target']['historyCommitCount']['totalCount']

                repo_banner_path = f'mini-repo-banners/{repo['name']}.svg'
                Path(repo_banner_path).parent.mkdir(parents=True, exist_ok=True)
                Path(repo_banner_path).write_text(reference_svg, encoding='utf-8')
                
                EditBanner.change_recent_repo_name(repo_banner_path, repo['name'])
                EditBanner.change_recent_repo_description(repo_banner_path, repo['description'])
                EditBanner.change_recent_repo_language(repo_banner_path, repo['primaryLanguage'])
                EditBanner.change_recent_repo_is_archive(repo_banner_path, repo['isArchived'])
                EditBanner.change_recent_repo_commit_count(repo_banner_path, repo['commitCount'])
            
            if not data['pageInfo']['hasNextPage']:
                break
            cursor = data['pageInfo']['endCursor']

        target_graphql_index += 1

if not Path(MakeMiniRepoBanner.base_svg_path).exists(): MakeMiniRepoBanner().generate_base_banner()
generate_mini_repo_banners()