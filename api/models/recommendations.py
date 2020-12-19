from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class Recommendation(db.Model):
    __tablename__ = 'recommendations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    index = db.Column(db.Integer)
    idTypeRecommendation = db.Column(
        db.Integer, db.ForeignKey('typesRecommendations.id'))
    idJob = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    idSkill = db.Column(db.Integer, db.ForeignKey('skills.id'))
    idDomain = db.Column(db.Integer, db.ForeignKey('domains.id'))
    idSubDomain = db.Column(db.Integer, db.ForeignKey('subDomains.id'))
    label = db.Column(db.String(100))
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 index,
                 idTypeRecommendation,
                 idJob,
                 idSkill,
                 idDomain,
                 idSubDomain,
                 label,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):
        self.index = index
        self.idTypeRecommendation = idTypeRecommendation
        self.idJob = idJob
        self.idSkill = idSkill
        self.idDomain = idDomain
        self.idSubDomain = idSubDomain
        self.label = label
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a Recommendation')
        db.session.add(self)
        db.session.commit()
        return self


class RecommendationSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Recommendation
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    index = fields.Integer(required=False)
    idTypeRecommendation = fields.Integer(required=True)
    idJob = fields.Integer(required=False)
    idSkill = fields.Integer(required=False)
    idDomain = fields.Integer(required=False)
    idSubDomain = fields.Integer(required=False)
    label = fields.String(required=True)
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
