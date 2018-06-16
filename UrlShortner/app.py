from flask import Blueprint
from flask_restful import Api
from resources.parenthesis import ParenthesisResource
from resources.shortner import UrlResource, UrlListResource, UrlRedirectResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(UrlListResource, '/url')
api.add_resource(UrlResource, '/url/<int:id>')
api.add_resource(ParenthesisResource, '/parenthesis')


url_bp = Blueprint('url', __name__)
url = Api(url_bp)
url.add_resource(UrlRedirectResource, '/<string:short_url>')
