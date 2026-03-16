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
EditBanner.change_recent_repo_description(banner_recent_repo, recent_repo['description'])
EditBanner.change_recent_repo_language(banner_recent_repo, recent_repo['primaryLanguage'])
EditBanner.change_recent_repo_is_archive(banner_recent_repo, recent_repo['isArchived'])

# this will run on github actions in scheduled time
# the change_recent_repo_updated_at will always update the banner
# and will make the github actions always commit
# EditBanner.change_recent_repo_updated_at(banner_recent_repo, recent_repo['pushedAt'])
EditBanner.change_recent_repo_last_update_date(banner_recent_repo, recent_repo['lastUpdateDate'])