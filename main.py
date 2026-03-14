from get_data import GetData
from edit_banner import EditBanner

GetData = GetData()
overall_commits = GetData.get_overall_commits()
days_streak = GetData.get_days_streak()

banner_main = "banner-main.svg"
banner_recent_repo = "banner-recent-repo.svg"

EditBanner.change_overall_commits(banner_main, overall_commits)
EditBanner.change_days_streak(banner_main, days_streak)