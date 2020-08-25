from flask import Blueprint

main = Blueprint('main', __name__)

from .ar import views
from .en import views
from . import errors
from . import posts
