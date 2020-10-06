from pathlib import Path


class Config:
    LANGUAGES = ['en', 'ar']
    POSTS_DIR = 'posts'
    SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS = True
    BABEL_TRANSLATION_DIRECTORIES = str(Path(__file__).absolute().parent / 'personal_website/translations')
    # Logging
    LOG_TYPE = "watched"
    LOG_LEVEL = "INFO"
    # Logging file Setup
    LOG_DIR = f"{str(Path(__file__).absolute().parent)}/logs/"
    APP_LOG_NAME = "app.log"
    WWW_LOG_NAME = "www.log"
    LOG_MAX_BYTES = 100000000
    LOG_COPIES = 5
    # Domain
    DOMAIN = "https://yshalsager.me"
