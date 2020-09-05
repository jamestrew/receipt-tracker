from flask import Flask
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

from receipt_tracker.flask import routes  # noqa
from receipt_tracker.repo.database import db_session, init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = '2702a6eab639bd94773edb5af1875c53'
Bootstrap(app)
datepicker(app)
db = db_session
init_db()
