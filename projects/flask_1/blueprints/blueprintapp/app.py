from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.db'

    db.init_app(app)

    # import and register all blueprints
    from blueprintapp.todos.routes import todos
    app.register_blueprint(todos, url_prefix='/todos')

    migrate = Migrate(app, db)

    return app

