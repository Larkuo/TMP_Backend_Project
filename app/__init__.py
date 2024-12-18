from flask import Flask
from app.extensions import db, ma, swagger, migrate
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    swagger.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.api.products import products_blueprint
    from app.api.users import user_blueprint

    app.register_blueprint(products_blueprint)
    app.register_blueprint(user_blueprint)

    with app.app_context():
        db.create_all()
    
    return app
