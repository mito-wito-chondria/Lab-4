import pytest

from routes import combat
from flask import Flask
from app import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
# its true that _create_app has a name
def test_create_app(bool):
    __name__ = True




