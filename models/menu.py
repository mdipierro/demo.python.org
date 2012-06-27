# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))
response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2011'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

def f(a): return URL('default','index',args=a)

response.menu = [
    (T('Python.org'),False,URL('default','index')),
    (T('About'), False, False, [
            (T('Readme'),None,URL('default','index',args='about')),
            (T('Getting Started'),None,f('about/gettingstarted')),
            (T('Applications'),None,f('about/apps')),
            (T('Success Stories'),None,f('about/success')),
            (T('License'),None,'http://docs.python.org/license.html'),
            (T('Help'),None,f('about/help'))]),
    (T('News'), False, False, [
            (T('Readme'),None,URL('default','index',args='news')),
            (T('Security Advisory'),None,f('news/security')),
            (T('Release Schedule'),None,f('news/releaseschedule'))]),
    (T('Docs'), False, False,[
            (T('Beginner\'s Tutorials'),None,'http://wiki.python.org/moin/BeginnersGuide'),
            (T('Libraries'),None,'http://docs.python.org/library/'),
            (T('Core Develoment'),None,'http://docs.python.org/devguide/'),
            (T('Wiki'),None,'http://wiki.python.org/moin/'),
            (T('PEPs'),None,f('dev/peps')),
            (T('Talks'),None,'http://python.org/doc/av/')]),     
    (T('Download'), False, False,[
            (T('For Windows'),None,f('download/windows')),
            (T('For Mac'),None,f('download/mac')),
            (T('For Linux'),None,f('download/source')),
            (T('For other OS'),None,f('download/other')),
            (T('Old Releases'),None,f('download/releases'))]),
    (T('Community'), False, False,[
            (T('Readme'),None,URL('default','index',args='community')),
            (T('Mailing Lists'),None,f('community/lists')),
            (T('User Groups'),None,f('community/sigs')),
            (T('Conferences'),None,f('community/workshops')),
            (T('Jobs'),None,f('community/jobs')),
            (T('Awards'),None,f('community/awards')),
            (T('Merchanise'),None,f('community/merchandise')),
            ]),
    (T('PSF'), False, False ,[
            (T('Readme'),None,URL('default','index',args='psf')),
            (T('About the PSF'),None,f('psf/about')),
            (T('Executive Summary'),None,f('psf/summary')),
            (T('Mission Statement'),None,f('psf/mission')),
            (T('Membership'),None,f('psf/membership')),
            (T('Volunteer'),None,f('psf/volunteer')),
            (T('League'),None,f('psf/league')),
            (T('Committees'),None,f('psf/committees')),
            (T('ByLaws'),None,f('psf/bylaws')),
            (T('Reports'),None,f('psf/reports')),
            (T('Wiki'),None,'http://wiki.python.org/moin/PythonSoftwareFoundation'),
            (T('Weblog'),None,'http://pyfound.blogspot.com/'),
            (T('Press Releases'),None,'http://python.org/psf/press-release/'),
            (T('Forms'),None,f('psf/forms')),
            ]),
    ]
