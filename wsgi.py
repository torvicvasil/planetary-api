from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! Teste"

@application.route("/super_simple")
def super_simple():
    return "Hello from the Planetary API."

if __name__ == "__main__":
    application.run()
