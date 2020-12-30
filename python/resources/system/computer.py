from flask_restx import Resource, reqparse
import platform

class Computer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('item', required=False)
    def get(self):
        data = self.parser.parse_args()
        item = data['item']
        if not item:
            return {'msg': 'wrong argument'}, 400
        if item == 'computer_name':
            return platform.node()
        else:
            return {'msg': 'wrong argument'}, 400
