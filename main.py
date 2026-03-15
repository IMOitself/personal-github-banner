from get_data import GetData
from edit_banner import EditBanner

banner_main = "banner-main.svg"
banner_recent_repo = "banner-recent-repo.svg"

GetData = GetData()
overall_commits = GetData.get_overall_commits()
days_streak, isStreakPaused = GetData.get_days_streak()
recent_repo = GetData.get_recent_repo()

EditBanner.change_date_to_today(banner_main)
EditBanner.change_overall_commits(banner_main, overall_commits)
EditBanner.change_days_streak(banner_main, days_streak, isStreakPaused)
EditBanner.change_recent_repo_name(banner_recent_repo, recent_repo['name'])