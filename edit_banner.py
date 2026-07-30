import re
from pathlib import Path
from datetime import datetime, timezone

class EditBanner:

    def file_replace_content(file_path, regex_pattern, replacement):
        file_content = Path(file_path).read_text(encoding='utf-8')
        new_file_content = re.sub(regex_pattern, replacement, file_content)
        Path(file_path).write_text(new_file_content, encoding='utf-8')

    
    def change_date_to_today(file_path):
        print(f"\nEditing date to today...")
        date_today = datetime.now().strftime("%B %d, %Y")
        regex_pattern = r'(<p class="date">)[\s\S]*?(</p>)'
        replacement = rf'\g<1>{date_today}\g<2>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)
        
    
    def change_overall_commits(file_path, overall_commits):
        print(f"\nEditing overall commits...")
        # note: i finally learnt how to redo the regex pattern without AI :D
        #
        #   <div class="total_commits">
        #     <div class="val">
        #       <div class="slot-strip">
        #         <div>2,530</div> <div>2,529</div> <div>2,528</div><!-- dont delete this comment -->
        #       </div>
        #     </div>
        #   </div>
        #
        slot_strip = f'<div>{overall_commits}</div> <div>{overall_commits - 1}</div> <div>{overall_commits - 2}</div>'
        regex_pattern = r'(<div class="total_commits">[\s\S]*?<div class="val">[\s\S]*?<div class="slot-strip">\s*)[\s\S]*?(\s*<!-- dont delete this comment -->)'
        replacement = rf'\g<1>{slot_strip}\g<2>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)


    def change_days_streak(file_path, days_streak, isStreakPaused):
        print(f"\nEditing days streak...")
        #
        #   <div class="days_streak">
        #     <svg class="fire_icon" width="40" height="40" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        #       <path fill-rule="evenodd" clip-rule="evenodd" d="M13.4997 4.93762C16.8478 6.87062 17.9949 11.1518 16.0619 14.4998C14.1289 17.8479 9.84775 18.995 6.4997 17.062C3.15166 15.129 2.00453 10.8479 3.93753 7.4998C4.10592 7.20813 4.29214 6.93316 4.49401 6.67548C4.69562 6.41812 5.08463 6.45704 5.28714 6.71368C5.56487 7.06565 5.88119 7.38577 6.22971 7.66764C6.56235 7.93667 7.01647 7.61943 7.00304 7.19183C7.00103 7.12812 7.00003 7.06416 7.00003 6.99997C7.00003 6.08143 7.20643 5.2111 7.57539 4.43282C8.10854 3.30822 8.98111 2.37583 10.0608 1.76798C10.3078 1.62893 10.6112 1.7522 10.7378 2.00584C11.3297 3.1927 12.2651 4.2248 13.4997 4.93762ZM14 12C14 14.2091 12.2092 16 10 16C8.08674 16 6.4791 14.6016 6.09017 12.8183C5.9966 12.3894 6.52967 12.1749 6.90396 12.4045C7.38998 12.7025 7.93731 12.8964 8.50538 12.9685C8.80801 13.0068 9.03609 12.7289 9.01482 12.4246C9.00501 12.2844 9.00002 12.1428 9.00002 12C9.00002 10.5731 9.49812 9.26254 10.3299 8.23269C10.4337 8.10417 10.599 8.04108 10.7612 8.07233C12.6063 8.4278 14 10.0511 14 12Z"/>
        #     </svg>
        #     <div class="val">
        #       <div class="slot-strip">
        #         <div>15</div> <div>14</div>
        #       <!-- dont delete this comment --></div>
        #   </div>
        #
        style = ' style="opacity: 0.5;"' if isStreakPaused else ''
        slot_strip = f'<div>{days_streak}</div> <div>{days_streak - 1}</div> <div>{days_streak - 2}</div>'

        regex_pattern = r'(<div class="days_streak")[\s\S]*?(>[\s\S]*?<div class="val">[\s\S]*?<div class="slot-strip">\s*)[\s\S]*?(\s*<!-- dont delete this comment -->)'
        replacement = rf'\g<1>{style}\g<2>{slot_strip}\g<3>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)


    def change_recent_repo_name(file_path, name):
        #
        #   <div class="repo-name">ovo</div>
        #
        print(f"\nEditing recent repo name...")
        regex_pattern = r'(<div class="repo-name">)[\s\S]*?(</div>)'
        replacement = rf'\g<1>{name}\g<2>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)
    

    def change_recent_repo_description(file_path, description):
        #
        #   <div class="repo-desc">fun website idea idk. no ai used.</div>
        #
        print(f"\nEditing recent repo description...")
        regex_pattern = r'(<div class="repo-desc">)[\s\S]*?(</div>)'
        replacement = rf'\g<1>{description}\g<2>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)
    

    def change_recent_repo_language(file_path, language):
        #
        #   <div class="repo-language">
        #     <div class="repo-language-color" style="background-color: #f1e05a;"/>
        #     JavaScript
        #   </div>
        #
        print(f"\nEditing recent repo language...")
        if(language == None):
            language_name = "idk"
            language_color = "#000000"
        else:
            language_name = language['name']
            language_color = language['color']
        
        is_hidden = ' style="display: none;"' if language == None else ''
        
        regex_pattern = r'(<div class="repo-language")[\s\S]*?(>[\s\S]*?<div class="repo-language-color" style="background-color:\s*)[\s\S]*?("/>\s*)[\s\S]*?(\s*</div>)'
        replacement = rf'\g<1>{is_hidden}\g<2>{language_color}\g<3>{language_name}\g<4>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)


    def change_recent_repo_is_archive(file_path, is_archive):
        #
        # <div class="repo-is-archive" style="display: none;">Public archive</div>
        #
        print(f"\nEditing recent repo is-archive...")
        regex_pattern = r'(<div class="repo-is-archive")[>\s\S]*?(>[\s\S]*?</div>)'
        visibility = ' style="display: none;"' if not is_archive else ''
        replacement = rf'\g<1>{visibility}\g<2>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)
            

    def change_recent_repo_last_update_date(file_path, updated_at):
        #
        #   <div class="repo-updated-at">
        #     <svg xmlns="http://www.w3.org/2000/svg" class="repo-updated-at-icon" role="presentation" viewBox="0 0 24 24"><g fill-rule="evenodd" class="wd-icon-container"><path fill-rule="nonzero" d="M6.182 17.481C7.817 19.161 9.757 20 12 20a8 8 0 0 0 8-8c0-4.418-3.532-7.931-8-8-4.478.1-7.591 3.446-7.94 7.049l-.463-.47a.5.5 0 0 0-.711 0l-.693.7a.5.5 0 0 0 .003.706l2.562 2.557a.5.5 0 0 0 .707 0l2.555-2.557a.5.5 0 0 0 .002-.705l-.695-.705a.5.5 0 0 0-.707-.005l-.546.538C6.316 9.103 8.187 6.032 12 6a6 6 0 1 1 0 12c-1.708 0-3.165-.634-4.37-1.903a.495.495 0 0 0-.705-.024s-.002.002-.004.001l-.726.698a.499.499 0 0 0-.015.707l.002.002z" class="wd-icon-fill"/><path d="M10.498 14a.491.491 0 0 1-.498-.498V9.498c0-.275.214-.498.505-.498h.99c.279 0 .505.215.505.498V12h2.502c.275 0 .498.214.498.505v.99a.496.496 0 0 1-.498.505h-4.004z" class="wd-icon-accent"/></g></svg>
        #     last updated at Today 9am
        #   </div>
        #
        print(f"\nEditing recent repo last update date...")
        converted_date = updated_at

        last_update_date = converted_date.strftime("%B %d")
        today = datetime.now().astimezone().strftime("%B %d")

        display_date = last_update_date # ex. March 15
        if(last_update_date == today): display_date = "Today"

        hour = int(converted_date.strftime("%I"))
        am_pm = converted_date.strftime("%p").lower()
        display_date = "last updated at " + display_date + " " + str(hour) + am_pm

        regex_pattern = r'(<div class="repo-updated-at">[\s\S]*?<svg[\s\S]*?</svg>\s*)[\s\S]*?(\s*</div>)'
        replacement = rf'\g<1>{display_date}\g<2>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)
    
    
    def change_sparkline_graph(file_path, five_commits_additions_and_deletions):
        print(f"\nEditing recent repo sparkline graph...")
        # oh boy this was like a challenge from leet code XD 
        y_points = []

        commit_changes = []
        for additions, deletions in five_commits_additions_and_deletions:
            change = additions + deletions
            commit_changes.append(change)
        
        max_commit_change = max(commit_changes)
        # prevent crashing if its 0
        if max_commit_change == 0: max_commit_change = 1

        for commit_change in commit_changes:
            percentage = commit_change / max_commit_change
            y_point = 200 - (percentage * 200)
            y_points.append(int(y_point))
            
        y_points.reverse() # latest commit will be at last

        if(len(y_points) < 10): 
            y_points = [200] * (10 - len(y_points)) + y_points

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

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)
    
    def change_redirect_to_recent_repo_url(file_path, url):
        #
        # <meta http-equiv="refresh" content="0; url=https://github.com/IMOitself/ovo">
        #
        print(f"\nEditing redirect to recent repo url...")
        regex_pattern = r'(<meta http-equiv="refresh" content="0; url=)[\s\S]*?(">)'
        replacement = rf'\g<1>{url}\g<2>'

        EditBanner.file_replace_content(file_path, regex_pattern, replacement)
    
