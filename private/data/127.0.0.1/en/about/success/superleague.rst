**MISSING**
**MISSING**

Super League Uses Python and PostgreSQL for Rapid Development
=============================================================

**MISSING**
**MISSING**
**Category:**  Software Development, Business,

**Keywords:**  Network Development, Rapid Application Development, Web2.0, XML, Sports

**Title:**  Super League Uses Python and PostgreSQL for Rapid Development

**Authors:**   Tim Parkin and Matt Goodall / Pollenation Internet

**Contact:**   `info@pollenation.net <mailto:info%40pollenation.net>`_

**Date:**   2005/06/04 15:59:02

**Web site:**  `http://www.pollenation.net/ <http://www.pollenation.net/>`_

**Summary:**  Pollenation Internet uses Python for rapid development of a high-traffic website for Super League, the premier rugby league in the UK.

**Logo:**  .. image:: /files/success/superleague/pollenation-logo.gif    :alt: /files/success/superleague/pollenation-logo.gif

Introduction
------------

`Pollenation Internet <http://pollenation.net/>`_ was approached in 2004 to develop a news, email,
match, and ticket management system for `Super League <http://superleague.co.uk/>`_, the premier rugby
league in the UK. The main constraint for the site was that it had to be live
within six weeks, in order to coincide with the start of the Tri-Nations
international rugby competition.

The Super League site was already established as the place to visit for
up-to-date news and results. In addition to the short development time frame,
the new system had to perform well from the start to keep up with existing
traffic to the site.

.. image:: /files/success/superleague/superleague-screenshot.png
   :alt: Screen Shot of the Super League Website

*Screen Shot of the Super League Website* `Zoom in 
</files/success/superleague/superleague-screenshot-large.png>`_

Python Chosen
-------------

Pollenation originally began as a technology-neutral Internet consultancy with
clients using languages such as PHP, Cold Fusion, Perl and ASP. By the time
the Super League project started, we had already developed some web based
applications in Python, including a skills matching recruitment engine and a
stock management system. We had been considering Python as our technology of
choice for some time, partly due to the advocacy of one of our staff and
partly through our positive experiences when developing these earlier
applications.

The vast majority of our clients had also expressed much less interest in
language choice and database portability than we had imagined at first,
placing a much greater emphasis on speed of development and price instead.

Given these conditions, we had come to the conclusion that a single preferred
tool set based on Python could give us a significant commercial advantage. This
approach was used in order to meet the tight delivery deadline for the Super
League project.

Nevow Web Framework
-------------------

Having worked with many web frameworks and templating systems, we had a strong
idea of our preferred way of working. `Nevow <http://www.nevow.org/>`_ uses Python's flexibility in
many innovative ways to deliver a web development framework that is used more
as a toolkit than an application server.

Nevow's templating and simplified Model-View-Controller architecture
encourages minimal markup of the areas of HTML to be replaced, modified or
reused dynamically. The effect of this is that HTML from non-technical
agencies is easily marked up for use by Nevow.

The flexibility of Nevow's URL handling also allows us to pass any 'unused'
URLs to a static directory structure, so a third party agency can add static
content, still using the site's dynamic header and navigation.

The Twisted Framework
---------------------

`Twisted <http://www.twistedmatrix.com/>`_ is an excellent general-purpose network framework that includes a full
HTTP protocol stack and web server. Twisted's web server proved more than
capable of handling the expected peak traffic, allowing us to avoid Apache
and its often complex configuration.  This made deployment and ongoing management
of the site substantially easier.

Twisted's concept of application, support for database connection pooling,
logging, scheduling, SMTP, and pluggable authentication mechanism all helped to
make development simpler and quicker.

XML Feed Processing
-------------------

Although the match management facilities allowed administration of scores,
scorers and fixtures, Super League wished to use a third party to provide the
raw data. This raw data was supplied as XML, sent over FTP. We adapted
Twisted's FTP server and integrated the FTP server into the application. This
avoided a number of problems: there was no need to install another FTP server,
the application did not need to poll a directory looking for newly uploaded
files, and we could be sure that a file was fully uploading before we processed
it. An added benefit was that we could begin to process new files the moment
the upload was complete making the whole process nearly instantaneous.

To actually parse the uploaded files we used `ElementTree <http://effbot.org/zone/element-index.htm>`_ which makes XML
trivial to work with.

Availability of Libraries
-------------------------

During the project, we made use of `YAML <http://www.yaml.org/>`_, a human-friendly data
serialization format. The pure Python implementation of YAML was missing some
required features, but these were available in the `Syck <http://whytheluckystiff.net/syck/>`_ library, which is
written in C. Using `Pyrex <http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/>`_, a Python-like language that is used to create C
modules for Python, we were very quickly able to create our own Python module
interfacing to Syck's functionality.

In general, the availability of a wide range of esoteric modules for Python,
supporting facilities such as the ability to write Microsoft Excel files, also
helped us achieve our deadlines.

Python Facilitates Outsourcing
------------------------------

During development of the project we were able to call on the services of a
consultant who had implemented league table management software before.
Unfortunately, this consultant did not have any Python experience. We asked
him to take a look at the source code to see if he could work with it or
provide suggestions and, to our surprise, he was able to provide working code
within days. This was a great testament to Python's readability and the
overall 'learnability' of the language.

Conclusion
----------

We were able to use Python to successfully meet the tight deadline for this
project with only two staff working full time on it. The resulting system
worked smoothly with over 20 page loads per second (300 requests per second)
on a 1GHz server, 1Gb RAM server.

Python's flexibility and power, the availability of professional development tools
such as `Wing IDE <http://wingware.com/products>`_ and powerful frameworks such as Twisted and Nevow, make it
possible for Pollenation to build bespoke Internet applications in what
would otherwise be impossible timeframes. The rapid development processes
used for this project were also seen by the client, Super League, to be a
business asset. The Super League website has since gone on to be an incredible
success.

As of the completion of this project, Pollenation has committed to Python,
Postgres, Twisted, and Nevow as the framework for all of its future development.

About the Authors
-----------------

*Tim Parkin and Matt Goodall are consultants for, and directors of,
Pollenation Internet Ltd, a UK based Internet Consultancy. Pollenation is the
combined skills of Tim Parkin Matt Goodall, Charlotte Britton, Damian
Staniforth and Dave Thompson, and is dedicated to the development of Internet
solutions based on Python and PostgreSQL.*