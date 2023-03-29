import secrets
from random import randint

from flask import Flask


FLASK = Flask('notes_controller')

FLASK.config.update(
    ENV='development',
    DEBUG=True,
    TESTING=True,
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='flask_controller',
    SECRET_KEY=secrets.token_urlsafe(randint(40, 60)),
    MAX_CONTENT_LENGTH=15*1024*1024,
)
