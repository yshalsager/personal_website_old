from flask import render_template, url_for, redirect
from flask_babel import _

from ..utils.posts import get_blog_posts
from .. import main


@main.route('/')
def index_redirect():
    return redirect('/en/')


@main.route('/en/')
def index_en():
    return render_template('index.html', lang="en")


@main.route('/en/about')
def about_en():
    return render_template('about.html',
                           lang="en",
                           heading=_("About Me"),
                           image=url_for('static', filename='img/home-bg.jpg'))


@main.route('/en/blog')
def blog_en():
    posts = get_blog_posts('en')
    return render_template('blog.html',
                           heading=_("Blog"),
                           image=url_for('static', filename='img/home-bg.jpg'),
                           lang='en',
                           posts=posts)


@main.route('/en/projects')
def projects_en():
    return render_template('projects.html',
                           lang="en",
                           heading=_("My Projects"),
                           image=url_for('static', filename='img/home-bg.jpg'))
