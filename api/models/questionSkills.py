from api.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime


class QuestionSkill(db.Model):
    __tablename__ = 'questionSkills'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idQuestion = db.Column(db.Integer, db.ForeignKey('questions.id'))
    idSkill = db.Column(
        db.Integer, db.ForeignKey('skills.id'))
    impactQuestionOnSkill = db.Column(db.Float)
    level1AssociatedSkillLevel = db.Column(db.Float)
    level2AssociatedSkillLevel = db.Column(db.Float)
    level3AssociatedSkillLevel = db.Column(db.Float)
    level4AssociatedSkillLevel = db.Column(db.Float)
    level5AssociatedSkillLevel = db.Column(db.Float)
    creation_date = db.Column(db.DateTime, nullable=False, auto_now_add=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,
                 idQuestion,
                 idSkill,
                 level1AssociatedSkillLevel,
                 level2AssociatedSkillLevel,
                 level3AssociatedSkillLevel,
                 level4AssociatedSkillLevel,
                 level5AssociatedSkillLevel,
                 impactQuestionOnSkill,
                 creation_date=datetime.datetime.now(),
                 updated_date=datetime.datetime.now()):
        self.idQuestion = idQuestion
        self.idSkill = idSkill
        self.level1AssociatedSkillLevel = level1AssociatedSkillLevel
        self.level2AssociatedSkillLevel = level2AssociatedSkillLevel
        self.level3AssociatedSkillLevel = level3AssociatedSkillLevel
        self.level4AssociatedSkillLevel = level4AssociatedSkillLevel
        self.level5AssociatedSkillLevel = level5AssociatedSkillLevel
        self.impactQuestionOnSkill = impactQuestionOnSkill
        self.creation_date = creation_date
        self.updated_date = updated_date

    def create(self):
        print('this is the creation function of a Question Skill')
        db.session.add(self)
        db.session.commit()
        return self


class QuestionSkillSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = QuestionSkill
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    idQuestion = fields.Integer(required=True)
    idSkill = fields.Integer(required=True)
    level1AssociatedSkillLevel = fields.Number(required=True)
    level2AssociatedSkillLevel = fields.Number(required=True)
    level3AssociatedSkillLevel = fields.Number(required=True)
    level4AssociatedSkillLevel = fields.Number(required=True)
    level5AssociatedSkillLevel = fields.Number(required=True)
    impactQuestionOnSkill = fields.Number(required=True)
    creation_date = fields.DateTime(format='%Y-%m-%d')
    updated_date = fields.DateTime(format='%Y-%m-%d')
