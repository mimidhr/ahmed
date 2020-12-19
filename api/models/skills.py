from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100))
    labelLevel1 = db.Column(db.String(100))
    labelLevel2 = db.Column(db.String(100))
    labelLevel3 = db.Column(db.String(100))
    labelLevel4 = db.Column(db.String(100))
    labelLevel5 = db.Column(db.String(100))
    idMasterDomain = db.Column(db.Integer, db.ForeignKey('masterDomains.id'))
    idDomain = db.Column(db.Integer, db.ForeignKey('domains.id'))
    idSubDomain = db.Column(db.Integer, db.ForeignKey('subDomains.id'))
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 label,
                 labelLevel1,
                 labelLevel2,
                 labelLevel3,
                 labelLevel4,
                 labelLevel5,
                 idMasterDomain,
                 idDomain,
                 idSubDomain,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):
        self.label = label
        self.labelLevel1 = labelLevel1
        self.labelLevel2 = labelLevel2
        self.labelLevel3 = labelLevel3
        self.labelLevel4 = labelLevel4
        self.labelLevel5 = labelLevel5
        self.idMasterDomain = idMasterDomain
        self.idDomain = idDomain
        self.idSubDomain = idSubDomain
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a Skill')
        db.session.add(self)
        db.session.commit()
        return self


class SkillSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Skill
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    label = fields.String(required=True)
    labelLevel1 = fields.String(required=False)
    labelLevel2 = fields.String(required=False)
    labelLevel3 = fields.String(required=False)
    labelLevel4 = fields.String(required=False)
    labelLevel5 = fields.String(required=False)
    idMasterDomain = fields.Integer()
    idDomain = fields.Integer()
    idSubDomain = fields.Integer()
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
