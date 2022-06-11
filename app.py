from flasgger import Swagger
from flask import Flask
from flask_migrate import Migrate

from controllers.courses import bp_course
from controllers.professors import bp_professor
from controllers.students import bp_student
from db import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(bp_professor, url_prefix='/api/v1/professors')
app.register_blueprint(bp_course, url_prefix='/api/v1/courses')
app.register_blueprint(bp_student, url_prefix='/api/v1/students')

swagger_info = {
    "swagger": "2.0",
    "info": {
        "title": "Canida",
        "description": "Course Management API",
        "contact": {
            "responsibleDeveloper": "Muhammad Nahid",
            "email": "mdnahid22@gmail.com",
            "url": "http://github.com/nahid111/canida",
        },
        "termsOfService": "#",
        "version": "0.0.1"
    },
    "basePath": "",  # base bash for blueprint registration
    "schemes": [
        "http"
    ]
}

Swagger(template=swagger_info).init_app(app)

if __name__ == "__main__":
    app.run(port=app.config['LISTEN_PORT'])
