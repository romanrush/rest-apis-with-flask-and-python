from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from Section5.item import Item, ItemList
from Section5.security import authenticate, identity
from Section5.settings import DEBUG
from Section5.user import UserRegister

app = Flask(__name__)
app.secret_key = "Davi"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    app.run(port=5000, debug=DEBUG)
