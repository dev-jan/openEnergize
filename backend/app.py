from flask import Flask
from flask_restx import Api, Resource, fields
from endpoints import api

app = Flask(__name__)
app.config["DEBUG"] = True
api.init_app(app)

def main():
    app.run()

if __name__ == "__main__":
    main()
