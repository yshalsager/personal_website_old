from pathlib import Path


class Config:
    LANGUAGES = ['en', 'ar']
    POSTS_DIR = 'posts'
    SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS = True
    BABEL_TRANSLATION_DIRECTORIES = str(Path(__file__).absolute().parent / 'personal_website/translations')
