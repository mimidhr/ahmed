import os
import uuid
from flask import Blueprint, request, current_app, url_for
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.languages import Language, LanguageSchema
from api.models.translations import Translation, TranslationSchema


#from api.models.users import User, UserSchema
from api.utils.database import db
from api.utils.translate import translateLabel
from api.utils.skillsTools import getQuestionSkills, getQuestionsSkillForMatching, getScoreByQuestionId
from api.utils.jobsTools import getJobDescriptions, getJobSkills, getJobSkillsForMatching
from flask_jwt_extended import jwt_required
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity
#from werkzeug.utils import secure_filename

assessments_routes = Blueprint("assessments_routes", __name__)
CORS(assessments_routes,
     resources={r"/*": {
         "origins": "http://localhost:3000"
     }})


@assessments_routes.route('/initialisation/<idJob>/<idLanguage>', methods=['GET'])
# @jwt_required
def get_questions_for_assessment(idJob, idLanguage):
    questions = []
    associatedskills = getJobSkills(idJob, idLanguage)
    for associatedskill in associatedskills:
        assosiatedquestions = getQuestionSkills(
            associatedskill["idSkill"], idLanguage)
        questions.append(assosiatedquestions)
    return response_with(resp.SUCCESS_200, value={"questions": questions})


@assessments_routes.route('/operations/matching/', methods=['POST'])
# @jwt_required
def calculate_maching():
    userResponses = request.get_json()
    idJob = userResponses["idJob"]
    sumWeightedSkillLevel = 0
    SumWeight = 0
    associatedSkills = getJobSkillsForMatching(idJob)
    for associatedSkill in associatedSkills:
        questions = getQuestionsSkillForMatching(associatedSkill["idSkill"])
        sumImpactQuestionOnSkill = 0
        sumPonderedLevel = 0
        for question in questions:
            userScore = getScoreByQuestionId(
                question['idQuestion'], userResponses['questions'])
            expectedSkillLevel = associatedSkill['expectedSkillLevel']
            impactQuestionOnSkill = question['impactQuestionOnSkill']
            associatedSkillLevel = 0
            if userScore == 1:
                associatedSkillLevel = question['level1AssociatedSkillLevel']
            if userScore == 2:
                associatedSkillLevel = question['level2AssociatedSkillLevel']
            if userScore == 3:
                associatedSkillLevel = question['level3AssociatedSkillLevel']
            if userScore == 4:
                associatedSkillLevel = question['level4AssociatedSkillLevel']
            if userScore == 5:
                associatedSkillLevel = question['level5AssociatedSkillLevel']

            if associatedSkillLevel >= expectedSkillLevel:
                level = 100
            else:
                level = 100 * associatedSkillLevel / expectedSkillLevel

            sumPonderedLevel = sumPonderedLevel + \
                (level * impactQuestionOnSkill)

            sumImpactQuestionOnSkill = sumImpactQuestionOnSkill + impactQuestionOnSkill

        skillLevel = sumPonderedLevel / sumImpactQuestionOnSkill
        associatedSkill["skillLevel"] = skillLevel

        weight = associatedSkill["weight"]
        sumWeightedSkillLevel = sumWeightedSkillLevel + (skillLevel * weight)
        SumWeight = SumWeight + weight
    jobLevel = sumWeightedSkillLevel / SumWeight
    return response_with(resp.SUCCESS_200, value={"jobLevel": jobLevel, "associatedSkills": associatedSkills})
