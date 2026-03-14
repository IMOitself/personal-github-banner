from get_data import GetData
from edit_banner import EditBanner

banner_main = "banner-main.svg"
banner_recent_repo = "banner-recent-repo.svg"

GetData = GetData()
overall_commits = GetData.get_overall_commits()
days_streak, isStreakPaused = GetData.get_days_streak()

EditBanner.change_overall_commits(banner_main, overall_commits)
# isStreakPaused = True
EditBanner.change_days_streak(banner_main, days_streak, isStreakPaused)