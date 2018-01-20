"""
Default configuration
If you want to replace some variable you have to make separate file config.py and
place this variables there. Minimum to use mail service is to provide valid
MAIL_USERNAME and MAIL_PASSWORD
"""
DEBUG = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEFAULT_SENDER = 'picam@picam.pl'
MAIL_USERNAME = 'accountname@mail.com'
MAIL_PASSWORD = 'password'
