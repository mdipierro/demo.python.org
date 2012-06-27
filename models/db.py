# -*- coding: utf-8 -*-

db = DAL(DB_URI)

response.language = \
    ([e for e in T.requested_languages if e in LANGUAGES]+['en'])[0]
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)
auth.settings.actions_disabled=['register']
## configure email
mail=auth.settings.mailer
mail.settings.server = EMAIL_SERVER
mail.settings.sender = EMAIL_SENDER
mail.settings.login = EMAIL_LOGIN

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

db.define_table(
    'page',
    Field('language',writable=False,readable=False),
    Field('path',writable=False,readable=False),
    Field('title',writable=False,readable=False),
    Field('body','text'),
    Field('html','text',writable=False,readable=False),
    Field('redirect',default=None),
    auth.signature)

if RECORD_VERSIONING:
    auth.enable_record_versioning(db)
