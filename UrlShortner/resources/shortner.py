from flask import request
from flask import redirect
from hashids import Hashids
from flask_restful import Resource
from model import db, Url, UrlSchema

urls_schema = UrlSchema(many=True)
url_schema = UrlSchema()

hashids = Hashids()
host = "http://127.0.0.1:5000/"


class UrlResource(Resource):
    def delete(self, id):
        url = Url.query.filter_by(id=id).delete()
        db.session.commit()

        result = url_schema.dump(url).data

        return {'status': 'success', 'data': result}, 200


class UrlListResource(Resource):
    def get(self):
        urls = Url.query.all()
        urls = urls_schema.dump(urls).data
        return {'status': 'success', 'data': urls}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        data, errors = url_schema.load(json_data)
        if errors:
            return errors, 422

        id = Url.query.filter_by(url=data['url']).first()
        if not id:
            id = Url.query.order_by('-id').first()
            if not id:
                id = 1
            short_url = host + hashids.encode(id + 1)

            data = Url(url=data['url'], short_url=short_url)
            db.session.add(data)
            db.session.commit()
        else:
            return {'message': 'Short url already exists'}, 400

        return {'status': 'success'}, 201


class UrlRedirectResource(Resource):
    def get(self, short_url):
        data = Url.query.filter_by(short_url=host + short_url).one()

        if not data:
            return {'message': 'Short url does not exists'}, 400
        result = url_schema.dump(data).data

        return redirect(result['url'], code=302)

