from api.utils.translate import translateLabel
from api.models.questionSkills import QuestionSkill, QuestionSkillSchema
from api.models.skills import Skill, SkillSchema


def getQuestionSkills(idSkill, idLanguage):
    fetched = QuestionSkill.query.filter_by(
        idSkill=idSkill).all()
    questionskill_schema = QuestionSkillSchema(
        many=True, only=['idQuestion'])
    questions = questionskill_schema.dump(fetched)

    return questions


def getQuestionsSkillForMatching(idSkill):
    fetched = QuestionSkill.query.filter_by(
        idSkill=idSkill).all()
    questionskill_schema = QuestionSkillSchema(
        many=True)
    questions = questionskill_schema.dump(fetched)

    return questions


def getScoreByQuestionId(idQuestion, userResponses):
    score = 0
    for userResponse in userResponses:
        if userResponse["idQuestion"] == idQuestion:
            score = userResponse["score"]
    return score
