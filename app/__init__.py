from flask import Flask, jsonify
from app.config import Configuration
from app.models.models import db, User, Location
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restx import Api
from app.routes.auth import api as auth
from app.routes.locations import api as locations
from app.routes.user import api as user
from app.routes.reviews import api as reviews
from app.routes.calendar import api as calendar


app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

jwt = JWTManager(app)
app.config.from_object(Configuration)
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=False
db.init_app(app)


api = Api(app)
api.add_namespace(auth)
api.add_namespace(locations)
api.add_namespace(user)
api.add_namespace(calendar, path="/locations/<int:location_id>/calendar")
api.add_namespace(reviews, path="/locations/<int:location_id>/reviews")


Migrate(app, db)
# run only the last command
# pipenv run flask db init
# pipenv run flask db migrate -m 'first migration'
# pipenv run flask db upgrade
