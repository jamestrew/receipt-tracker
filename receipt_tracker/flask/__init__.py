from flask import Flask
from receipt_tracker.repo.database import init_db, db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = '2702a6eab639bd94773edb5af1875c53'
db = db_session
init_db()


from receipt_tracker.flask import routes  # noqa
