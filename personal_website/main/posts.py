from datetime import datetime, timezone
from functools import partial
from pathlib import Path

from feedgen.feed import FeedGenerator
from flask import render_template, make_response, request, current_app
from flask_babel import force_locale

from .utils.posts import Post, get_blog_posts
from ..main import main


def render(lang, post: Post):
    return render_template('post.html', lang=lang, content=post.html, title=post.title,
                           description=post.description, date=post.date, image=post.image)


def render_func(lang, post: Post):
    if lang == "ar":
        with force_locale('ar'):
            return render(lang, post)
    return render(lang, post)


def add_posts_routes(app):
    posts_dir = Path(__file__).parents[1] / Path(app.config['POSTS_DIR'])
    for lang in app.config['LANGUAGES']:
        for file in posts_dir.glob(f'{lang}/*.md'):
            app.add_url_rule(f'/{lang}/blog/{file.stem}',
                             file.stem,
                             partial(render_func, lang, Post(file))
                             )


@main.route('/<lang>/rss')
def rss(lang):
    posts = get_blog_posts(lang)
    fg = FeedGenerator()
    fg.title('مدونة يوسف شعبان' if lang == 'ar' else 'yshalsager Blog')
    fg.description('آخر التدوينات على مدونتي' if lang == 'ar' else 'Latest Feeds from my blog')
    fg.link(href=current_app.config['DOMAIN'], rel='alternate')
    fg.logo(f"{current_app.config['DOMAIN']}/static/img/logo.svg")
    fg.language(lang)

    for post in posts:
        fe = fg.add_entry()
        fe.title(post.title)
        fe.link(href=f"{current_app.config['DOMAIN']}/{lang}/{post.file.stem}")
        fe.description(post.html)
        fe.pubDate(datetime.combine(datetime.strptime(post.date, "%d-%m-%Y"), datetime.min.time(), tzinfo=timezone.utc))

    response = make_response(fg.rss_str(pretty=True))
    response.headers.set('Content-Type', 'application/rss+xml')

    return response
