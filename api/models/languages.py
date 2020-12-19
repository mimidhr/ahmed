from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class Language(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.String(2), primary_key=True)
    label = db.Column(db.String(100))
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 label,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):
        self.label = label
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a Language')
        db.session.add(self)
        db.session.commit()
        return self


class LanguageSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Language
        sqla_session = db.session

    id = fields.String(required=True)
    label = fields.String(required=True)
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
