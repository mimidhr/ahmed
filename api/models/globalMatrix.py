from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class GlobalMatrix(db.Model):
    __tablename__ = 'globalMatrix'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idJob = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    idQuestion = db.Column(db.Integer, db.ForeignKey('questions.id'))
    idSkill = db.Column(db.Integer, db.ForeignKey('skills.id'))
    expectedSkillLevel = db.Column(db.Float)
    impactQuestionOnSkill = db.Column(db.Float)
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 idJob,
                 idQuestion,
                 idSkill,
                 expectedSkillLevel,
                 impactQuestionOnSkill,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):

        self.idJob = idJob
        self.idQuestion = idQuestion
        self.idSkill = idSkill
        self.expectedSkillLevel = expectedSkillLevel
        self.impactQuestionOnSkill = impactQuestionOnSkill
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a global Matrix')
        db.session.add(self)
        db.session.commit()
        return self


class GlobalMatrixSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = GlobalMatrix
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    idJob = fields.Integer(required=True)
    idQuestion = fields.Integer(required=True)
    idSkill = fields.Integer(required=True)
    expectedSkillLevel = fields.Number(required=True)
    impactQuestionOnSkill = fields.Number(required=True)
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
