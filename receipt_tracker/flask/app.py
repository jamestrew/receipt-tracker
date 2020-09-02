import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return flask.render_template('layout.html')


if __name__ == "__main__":
    app.run(debug=True)