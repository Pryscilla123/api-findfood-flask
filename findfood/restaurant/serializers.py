import werkzeug


class RestaurantSerializer:
    def __init__(self, parser):
        self._parser = parser

    @property
    def parser(self):
        self._parser.add_argument('name', required=True, type=str, help='A name must be passed!')
        self._parser.add_argument('type', required=True, type=str, help='A type must be passed!')
        return self._parser
