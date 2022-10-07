from flask import  Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from decouple import config
db = SQLAlchemy()
# from registrations.register_blueprint import register_blueprint
from api.projects_views.views import project_view
from api.user.view import user as user_views

class Config:
   
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.from_object(Config)
    # app = register_blueprint(app)
    app.register_blueprint(project_view)
    app.register_blueprint(user_views)
    # app = connect_to_db(app)
    db.init_app(app)
    Migrate(app, db)

    return app
