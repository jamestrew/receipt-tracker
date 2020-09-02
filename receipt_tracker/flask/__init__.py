from flask import Flask

app = Flask(__name__)
# Secret key required to use CSRF
# Probably should use env var?
app.config['SECRET_KEY'] = '2702a6eab639bd94773edb5af1875c53'

from receipt_tracker.flask import routes  # noqa
