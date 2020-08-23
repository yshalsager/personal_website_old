from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code="404", description="The requested page couldn't be found!"), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_code="500", description="Internal Server Error :("), 500
