import werkzeug
from findfood.restaurant.serializers import RestaurantSerializer
from findfood.restaurant.models import Restaurant
from findfood.config.database import db
from flask_restful import Resource, reqparse


class RestaurantViewSets(Resource):

    def __init__(self):
        self.parser = RestaurantSerializer(reqparse.RequestParser()).parser
        super(RestaurantViewSets, self).__init__()

    def post(self):
        args = self.parser.parse_args()

        new_restaurant = Restaurant(name=args['name'], type=args['type'])

        db.session.add(new_restaurant)
        db.session.commit()

        return {'message': 'Restaurant added successfully',
                'data': {'name': new_restaurant.name, 'type': new_restaurant.type}}, 201

    def put(self, id):
        args = self.parser.parse_args()
        restaurant = Restaurant.query.get(id)

        if not restaurant:
            return {'message': 'Restaurant not founded!'}, 404

        restaurant.name = args['name'] or restaurant.name
        restaurant.type = args['type'] or restaurant.type

        db.session.commit()

        return {'message': 'Restaurant updated successfully!'}, 200

    def delete(self, id):
        restaurant = Restaurant.query.get(id)

        if not restaurant:
            return {'message': 'Restaurant not founded!'}, 404

        db.session.delete(restaurant)
        db.session.commit()

        return {'message': 'Restaurant deleted!'}, 204
