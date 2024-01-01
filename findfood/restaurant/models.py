import uuid
from sqlalchemy.dialects.postgresql import UUID
from findfood.config.database import db


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    img = db.Column(db.String(100), nullable=False)
    restaurant_address = db.relationship('Address', backref='restaurant', lazy=True)


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    line1 = db.Column(db.String(255), nullable=False)
    line2 = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    postal_code = db.Column(db.String(9), nullable=False)
    restaurant_id = db.Column(UUID(as_uuid=True), db.ForeignKey('restaurant.id'), nullable=False)

