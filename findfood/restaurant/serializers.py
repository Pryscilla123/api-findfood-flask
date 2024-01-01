import werkzeug
from typing import Union
from pydantic import BaseModel, HttpUrl


class RestaurantSerializer(BaseModel):
    name: str
    type: str
    img: str
