from decouple import config
from flask import Flask
from flask_restful import Api
from findfood.config.database import configure_database
from findfood.restaurant.viewsets import RestaurantViewSets

app = Flask(__name__)
api = Api(app)

configure_database(app)

api.add_resource(RestaurantViewSets, '/restaurant/', '/restaurant/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
