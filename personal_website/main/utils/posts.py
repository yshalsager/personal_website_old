import re
from pathlib import Path

from markdown import markdown


class Post:
    title: str
    description: str
    tags: str
    date: str

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
