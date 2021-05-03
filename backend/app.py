import logging
import os
from flask import Flask, redirect
from .endpoints import api
from .ConsumerTrigger import start_checking
from .Configuration import get_configuration

logfile_path = 'app.log'
if os.getenv('FLASK_ENV', '') == 'development':
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Loglevel is set to debug")
else:
    logging.basicConfig(level=logging.INFO)
    logfile_path = 'backend/' + logfile_path

logfile = logging.FileHandler(logfile_path)
log_format = '%(asctime)s %(levelname)s %(name)s %(message)s'
formatter = logging.Formatter(log_format)
logfile.setFormatter(formatter)
logging.getLogger().addHandler(logfile)


logger = logging.getLogger(__name__)
logger.info("startup backend app")

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SWAGGER_UI_DOC_EXPANSION"] = 'list'
api.init_app(app)

start_checking(get_configuration())


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Origin',
        os.getenv('FLASK_CORS_ORIGIN', '*')
    )
    return response


@app.route('/')
def redirect_to_api():
    return redirect('/api/')


if __name__ == "__main__":
    app.run()
