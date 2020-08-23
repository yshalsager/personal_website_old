from flask import render_template, url_for
from . import main


@main.route('/')
def index():
    return render_template('index.html',
                           image=url_for('static', filename='img/home-bg.jpg'), safe=True)


@main.route('/about')
def about():
    return render_template('about.html',
                           heading="About Me",
                           subheading="This is what I do",
                           image=url_for('static', filename='img/home-bg.jpg'))
