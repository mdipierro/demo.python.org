Python Distutils-SIG
====================

Tasks and Division of Labour
----------------------------

At the Seventh International Python Conference Developer's Day
    session
`"Extension Building Considered Painful" <http://www.foretec.com/python/workshops/1998-11/dd-ward-sum.html>`_,
    we enumerated the tasks necessary to develop, distribute, and
    install Python modules; arrived at a rough consensus regarding the
    division of labour necessary to conceptualize any
    distribution/installation system; and came up with a proposed user
    interface.  This document describes the tasks and division of
    labour; the `proposed user interface <../interface/>`_ is
    described elsewhere.

Three roles were identified: the developer, the packager, and the
    installer (in one sense, the end-user of the system; I'll stick to
    "installer" because he's not the *only* user).  Obviously,
    there is overlap in these roles; some tasks have to be done by both
    developer and packager, some have to be done by all three, etc.
    I'll try to associate each task with a "primary" role, and mention
    them again under other roles where they also pop up.

Developer tasks
~~~~~~~~~~~~~~~

The developer's primary tasks are:
    **MISSING**
    The developer will also have to *build* the software
    repeatedly in the course of development, which means that the
    interface for building has to be geared towards both installers
    (possibly naive end-users) and developers.  (This argues in favour
    of having two build interfaces.)  Creating a source distribution
    could be considered a packager task, but it will almost always be
    done by the developer wearing his "packager" hat; on the other hand,
    the developer may put that hat on again to create a built
    distribution for his favourite platform(s), but I've lumped that
    below under packager tasks.

Packager tasks
~~~~~~~~~~~~~~

**MISSING**
    In addition to building the software, the packager should probably
    test it before creating the built distribution.

Installer tasks
~~~~~~~~~~~~~~~

**MISSING**
    Note that these assume the installer is working from a source
    distribution -- if this is always the case, then the packager has
    wasted his time, and we don't want that.  Installing built
    distributions should be trivial, but there are a few unresolved
    concerns: how do we deal with the difference between "smart" and
    "dumb" built distributions (e.g. RPM or Wise Installer vs. a simple
    .tar or .zip file)? should the test suite
    be run when a built distribution is installed, and if so, how?