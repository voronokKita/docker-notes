from datetime import datetime

from flask_config import FLASK


@FLASK.template_filter()
def dateformat(date: datetime) -> datetime:
    return date.strftime('%Y.%b.%d %H:%M:%S %z-%Z')
