import logging
from datetime import datetime

from flask import Flask, request
from flask_babel import Babel
from flask_sitemap import Sitemap

from config import Config
from logger import LogSetup
from .main.posts import add_posts_routes

babel = Babel()
sitemap = Sitemap()
logs = LogSetup()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    babel.init_app(app)
    sitemap.init_app(app)
    logs.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    add_posts_routes(app)

    @app.after_request
    def after_request(response):
        """ Logging after every request. """
        logger = logging.getLogger("app.access")
        logger.info(
            "%s [%s] %s %s %s %s %s %s %s",
            request.remote_addr,
            datetime.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        return response

    return app

# @babel.localeselector
# def get_locale():
#     # return request.accept_languages.best_match(current_app.config['LANGUAGES'])
