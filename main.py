from get_data import GetData
from edit_banner import EditBanner

# TODO: get values from graphql
get_data = GetData()
overall_commits = get_data.get_overall_commits()

print(f"\nOverall Commits: {overall_commits}")

# TODO: edit banner svg files
EditBanner.test()