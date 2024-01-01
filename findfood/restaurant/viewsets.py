import cloudinary
from cloudinary.uploader import upload
from decouple import config
from werkzeug import datastructures
from findfood.restaurant.serializers import RestaurantSerializer
from findfood.restaurant.models import Restaurant
from findfood.config.database import db
from flask_restful import Resource, reqparse
from flask import request

cloudinary.config(cloud_name=config('CLOUD_NAME'), api_key=config('API_KEY'),
                  api_secret=config('API_SECRET'))


class RestaurantViewSets(Resource):

    def post(self):

        name = request.form.get("name")
        type = request.form.get("type")
        img = request.files.get("img")

        try:

            uploaded_img = upload(img)

            validated_data = RestaurantSerializer(name=name, type=type, img=uploaded_img.get('secure_url'))

            new_restaurant = Restaurant(**dict(validated_data))

            db.session.add(new_restaurant)
            db.session.commit()

            return {'message': 'Restaurant added successfully',
                    'data': {'name': new_restaurant.name, 'type': new_restaurant.type, 'img': new_restaurant.img}}, 201

        except Exception as e:
            return {'message': e}, 400

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
