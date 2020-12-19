class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aya150509##@localhost:3306/sr_assessments'
    SECRET_KEY = 'prodjjhqsdkljkjhjkhqsdflkjgqksjgqfkg'
    SECURITY_PASSWORD_SALT = 'jkgdshkgsdqjhqsdgjhqsgjhqsdgiuzezaygqsddvsd'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sql3383073:24ZXKNytgY@sql3.freemysqlhosting.net:3306/sql3383073'
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'jksdhjkhsdjklhkljhqsdjklhlkjsdmlkjqsdklqsdjklqsdjqsdkljqsdhjhsgkhgsdhg'
    SECURITY_PASSWORD_SALT = 'hdksksdjqhjkqsdhljhsdqozeuiayzjbcqomiejkhklDSjhDLKJHpoopopopdssd'
    MAIL_DEFAULT_SENDER = 'elizabeth@sleepuniverse.org'
    MAIL_SERVER = 'premium39.web-hosting.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'elizabeth@sleepuniverse.org'
    MAIL_PASSWORD = '^LuDOFq}OiZc'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    UPLOAD_FOLDER = 'images'
    CORS_HEADERS = 'Content-Type'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aya150509##@localhost:3306/sr_assessments_test'
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'HQSDFJKLHQSDJKHQIUAZELkljhsdklqsddhqsdlkqsdjhsdkjh'
    SECURITY_PASSWORD_SALT = 'jqdfmklhqfjjqfdmlkjqdfmqdflkjqdfmlkj'


class DevelopmentConfigSauvegarde(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aya150509##@localhost:3306/sr_assessments_dev'
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'jksdhjkhsdjklhkljhqsdjklhlkjsdmlkjqsdklqsdjklqsdjqsdkljqsdhjhsgkhgsdhg'
    SECURITY_PASSWORD_SALT = 'hdksksdjqhjkqsdhljhsdqozeuiayzjbcqomiejkhklDSjhDLKJHpoopopopdssd'
    MAIL_DEFAULT_SENDER = 'elizabeth@sleepuniverse.org'
    MAIL_SERVER = 'premium39.web-hosting.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'elizabeth@sleepuniverse.org'
    MAIL_PASSWORD = '^LuDOFq}OiZc'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    UPLOAD_FOLDER = 'images'
    CORS_HEADERS = 'Content-Type'
