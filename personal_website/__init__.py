from flask import Flask
from flask_babel import Babel

from config import Config

babel = Babel()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    babel.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

# @babel.localeselector
# def get_locale():
#     # return request.accept_languages.best_match(current_app.config['LANGUAGES'])
