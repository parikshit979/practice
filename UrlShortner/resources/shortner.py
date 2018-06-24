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
        Url.query.filter_by(id=id).delete()
        db.session.commit()
        return {'status': 'success'}, 200


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

        print data

        url = data['url'].split('//')
        url = url[1:] if len(url) == 2 else url[:]
        url = url[0].split('/')
        url[0] = url[0].split('.')
        url[0] = ".".join(url[0][1:] if len(url[0]) == 3 else url[0][:])
        url = "/".join(url)

        id = Url.query.filter_by(url=url).first()
        if not id:
            id = Url.query.order_by('-id').first()
            if not id:
                id = 0
            short_url = host + hashids.encode(id + 1)

            data = Url(url=url, short_url=short_url)
            db.session.add(data)
            db.session.commit()
        else:
            return {'message': 'Short url already exists'}, 400

        return {'status': 'success'}, 201


class UrlRedirectResource(Resource):
    def post(self, short_url):
        id = hashids.decode(short_url)
        data = Url.query.filter_by(id=id[0]).one()
        if not data:
            return {'message': 'Short url does not exists'}, 400
        result = url_schema.dump(data).data

        return redirect("http://www." + result['url'], code=302)
