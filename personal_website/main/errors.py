from flask import render_template, request
from flask_babel import _, force_locale

from . import main


@main.app_errorhandler(404)
@main.app_errorhandler(500)
def error_handler(e):
    error_code = e.code
    if "/ar" in request.url:
        with force_locale('ar'):
            return render_template('error.html', error_code=str(error_code), lang="ar"), error_code
    return render_template('error.html', error_code=str(error_code)), error_code
