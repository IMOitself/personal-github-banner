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
        regex_pattern = r'(<p class="date">)MARCH 5, 2026(</p>)'
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
        regex_pattern = r'(<div class="val">\s*)<div class="slot-strip"[^>]*>(\s*<div>)[\d,]+(</div>\s*<div>)[\d,]+(</div>\s*</div>\s*</div>)'
        style = ' style="opacity: 0.5;"' if isStreakPaused else ''
        replacement = rf'\g<1><div class="slot-strip"{style}>\g<2>{days_streak:,}\g<3>{days_streak - 1:,}\g<4>'

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
        # TODO: show what time of day it was updated e.g 5:00 PM
        pass
