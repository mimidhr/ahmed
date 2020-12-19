from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class JobSkill(db.Model):
    __tablename__ = 'jobSkills'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idJob = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    idSkill = db.Column(
        db.Integer, db.ForeignKey('skills.id'))
    expectedSkillLevel = db.Column(db.Float)
    weight = db.Column(db.Float)
    averageLevel = db.Column(db.Float)
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 idJob,
                 idSkill,
                 expectedSkillLevel,
                 weight,
                 averageLevel,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):
        self.idJob = idJob
        self.idSkill = idSkill
        self.expectedSkillLevel = expectedSkillLevel
        self.weight = weight
        self.averageLevel = averageLevel
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a Job Skill')
        db.session.add(self)
        db.session.commit()
        return self


class JobSkillSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = JobSkill
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    idJob = fields.Integer(required=True)
    idSkill = fields.Integer(required=True)
    expectedSkillLevel = fields.Number(required=True)
    weight = fields.Number(required=True)
    averageLevel = fields.Number()
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
