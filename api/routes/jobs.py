import os
import uuid
from flask import Blueprint, request, current_app, url_for
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.seniorities import Seniority, SenioritySchema
from api.models.languages import Language, LanguageSchema
from api.models.translations import Translation, TranslationSchema
from api.models.jobs import Job, JobSchema
from api.models.masterDomains import MasterDomain, MasterDomainSchema
from api.models.domains import Domain, DomainSchema
from api.models.subDomains import SubDomain, SubDomainSchema


#from api.models.users import User, UserSchema
from api.utils.database import db
from api.utils.translate import translateLabel
from api.utils.jobsTools import getJobDescriptions, getJobSkills
from flask_jwt_extended import jwt_required
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity
#from werkzeug.utils import secure_filename

jobs_routes = Blueprint("jobs_routes", __name__)
CORS(jobs_routes,
     resources={r"/*": {
         "origins": "http://localhost:3000"
     }})


@jobs_routes.route('/all/<idLanguage>', methods=['GET'])
# @jwt_required
def get_all_jobs(idLanguage):
    jobs = []
    fetched = Job.query.all()
    print("fetched:", fetched)
    job_schema = JobSchema(many=True, only=['id', 'label', 'idSeniority'])
    jobs_source = job_schema.dump(fetched)
    for job_source in jobs_source:
        job = {}
        job["id"] = job_source["id"]
        job["idSeniority"] = job_source["idSeniority"]
        job["jobLabel"] = translateLabel(job_source["label"], idLanguage)
        job["jobDescriptions"] = getJobDescriptions(
            job_source["id"], idLanguage)
        job["skills"] = getJobSkills(
            job_source["id"], idLanguage)
        jobs.append(job)
    return response_with(resp.SUCCESS_200, value={"jobs": jobs})


@jobs_routes.route('/one/<idJob>/<idLanguage>', methods=['GET'])
# @jwt_required
def get_job_info(idJob, idLanguage):
    job = {}
    fetched = Job.query.filter_by(
        id=idJob).all()
    job_schema = JobSchema(many=True, only=['id', 'label', 'idSeniority'])
    jobs_source = job_schema.dump(fetched)
    print("jobs_source:", jobs_source)
    for job_source in jobs_source:

        job["id"] = job_source["id"]
        job["idSeniority"] = job_source["idSeniority"]
        job["jobLabel"] = translateLabel(job_source["label"], idLanguage)
        job["jobDescriptions"] = getJobDescriptions(
            job_source["id"], idLanguage)
        job["skills"] = getJobSkills(
            job_source["id"], idLanguage)
    return response_with(resp.SUCCESS_200, value={"job": job})
