import uuid
from sqlalchemy.dialects.postgresql import UUID
from findfood.config.database import db


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Restaurant {self.name}>'
