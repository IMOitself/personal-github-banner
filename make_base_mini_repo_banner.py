import re
from pathlib import Path
from edit_banner import EditBanner

class MakeBaseMiniRepoBanner:
    base_svg_path = 'mini-repo-banners/base.svg'

    def generate_base_banner(self):
        reference_svg = Path('banner-recent-repo.svg').read_text(encoding='utf-8')
        new_file_content = reference_svg

# '<div class="label">recently updated repository</div>'
        # remove label
        regex_pattern = r'(<div class="label")[\s\S]*?(>[\s\S]*?</div>)'
        replacement = rf'\g<1> style="display: none;"\g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


# <svg width="680" height="230" viewBox="0 0 680 230" xmlns="http://www.w3.org/2000/svg">
        # change svg size
        w = 340 + 6 # padding 6px
        h = 167.6
        regex_pattern = r'(<svg width=")[\s\S]*?("[\s\S]*?height=")[\s\S]*?("[\s\S]*?viewBox="0 0 )[\s\S]*?("[\s\S]*?>)'
        replacement = rf'\g<1>{w}\g<2>{h}\g<3>{w} {h}\g<4>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# '<foreignObject x="0" y="0" width="680" height="230">'
        # change foreign object width and height
        regex_pattern = r'(<foreignObject[\s\S]*?width=")[\s\S]*?("[\s\S]*?height=")[\s\S]*?("[\s\S]*?>)'
        replacement = rf'\g<1>{w}\g<2>{h}\g<3>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# .banner {
#   width: 680px;
#   height: 230px;
        # change banner's actual width and height 
        regex_pattern = r'(.banner\s*{[\s\S]*?width: )[\s\S]*?(px;[\s\S]*?height: )[\s\S]*?(px;)'
        replacement = rf'\g<1>{w}\g<2>{h}\g<3>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# <div class="sparkline-graph">...</div>'
        # remove sparkline graph
        regex_pattern = r'(<div class="sparkline-graph">)[\s\S]*?(</div>)'
        replacement = rf'\g<1> \g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# <svg class="repo-header-icon" ...>...</svg>
        # remove header icon
        regex_pattern = r'(<svg class="repo-header-icon")[\s\S]*?( xmlns="http:[\s\S]*?</svg>)'
        replacement = rf'\g<1> style="display: none;"\g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# <div class="repo-updated-at">...</div>'
        # remove 'last updated at ....'
        regex_pattern = r'(<div class="repo-updated-at">)[\s\S]*?(</div>)'
        replacement = rf'\g<1> \g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# <div class="repo-body">...</div>'
        # remove repo-body margin
        regex_pattern = r'(<div class="repo-body")[\s\S]*?(>[\s\S]*?</div>)'
        replacement = rf'\g<1> style="margin: 0"\g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# <div class="repo-card">...</div>'
        # remove repo-card padding
        regex_pattern = r'(<div class="repo-card")[\s\S]*?(>[\s\S]*?</div>)'
        replacement = rf'\g<1> style="margin: 0"\g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# <div class="banner">...</div>'
        # smaller banner padding
        regex_pattern = r'(<div class="banner")[\s\S]*?(>[\s\S]*?</div>)'
        replacement = rf'\g<1> style="padding: 16px; margin: 0 3px"\g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# <div class="repo-is-archive" style="">Public archive</div>
        # shorten is archive status instead of 'Public archive'
        regex_pattern = r'(<div class="repo-is-archive"[\s\S]*?>)[\s\S]*?(</div>)'
        replacement = rf'\g<1> archive \g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# .banner { ... background-color: #2B2D5B; ... }
        # get banner background
        match = re.search(r'\.banner[\s\S]*?{[\s\S]*?(background-color:[\s\S]*?;)[\s\S]*?}', new_file_content)
        background = match.group(1).strip() if match else ''

        # remove banner background
        regex_pattern = r'(\.banner[\s\S]*?{[\s\S]*?)background-color:[\s\S]*?;([\s\S]*?})'
        replacement = rf'\g<1>\g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# .repo-card { background: transparent; ... }
        # add background to repo card
        regex_pattern = r'(\.repo-card[\s\S]*?{[\s\S]*?)background:[\s\S]*?;([\s\S]*?})'
        replacement = rf'\g<1> {background} \g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

        Path(self.base_svg_path).parent.mkdir(parents=True, exist_ok=True)
        Path(self.base_svg_path).write_text(new_file_content, encoding='utf-8')

        EditBanner.change_repo_name(self.base_svg_path, 'dummy repo name')
        EditBanner.change_repo_description(self.base_svg_path, 'dummy long ahh repo description that should be waaaaaaay too long idk')
        EditBanner.change_repo_language(self.base_svg_path, {'name': 'lolcat', 'color': "#D5B4AA"})
        EditBanner.change_repo_is_archive(self.base_svg_path, True)
        EditBanner.change_repo_commit_count(self.base_svg_path, 67)