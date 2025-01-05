import flask

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
