from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100))
    level1Label = db.Column(db.String(100))
    level2Label = db.Column(db.String(100))
    level3Label = db.Column(db.String(100))
    level4Label = db.Column(db.String(100))
    level5Label = db.Column(db.String(100))
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 label,
                 level1Label,
                 level2Label,
                 level3Label,
                 level4Label,
                 level5Label,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):
        self.label = label
        self.level1Label = level1Label
        self.level2Label = level2Label
        self.level3Label = level3Label
        self.level4Label = level4Label
        self.level5Label = level5Label
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a question')
        db.session.add(self)
        db.session.commit()
        return self


class QuestionSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Question
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    label = fields.String(required=True)
    level1Label = fields.String(required=True)
    level2Label = fields.String(required=True)
    level3Label = fields.String(required=True)
    level4Label = fields.String(required=True)
    level5Label = fields.String(required=True)
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
