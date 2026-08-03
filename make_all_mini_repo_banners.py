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

    for graphql_path, repo_tag in target_graphql_strings:
        query = Path(graphql_path).read_text()
        repos = GetData.query_graphql(query, {"viewerId": GetData.viewerId})['data']['viewer'][repo_tag]['nodes']

        for repo in repos:
            reference_svg = Path('mini-repo-banners/base.svg').read_text(encoding='utf-8')
            repo_banner_path = f'mini-repo-banners/{repo['nameWithOwner']}.svg'
            Path(repo_banner_path).parent.mkdir(parents=True, exist_ok=True)
            Path(repo_banner_path).write_text(reference_svg, encoding='utf-8')

            if(repo['description'] is None): repo['description'] = "<i>No description.</i>"
            repo['commitCount'] = repo['defaultBranchRef']['target']['historyCommitCount']['totalCount']

            EditBanner.change_recent_repo_name(repo_banner_path, repo['nameWithOwner'])
            EditBanner.change_recent_repo_description(repo_banner_path, repo['description'])
            EditBanner.change_recent_repo_language(repo_banner_path, repo['primaryLanguage'])
            EditBanner.change_recent_repo_is_archive(repo_banner_path, repo['isArchived'])
            EditBanner.change_recent_repo_commit_count(repo_banner_path, repo['commitCount'])


# TODO: only have the repo name to <repo-owner>/<repo-name> if its not the user's repo

MakeMiniRepoBanner().generate_base_banner()
generate_mini_repo_banners()