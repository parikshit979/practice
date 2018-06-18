from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(250), unique=True, nullable=False)
    short_url = db.Column(db.String(250), unique=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, url, short_url):
        self.url = url
        self.short_url = short_url


class UrlSchema(ma.Schema):
    id = fields.Integer()
    url = db.Column(db.String(250), unique=True)
    short_url = fields.String()
