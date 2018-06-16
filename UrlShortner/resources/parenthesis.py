from flask import request
from flask_restful import Resource


class ParenthesisResource(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No input data provided'}, 400
        if not json_data['expression']:
            return {'message': 'No input data provided'}, 400

        expression = json_data['expression']

        opening = tuple('({[')
        closing = tuple(')}]')
        mapping = dict(zip(opening, closing))
        stack = []

        state = True
        for letter in expression:
            if letter in opening:
                stack.append(mapping[letter])
            elif letter in closing:
                if not stack or letter != stack.pop():
                    state = False
                    break

        state = not stack

        return {'output': state}, 200
