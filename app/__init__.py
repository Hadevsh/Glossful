from flask import Flask

def create_app():
    app = Flask(__name__)

    from dotenv import load_dotenv
    import os

    load_dotenv()
    app.config['BabelNet'] = os.getenv("BabelNetAPI")

    from .routes import main
    app.register_blueprint(main)

    return app