import re
from pathlib import Path

class EditBanner:
    @staticmethod
    def change_overall_commits(file_path, overall_commits):
        banner_content = Path(file_path).read_text(encoding='utf-8')
        
        # note: crafting a pattern is very difficult, so sadly i auto generate from ai:(
        pattern = r'(<div class="val">\s*<div class="slot-strip">\s*<div>)[\d,]+(</div>\s*<div>)[\d,]+(</div>\s*<div>)[\d,]+(</div>\s*</div>\s*</div>)'
        replacement = rf'\g<1>{overall_commits}\g<2>{overall_commits - 1}\g<3>{overall_commits - 2}\g<4>'

        new_banner_content = re.sub(pattern, replacement, banner_content)

        Path(file_path).write_text(new_banner_content, encoding='utf-8')
        print(f"\nEdited {file_path} overall commits to {overall_commits}")

    def change_days_streak(file_path, days_streak):
        banner_content = Path(file_path).read_text(encoding='utf-8')

        pattern = r'(<div class="val">\s*<div class="slot-strip">\s*<div>)[\d,]+(</div>\s*<div>)[\d,]+(</div>\s*</div>\s*</div>)'
        replacement = rf'\g<1>{days_streak}\g<2>{days_streak - 1}\g<3>'

        new_banner_content = re.sub(pattern, replacement, banner_content)

        Path(file_path).write_text(new_banner_content, encoding='utf-8')
        print(f"\nEdited {file_path} days streak to {days_streak}")

