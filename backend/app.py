import logging
from flask import Flask, redirect
from .endpoints import api
from .ConsumerTrigger import start_checking
from .Configuration import get_configuration

logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info("startup backend app")

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SWAGGER_UI_DOC_EXPANSION"] = 'list'
api.init_app(app)

start_checking(get_configuration())


@app.after_request
def after_request(response):
    # TODO: Make this policy more restrictive for security reasons
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def redirect_to_api():
    return redirect('/api/')

if __name__ == "__main__":
    app.run()
