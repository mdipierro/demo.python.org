**MISSING**
**MISSING**

DevNet: A web-based RSS aggregator developed in Python
======================================================

**MISSING**
**MISSING**
**Category:**  Software Development,

**Keywords:**  Web2.0,

**Title:**  DevNet: A web-based RSS aggregator developed in Python

**Author:**   Aadish Shrestha

**Date:**   2005-01-05

**Summary:**  DevNet is a web based RSS aggregator developed in Python using the Quixote web development framework.

**Logo:**  .. image:: /files/success/devnet/devnet-logo.gif    :alt: /files/success/devnet/devnet-logo.gif

Introduction
------------

DevNet provides a convenient way to keep up with changes on IT related news
sites, without re-visiting those sites manually to look for new articles. It
acts as a gateway to multiple news sites, organizes news by topic, and keeps
track of which articles have already been seen by a given user.

DevNet works by watching news feeds based on Really Simple Syndication (RSS),
a popular standard for syndicating web-based news. RSS packages news articles
as XML documents to facilitate their transfer from site to site. DevNet acts
as a web-based RSS aggregator by fetching RSS feeds from selected websites
every 2 hours and updating its database with any new items published since the
last fetch from each site.

Users can select feeds of interest from the collection of all feeds and
organize these on a customized page called ``My Feeds``. These are remembered
using cookies so registration is not required. On later visits, a user can
go directly to ``My Feeds`` and get a listing of items published in various
sites (feeds) he has subscribed to. The customized page will also display the
number of new items in each site (feed) since the user's last visit.

Architecture
------------

DevNet can be divided into 2 modules: (1) the RSS fetcher, and (2) the web
application.

The RSS fetcher is responsible for retrieving RSS feeds from selected sites at
specified time intervals. It is written in Python and uses Mark Pilgrim's
`Universal Feed Parser <http://packages.python.org/feedparser/>`_ to parse RSS feeds, and `MySQLdb <http://sourceforge.net/projects/mysql-python>`_ to store each
parsed RSS document into a `MySQL <http://www.mysql.com/>`_ database. The fetcher is multi-threaded and
is scheduled by ``cron`` to run every 2 hours.

.. image:: /files/success/devnet/devnet-arch.png
   :alt: DevNet RSS Aggregator Architecture

The web application is responsible for interacting with the user and
presenting them with the previously fetched RSS documents according to their
interest and time of previous visit. This part of DevNet was written using the
`Quixote <http://www.mems-exchange.org/software/quixote/>`_ web development framework and `simpleTAL <http://www.owlfish.com/software/simpleTAL/>`_ for generating HTML
from templates. It is a 3-tiered application, with application logic
implemented in ``lib.py`` and the user interface in ``web.py``. The code in
``web.py`` uses simpleTAL templates to generate HTML. These templates are
compiled to HTML on the first request received and then cached. On consecutive
requests the cached HTML pages are served until the cache expires, at which
time the templates are recompiled.

The DevNet web application runs as a cgi script on a Linux server using
Apache. However, the Quixote web application framework is not Apache-specific,
so other other web servers capable of executing CGI scripts can also be used.
In fact, the development of DevNet was done using `Medusa <http://www.amk.ca/python/code/medusa.html>`_.

Why Python?
-----------

The author had two reasons to undertake this project: 

- To save time keeping up with IT related news.

- To learn Python.

DevNet is a fairly simple application, so it was appropriate as a first
project while learning Python. The first prototype version of DevNet used
Quixote's PTL for templating and had no database.  Python made development
of this prototype very rapid, despite the author's initial unfamiliarity
with the language.

After this was completed, the rapid development nature of Python made it easy
to throw away the prototype and rewrite DevNET, again quite quickly, using the
architecture described above.

Conclusion
----------

Learning Python and writing DevNet at the same time was an enjoyable
experience. With Python, application development is fast and the learning
curve is easy to manage.

About the Author
----------------

Aadish Shrestha *is currently pursuing a Masters in Venture Technology
Management at Hoseo University, South Korea. He worked previously as lead
systems administrator at an ISP in his home country of Nepal, and has a degree
in Computer Science and Engineering from Kathmandu University, Nepal.*