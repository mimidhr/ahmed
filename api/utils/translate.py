from api.models.translations import Translation, TranslationSchema
from api.utils.database import db


def translateLabel(label, idLanguage):
    print("label:", label)
    print("idLanguage:", idLanguage)
    fetched = Translation.query.filter_by(
        label=label, idLanguage=idLanguage).all()
    #fetched = Translation.query.all()
    print("fetched:", fetched)
    translation_schema = TranslationSchema(many=True)
    result = translation_schema.dump(fetched)
    print('result:', result)
    return result[0]["translation"]
