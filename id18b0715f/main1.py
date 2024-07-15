from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>TVDI</h1><h2>aaaaa</h2>"

@app.route("/hello")
def hello():
    return "<h1>hello kitty 123!</h1>"

@app.route("/user/<username>")
def hello_username(username):
    return f"<h2>Hello {username}</h2>"

with app.test_request_context():
    print(url_for('index'))