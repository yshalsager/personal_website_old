from flask import render_template, url_for
from flask_babel import force_locale as force_locale, _

from ..utils.posts import get_blog_posts
from .. import main


@main.route('/ar/')
def index_ar():
    with force_locale('ar'):
        return render_template('index.html', lang="ar")


@main.route('/ar/blog')
def blog_ar():
    posts = get_blog_posts('ar')
    with force_locale('ar'):
        return render_template('blog.html',
                               heading=_("Blog"),
                               image=url_for('static', filename='img/home-bg.jpg'),
                               lang='ar',
                               posts=posts)
