from api.utils.translate import translateLabel
from api.models.jobDescriptions import JobDescription, JobDescriptionSchema
from api.models.typesDescriptions import TypeDescription, TypeDescriptionSchema
from api.models.jobSkills import JobSkill, JobSkillSchema
from api.models.skills import Skill, SkillSchema


def getJobDescriptions(idJob, idLanguage):
    jobsDescriptions = []
    fetched = JobDescription.query.filter_by(
        idJob=idJob).all()

    jobDescription_schema = JobDescriptionSchema(many=True)
    jobsDescriptions_source = jobDescription_schema.dump(fetched)
    for jobDescription_source in jobsDescriptions_source:
        description = {}
        description["idTypeDescription"] = jobDescription_source["idTypeDescription"]
        description["descriptionLabel"] = translateLabel(
            jobDescription_source["label"], idLanguage)

        jobsDescriptions.append(description)
    return jobsDescriptions


def getJobSkills(idJob, idLanguage):
    jobsSkills = []
    fetched = JobSkill.query.filter_by(
        idJob=idJob).all()
    jobskill_schema = JobSkillSchema(
        many=True, only=['idSkill'])
    jobSkills_source = jobskill_schema.dump(fetched)
    jobSkills = []
    for jobSkill_source in jobSkills_source:
        jobSkills.append(jobSkill_source["idSkill"])

    fetchedSkills = Skill.query.filter(Skill.id.in_(jobSkills)).all()
    skill_schema = SkillSchema(many=True)
    Skills_source = skill_schema.dump(fetchedSkills)

    skills = []
    for skill_source in Skills_source:
        skill = {}

        skill["idSkill"] = skill_source["id"]
        skill["idDomain"] = skill_source["idDomain"]
        skill["idMasterDomain"] = skill_source["idMasterDomain"]
        skill["idSubDomain"] = skill_source["idSubDomain"]
        skill["label"] = translateLabel(skill_source["label"], idLanguage)
        skill["labelLevel1"] = translateLabel(
            skill_source["labelLevel1"], idLanguage)
        skill["labelLevel2"] = translateLabel(
            skill_source["labelLevel2"], idLanguage)
        skill["labelLevel3"] = translateLabel(
            skill_source["labelLevel3"], idLanguage)
        skill["labelLevel4"] = translateLabel(
            skill_source["labelLevel4"], idLanguage)
        skill["labelLevel5"] = translateLabel(
            skill_source["labelLevel5"], idLanguage)
        skills.append(skill)

    return skills


def getJobSkillsForMatching(idJob):
    fetched = JobSkill.query.filter_by(
        idJob=idJob).all()
    jobskill_schema = JobSkillSchema(
        many=True, only=['idSkill', 'expectedSkillLevel', 'weight', 'averageLevel'])
    associatedSkills = jobskill_schema.dump(fetched)
    return associatedSkills
