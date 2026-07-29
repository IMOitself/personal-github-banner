import re
from pathlib import Path

class MakeBannerRepo:
    def test(self):
        base_svg = Path('banner-recent-repo.svg').read_text(encoding='utf-8')
        new_file_content = base_svg

# '<div class="label">recently updated repository</div>'
        # remove label
        regex_pattern = r'(<div class="label")[\s\S]*?(>[\s\S]*?</div>)'
        replacement = rf'\g<1> style="display: none;"\g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# '<foreignObject xmlns="http://www.w3.org/2000/svg" x="0" y="0" width="680" height="230">'
        # change banner width
        regex_pattern = r'(<foreignObject[\s\S]*?width=")[\s\S]*?("[\s\S]*?>)'
        replacement = rf'\g<1>340\g<2>'
        new_file_content = re.sub(regex_pattern, replacement, new_file_content)
        # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

        Path('repo-banners/test.svg').write_text(new_file_content, encoding='utf-8')


MakeBannerRepo().test()