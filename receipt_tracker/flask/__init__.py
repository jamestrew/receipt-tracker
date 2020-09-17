from flask import Flask
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from receipt_tracker.repo.sql_repo import SQLRepo
from receipt_tracker.repo.sql_config import SQL_DEV_CONFIG


app = Flask(__name__,
            static_url_path='',
            static_folder='static')
app.config['SECRET_KEY'] = '2702a6eab639bd94773edb5af1875c53'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
Bootstrap(app)
datepicker(app)

repo = SQLRepo(SQL_DEV_CONFIG)
session = repo.init_db()


@app.teardown_appcontext
def shudown_db_session(exeception=None):
    """Dispose of the current Session, if present.

    This will first call Session.close() method on the current Session, which releases any existing transactional/connection resources still being held; transactions specifically are rolled back. The Session is then discarded. Upon next usage within the same scope, the scoped_session will produce a new Session object.
    """
    session.remove()


from receipt_tracker.flask import routes  # noqa
