import random
from flask import Flask

from routes import combat
    
def create_app():
    app = Flask(__name__)
    app.register_blueprint(combat)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)