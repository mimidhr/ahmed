import os
import uuid
from flask import Blueprint, request, current_app, url_for
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.languages import Language, LanguageSchema
from api.models.translations import Translation, TranslationSchema
from api.models.questions import Question, QuestionSchema


#from api.models.users import User, UserSchema
from api.utils.database import db
from api.utils.translate import translateLabel
from flask_jwt_extended import jwt_required
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity
#from werkzeug.utils import secure_filename

questions_routes = Blueprint("questions_routes", __name__)
CORS(questions_routes,
     resources={r"/*": {
         "origins": "http://localhost:3000"
     }})


@questions_routes.route('/one/<idQuestion>/<idLanguage>', methods=['GET'])
# @jwt_required
def get_question_info(idQuestion, idLanguage):
    question = {}
    fetched = Question.query.filter_by(
        id=idQuestion).all()
    question_schema = QuestionSchema(many=True)
    questions_source = question_schema.dump(fetched)
    for question_source in questions_source:
        question["id"] = question_source["id"]
        question["questionLabel"] = translateLabel(
            question_source["label"], idLanguage)
        question["questionLevel1Label"] = translateLabel(
            question_source["level1Label"], idLanguage)
        question["questionLevel2Label"] = translateLabel(
            question_source["level2Label"], idLanguage)
        question["questionLevel3Label"] = translateLabel(
            question_source["level3Label"], idLanguage)
        question["questionLevel4Label"] = translateLabel(
            question_source["level4Label"], idLanguage)
        question["questionLevel5Label"] = translateLabel(
            question_source["level5Label"], idLanguage)

    return response_with(resp.SUCCESS_200, value={"question": question})
