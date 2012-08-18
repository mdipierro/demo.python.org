SIG for Development of Persistence and Transaction Frameworks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Recent News
###########

There will be a 
`Python Persistence BOF <http://conferences.oreillynet.com/pub/w/15/bof.html>`_
at the O'Reilly Open Source Conference.

Python Persistence

Date: 07/25/2002

Time: 8:00pm - 10:00pm

Location: Grande Ballroom C in the East Tower

Moderated by: Patrick O'Brien, Orbtech

A Python Persistence Special Interest Group was recently formed to explore
ways to add basic persistence and transaction mechanisms into the core of
Python to avoid duplication of effort by a variety of projects that have
similar issues. This BOF will permit participants to ponder Python
persistence in person. In addition, anyone interested in an informal Python
Persistence breakfast discussion with Jim Fulton and Guido van Rossum is
welcome to join us at the O'Reilly Food Tent Wednesday morning at 7am.

Charter
~~~~~~~

Problem
#######

A number of projects are underway to provide persistence mechanisms
for Python.  These efforts have a number of common requirements,
including:

**MISSING**

Most of these efforts are focused on providing persistence using
   relational database data. The efforts are, for the most part,
   proceeding independently. Each will attempt to address the above
   requirements independently, with much duplication of effort.

The Zope
   Object Database (ZODB) has satisfied the above requirements
   for some time. ZODB is currently undergoing a transition from ZODB
   3, which was based on ExtensionClass, to ZODB 4, which is based on
   Python 2.2 new-style classes.  As a part of this effort, the ZODB
   persistence and transaction frameworks are being factored out of
   ZODB into separate packages, with the hope that they will be of use
   to other persistence-based frameworks.

It will be a huge duplication of effort if each of the various
   persistence projects has to address the above requirements
   independently. Worse, the resulting systems will have independent
   frameworks that are unlikely to interoperate. Objects built for one
   framework will need to be rewritten to work with another.

Proposal
########

A new persistence-SIG is proposed to explore and, if possible,
   produce persistence and transaction frameworks that can be used for
   a variety of persistence implementations, including relational
   database-based persistence and the ZODB.

Coordinator: Jeremy Hylton 

Conclusion: When 1.0 versions of the frameworks are delivered, or
               September 1, 2003, whichever is sooner.

Deliverables: PEPs documenting the frameworks created and software
                 implementing key parts of the frameworks.

Assuming that a satisfactory framework can be defined, then the
   framework and core implementations should be included in standard
   Python distributions.

Scope
#####

   The scope of this SIG includes common frameworks for:

- Transaction coordination
- Basic persistence management, in particular observing object     changes (to know when an object needs to be saved) and access (to     know when objects are used so that unused objects are removed from     memory), and
- Activation and caching, to move objects into memory when needed     and out of memory when no longer needed.

The scope does *not* include:

- Concurrency control. This is the responsibility of specific data     managers that are plugged into the frameworks. The transaction     manager simply tracks object changes and coordinates the     activities of data managers to commit (or rollback) changes in an     atomic fashion.
- Query languages.  Individual data managers or applications may     provide query facilities. While it would be cool to have a common     query facility for Python, and I would support such a project,     that would be a different project than this one.
- Integrity constraints. Some data managers, such as those based on     relational data, will need to provide facilities for low-level     integrity checks, while others, such as ZODB, will not. Similarly,     garbage collection is the responsibility of the data manager, not     the framework. Application-level integrity systems would also be     interesting, but would not depend on a persistence system.