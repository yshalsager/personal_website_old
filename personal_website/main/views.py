from flask import render_template, url_for, redirect
from . import main


@main.route('/')
def index_redirect():
    return redirect('/en/')


@main.route('/en/')
def index_en():
    return render_template('index.html', lang="en")


@main.route('/ar/')
def index_ar():
    return render_template('index_ar.html', lang="ar")


@main.route('/en/about')
def about():
    return render_template('about.html',
                           heading="About Me",
                           subheading="This is what I do",
                           lang="en",
                           image=url_for('static', filename='img/home-bg.jpg'))


@main.route('/en/blog')
def blog():
    return render_template('blog.html',
                           heading="Blog",
                           lang="en",
                           image=url_for('static', filename='img/home-bg.jpg'))
