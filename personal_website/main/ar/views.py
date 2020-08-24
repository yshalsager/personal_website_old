from flask import render_template
from flask_babel import force_locale as force_locale
from .. import main


@main.route('/ar/')
def index_ar():
    with force_locale('ar'):
        return render_template('index.html', lang="ar")
