'''Example configuration file'''
class Config(object):
    '''Main class'''
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'mail.example.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = '<user>'
    MAIL_PASSWORD = '<pwd>'
    MAIL_SUPPRESS_SEND = False
    ADMINS = ['<email>']
