import os
from flask import Flask, send_from_directory
from .model import load_model

def create_app():
    # Create Flask app WITHOUT a static_folder
    app = Flask(__name__, static_folder=None)

    # Register your API blueprint
    from .routes import auth_bp
    app.register_blueprint(auth_bp)

    # Load your ML model once at startup
    load_model()

    # Serve index.html at the site root
    @app.route('/', methods=['GET'])
    def index():
        return send_from_directory(
            os.path.join(app.root_path, '..', 'public'),
            'index.html'
        )

    # Serve any other file from public/ (style.css, etc.)
    @app.route('/<path:filename>', methods=['GET'])
    def public_files(filename):
        return send_from_directory(
            os.path.join(app.root_path, '..', 'public'),
            filename
        )

    return app
