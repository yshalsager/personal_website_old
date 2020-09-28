import re
from pathlib import Path
from typing import List

from flask import current_app
from markdown import markdown


class Post:
    title: str
    description: str
    tags: str
    date: str
    image: str

    _content_pattern = r'---[\s\S]+---\n'
    _attributes_pattern = r'(\w+)(?:: )(.*)'

    def __init__(self, file: Path):
        self.file = file
        self.raw_content = file.read_text(encoding="utf-8", errors="ignore")
        self.raw_meta = re.search(self._content_pattern, self.raw_content, re.MULTILINE)
        self.raw_meta = self.raw_meta.group() if self.raw_meta else ""
        for attribute in re.findall(self._attributes_pattern, self.raw_meta, re.MULTILINE):
            setattr(self, attribute[0], attribute[1])
        self.content = re.sub(self._content_pattern, '', self.raw_content, re.MULTILINE)
        self.html = markdown(self.content)


def get_blog_posts(lang) -> List[Post]:
    posts_dir = Path(__file__).parents[2] / Path(current_app.config['POSTS_DIR'] / Path(lang))
    posts = [Post(file) for file in posts_dir.glob(f'*.md')]
    return posts
