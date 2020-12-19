from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(100))
    idSeniority = db.Column(db.Integer, db.ForeignKey('seniorities.id'))
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 label,
                 idSeniority,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):
        self.label = label
        self.idSeniority = idSeniority
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a Job')
        db.session.add(self)
        db.session.commit()
        return self


class JobSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Job
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    label = fields.String(required=True)
    idSeniority = fields.Integer(required=True)
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
