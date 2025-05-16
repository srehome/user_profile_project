import flask

app = flask.Flask(__name__, template_folder='../client/templates/', static_folder='../client/static/')