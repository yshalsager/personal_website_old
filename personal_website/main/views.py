from flask import render_template, url_for
from . import main


@main.route('/')
def index():
    return render_template('index.html',
                           heading="Clean Blog",
                           subheading="A Blog Theme by Start Bootstrap",
                           image=url_for('static', filename='img/home-bg.jpg'))


@main.route('/about')
def about():
    return render_template('about.html',
                           heading="About Me",
                           subheading="This is what I do",
                           image=url_for('static', filename='img/home-bg.jpg'))
