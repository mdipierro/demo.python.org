import os

DB_URI = 'sqlite://storage.sqlite'
EMAIL_SERVER = 'localhost'
EMAIL_SENDER = 'no-reply@example.com'
EMAIL_LOGIN = None
GOOGLE_ANALYTICS = 'unknown'
LANGUAGES = ['en']
USE_CACHE = True
DEMO_MODE = True
RECORD_VERSIONING = False
BASE_PATH = os.path.join(request.folder,'private','data','127.0.0.1')
