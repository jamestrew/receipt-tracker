from flask import Flask

app = Flask(__name__)

from receipt_tracker.flask import routes  # noqa
