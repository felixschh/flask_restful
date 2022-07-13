from flask_restful import Resource


class HomeRoute(Resource):
    def get(self):
        return {'hello': 'world'}