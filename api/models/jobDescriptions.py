from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class JobDescription(db.Model):
    __tablename__ = 'jobDescriptions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idJob = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    idTypeDescription = db.Column(
        db.Integer, db.ForeignKey('typesDescriptions.id'))
    label = db.Column(db.String(100))
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 idJob,
                 idTypeDescription,
                 label,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):
        self.idJob = idJob
        self.idTypeDescription = idTypeDescription
        self.label = label
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a Job Description')
        db.session.add(self)
        db.session.commit()
        return self


class JobDescriptionSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = JobDescription
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    idJob = fields.Integer(required=True)
    idTypeDescription = fields.Integer(required=True)
    label = fields.String(required=True)
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
