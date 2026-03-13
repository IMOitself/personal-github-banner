import re
from pathlib import Path

class EditBanner:
    @staticmethod
    def change_overall_commits(file_path, overall_commits):
        banner_content = Path(file_path).read_text(encoding='utf-8')
        
        # TODO: do regex to replace the overall commits section
        pattern = r''
        replacement = banner_content

        Path(file_path).write_text(banner_content, encoding='utf-8')