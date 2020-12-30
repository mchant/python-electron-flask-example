from flask_restx import Resource, reqparse

class Sample(Resource):
    def get(self):
        todo_list = {'buy': 'milk', 'wash': 'car'}
        return todo_list