from flask import Flask
from flask_babel import Babel
from flask_sitemap import Sitemap

from config import Config
from .main.posts import add_posts_routes

babel = Babel()
sitemap = Sitemap()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    babel.init_app(app)
    sitemap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    add_posts_routes(app)
    return app

# @babel.localeselector
# def get_locale():
#     # return request.accept_languages.best_match(current_app.config['LANGUAGES'])
