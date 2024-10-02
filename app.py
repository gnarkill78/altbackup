#!/usr/bin/python
import flask

app = flask.Flask(__name__)
app = flask.Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def index():
    return flask.render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
