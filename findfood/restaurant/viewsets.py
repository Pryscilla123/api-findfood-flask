import werkzeug
from findfood.restaurant.models import Restaurant
from findfood.config.database import db
from flask_restful import Resource, reqparse


class RestaurantViewSets(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='A name must be passed!', location='json')
        parser.add_argument('type', required=True, help='A type must be passed!', location='json')
        args = parser.parse_args()

        new_restaurant = Restaurant(name=args['name'], type=args['type'])

        db.session.add(new_restaurant)
        db.session.commit()

        return {'message': 'Restaurant added successfully',
                'data': {'name': new_restaurant.name, 'type': new_restaurant.type}}, 201
