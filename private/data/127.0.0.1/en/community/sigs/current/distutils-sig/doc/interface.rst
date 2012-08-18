Python Distutils-SIG
====================

Proposed User Interface
-----------------------

In addition to identifying the common tasks
    and division of labour involved in developing, distributing, and
    installing Python modules, the "Extension Building Considered
    Painful" Developer's Day Session also came up with a proposed user
    interface.  The core idea of the interface is that the module
    developer would provide a small Python script, called
    setup.py for purposes of illustration (although it is
    hoped that this convention catches on!).  This script would have two
    components: meta-data about the module distribution (name, version
    number, description, etc.), written as Python code of some sort; and
    optional code to inspect the target system and carry out any needed
    pre-build configuration operations.  Only the meta-data will be
    required, and indeed it is anticipated that most module distributions
    (especially those written purely in Python) will have only the
    meta-data component.  Some ideas for how to represent the meta-data
    will be presented below.

This document describes an interface based on what we agreed upon
    at the Developer's Day session, but with a lot more detail.  (Some
    of that detail could be construed as implementation rather than
    interface, but it's important to specify it somewhere.)

Once the setup.py script is written, developers,
    packagers, and installers alike will use it to carry out all of
    their tasks that can be automated (i.e. everything except actually
    writing the modules, documentation, and test suite).  This will be
    done by running setup.py with a mandatory "command"
    argument corresponding to the task to be accomplished.  (By sheer
    coincidence, many of these commands will look a lot like traditional
    makefile targets.)

For example, the command to initiate a build is
    build.  The developer, packager, and installer (at
    least an installer working from a source distribution) will all have
    to build the module(s), using the following command:

.. code-block::

    ./setup.py build

    After building, everyone should run the test suite, using the
    test command:

.. code-block::

    ./setup.py test

    When he's happy with the state of the code, the developer will want
    to put on his first packager hat and create a source distribution:

.. code-block::

    ./setup.py dist

    or he might want to put on his other packager hat and make a built
    distribution (or this could be done by a packager for some other
    platform):

.. code-block::

    ./setup.py bdist

    If the packager is making build distributions for a system that
    supports a "smart installer" (which the distutils also support!), he 
    could make a "smart" built distribution, e.g. an RPM for the Linux
    distributions that use it:

.. code-block::

    ./setup.py bdist -rpm

    (Note the use of a command-specific option here; for instance, the 
    bdist command should also have options to enable
    generating "smart" distributions for Windows and Macintosh, assuming
    suitable smart install tools can be found for those platforms.)

By now, you're probably wondering what's *really*
    happening behind each of those commands.  It could be argued that
    that is an implementation detail that doesn't belong in an interface
    proposal, but I think that most developers, many packagers, and a
    few curious users will be inclined to look "under the hood" and see
    what's really going on as they build and install module
    distributions.  (And the unlucky ones will have to understand the
    process if things go wrong!)  So, here is a list of commands to be
    supported by setup.py (through cooperation with the
    **distutils** modules) and the actions corresponding to
    each command:

**MISSING**