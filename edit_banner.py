import re
from pathlib import Path
from datetime import datetime, timezone

class EditBanner:

    def banner_replace_content(file_path, regex_pattern, replacement):
        banner_content = Path(file_path).read_text(encoding='utf-8')
        new_banner_content = re.sub(regex_pattern, replacement, banner_content)
        Path(file_path).write_text(new_banner_content, encoding='utf-8')

    
    def change_date_to_today(file_path):
        date_today = datetime.now().strftime("%B %d, %Y")
        regex_pattern = r'(<p class="date">)[\s\S]*?(</p>)'
        replacement = rf'\g<1>{date_today}\g<2>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f"\nEdited {file_path} date to {date_today}")
        
    
    def change_overall_commits(file_path, overall_commits):
        # note: crafting a pattern is very difficult, so sadly i auto generate from ai:(
        regex_pattern = r'(<div class="val">\s*<div class="slot-strip">\s*<div>)[\d,]+(</div>\s*<div>)[\d,]+(</div>\s*<div>)[\d,]+(</div>\s*</div>\s*</div>)'
        replacement = rf'\g<1>{overall_commits:,}\g<2>{overall_commits - 1:,}\g<3>{overall_commits - 2:,}\g<4>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f"\nEdited {file_path} overall commits to {overall_commits}")


    def change_days_streak(file_path, days_streak, isStreakPaused):
        # note: ngl the pattern is from ai again :(
        style = ' style="opacity: 0.5;"' if isStreakPaused else ''
        regex_pattern = r'(<div class="days_streak")[\s\S]*?(>[\s\S]*?<div class="slot-strip">[\s\S]*?<div>)[\d,]+(</div>\s*<div>)[\d,]+(</div>\s*</div>\s*</div>)'
        replacement = rf'\g<1>{style}\g<2>{days_streak:,}\g<3>{days_streak - 1:,}\g<4>'
        
        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f"\nEdited {file_path} days streak to {days_streak}")


    def change_recent_repo_name(file_path, name):
        regex_pattern = r'(<div class="repo-name">)[\s\S]*?(</div>)'
        replacement = rf'\g<1>{name}\g<2>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f'\nEdited {file_path} recent repo name to "{name}"')
    

    def change_recent_repo_description(file_path, description):
        regex_pattern = r'(<div class="repo-desc">)[\s\S]*?(</div>)'
        replacement = rf'\g<1>{description}\g<2>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f'\nEdited {file_path} recent repo description to "{description}"')
    

    def change_recent_repo_language(file_path, language):
        language_name = language['name']
        language_color = language['color']
        
        # note: ngl the pattern is from ai again :(
        regex_pattern = r'(<div class="repo-language">[\s\S]*?<div class="repo-language-color" style="background-color:\s*)[^;"]+(;"\s*/>\s*)[\s\S]*?(\s*</div>)'
        replacement = rf'\g<1>{language_color}\g<2>{language_name}\g<3>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f'\nEdited {file_path} recent repo language to "{language}"')


    def change_recent_repo_is_archive(file_path, is_archive):
        regex_pattern = r'(<div class="repo-is-archive")[>\s\S]*?(>[\s\S]*?</div>)'
        visibility = ' style="opacity: 0;"' if not is_archive else ''
        replacement = rf'\g<1>{visibility}\g<2>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        if(is_archive):
            print(f'\nEdited {file_path} recent repo to show is-archived')
        else:
            print(f'\nEdited {file_path} recent repo to hide is-archived')
    

    def change_recent_repo_updated_at(file_path, updated_at):
        # i hate calculating time >:(
        converted_date = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).astimezone()
        time_diff = datetime.now().astimezone() - converted_date

        days_diff = time_diff.days
        seconds_diff = time_diff.seconds

        years_diff = days_diff // 365
        months_diff = days_diff // 30
        weeks_diff = days_diff // 7
        minutes_diff = seconds_diff // 60
        hours_diff = minutes_diff // 60

        if (years_diff > 0):
            display_updated_at = f"Updated {years_diff} year{'s' if years_diff > 1 else ''} ago"
        elif (months_diff > 0):
            display_updated_at = f"Updated {months_diff} month{'s' if months_diff > 1 else ''} ago"
        elif (weeks_diff > 0):
            display_updated_at = f"Updated {weeks_diff} week{'s' if weeks_diff > 1 else ''} ago"
        elif (hours_diff > 0):
            display_updated_at = f"Updated {hours_diff} hour{'s' if hours_diff > 1 else ''} ago"
        elif (minutes_diff > 0):
            display_updated_at = f"Updated {minutes_diff} minute{'s' if minutes_diff > 1 else ''} ago"
        else:
            display_updated_at = "Updated just now"

        regex_pattern = r'(<div class="repo-updated-at">)[\s\S]*?(</div>)'
        replacement = rf'\g<1>{display_updated_at}\g<2>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f'\nEdited {file_path} recent repo "updated at" to "{display_updated_at}"')
    

    def change_recent_repo_last_update_date(file_path, updated_at):
        converted_date = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).astimezone()

        last_update_date = converted_date.strftime("%B %d")
        today = datetime.now().astimezone().strftime("%B %d")

        display_date = last_update_date # ex. March 15
        if(last_update_date == today): display_date = "Today at"

        hour = int(converted_date.strftime("%I"))
        am_pm = converted_date.strftime("%p").lower()
        display_date = display_date + " " + str(hour) + am_pm

        regex_pattern = r'(<div class="repo-updated-at">)[\s\S]*?(</div>)'
        replacement = rf'\g<1>{display_date}\g<2>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f'\nEdited {file_path} recent repo "updated at" to "{display_date}"')
    
    
    def change_sparkline_graph(file_path, five_commits_additions_and_deletions):
        # oh boy this was like a challenge from leet code XD 
        y_points = []

        commit_changes = []
        for additions, deletions in five_commits_additions_and_deletions:
            commit_changes.append(additions + deletions)
        
        max_commit_change = max(commit_changes)

        for commit_change in commit_changes:
            percentage = commit_change / max_commit_change
            y_point = 200 - (percentage * 200)
            y_points.append(int(y_point))
        
        y_points.reverse() # latest commit will be at last

        # start with a flat line for about 50. 
        # also cut the end of the line as if its going straight upwards.
        combined_points = f'0,200 50,200 100,{y_points[0]} 150,200 200,{y_points[1]} 250,200 300,{y_points[2]} 350,200 400,{y_points[3]} 450,200 500,{y_points[4]} '
        combined_points += f'550,200 600,{y_points[5]} 650,200 700,{y_points[6]} 750,200 800,{y_points[7]} 850,200 900,{y_points[8]} 950,200 1000,{y_points[9]}'
        
        sparkline_svg = f"""
            <!-- DO NOT MODIFY THIS SVG:D. any edit will be overwritten -->
            <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1000 200'>
            <defs>
              <linearGradient id="spikeGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="10%" stop-color="#90fe92ff" />
                <stop offset="60%" stop-color="#90fe92ff" />
                <stop offset="80%" stop-color="#0f9657ff" />
              </linearGradient>
            </defs>
              <polyline points="{combined_points}"
                        fill="none"
                        stroke="url(#spikeGradient)"
                        stroke-width="20"
                        stroke-linejoin="round"
                        stroke-linecap="round" />
            </svg>
        """

        regex_pattern = r'(<div class="sparkline-graph">)[\s\S]*?(</div>)'
        replacement = rf'\g<1>{sparkline_svg}\g<2>'

        EditBanner.banner_replace_content(file_path, regex_pattern, replacement)
        print(f'\nEdited {file_path} sparkline graph')
