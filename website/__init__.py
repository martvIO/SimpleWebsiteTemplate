from flask import Flask

def create_app(key):
    # Create a Flask application instance
    app = Flask(__name__)

    # Import the blueprints from their respective modules
    from .views import views
    from .auth import auth

    # Register the blueprints with the application instance
    # The blueprints handle different parts of the application
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Set the secret key for session management and security
    app.secret_key = key

    # Return the configured application instance
    return app