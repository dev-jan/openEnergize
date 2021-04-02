from flask import Flask
from flask_restx import Api, Resource, fields
from .endpoints import api

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SWAGGER_UI_DOC_EXPANSION"] = 'list'
api.init_app(app)

@app.after_request
def after_request(response):
    # TODO: Make this policy more restrictive for security reasons
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def main():
    app.run()

if __name__ == "__main__":
    main()
