from flask import Flask
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

from receipt_tracker.repo.sql_repo import SQLRepo
from receipt_tracker.repo.sql_config import DEV_CONFIG


app = Flask(__name__)
app.config['SECRET_KEY'] = '2702a6eab639bd94773edb5af1875c53'
Bootstrap(app)
datepicker(app)

db = SQLRepo(DEV_CONFIG).init_db()


from receipt_tracker.flask import routes  # noqa
