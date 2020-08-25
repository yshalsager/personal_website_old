from flask import render_template
from flask_babel import force_locale

from utils.posts import Post

from pathlib import Path
from functools import partial


def render(lang, post: Post):
    return render_template('post.html', lang=lang, content=post.html, title=post.title,
                           description=post.description, date=post.date)


def render_func(lang, post: Post):
    if lang == "ar":
        with force_locale('ar'):
            return render(lang, post)
    return render(lang, post)


def add_posts_routes(app):
    posts_dir = Path(__file__).parents[1] / Path(app.config['POSTS_DIR'])
    for lang in app.config['LANGUAGES']:
        for file in posts_dir.glob(f'{lang}/*.md'):
            app.add_url_rule(f'/{lang}/{file.stem}',
                             file.stem,
                             partial(render_func, lang, Post(file))
                             )
