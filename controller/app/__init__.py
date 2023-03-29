from flask_config import FLASK
import models
import forms
import views
import controller
from utils.filters import dateformat

FLASK.run(host='0.0.0.0', port=80)
