import os
import logging
import sys
from flask import Flask
from flask import jsonify, send_from_directory
from flask_cors import CORS
from api.utils.database import db
from api.utils.migrate import migrate
from api.utils.responses import response_with
import api.utils.responses as resp
from api.config.config import DevelopmentConfig

# Routes registration

from api.routes.jobs import jobs_routes
from api.routes.questions import questions_routes
from api.routes.assessments import assessments_routes

# Import email
from api.utils.email import mail


from flask_jwt_extended import JWTManager

app = Flask(__name__)

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

db.init_app(app)
jwt = JWTManager(app)
mail.init_app(app)
migrate.init_app(app, db)


with app.app_context():
    db.create_all()

# Definition of the Blueprint routes

app.register_blueprint(jobs_routes, url_prefix='/api/jobs')
app.register_blueprint(questions_routes, url_prefix='/api/questions')
app.register_blueprint(assessments_routes, url_prefix='/api/assessments')


# START GLOBAL HTTP CONFIGURATIONS
@app.after_request
def add_header(response):
    return response


@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)


db.init_app(app)

with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)
