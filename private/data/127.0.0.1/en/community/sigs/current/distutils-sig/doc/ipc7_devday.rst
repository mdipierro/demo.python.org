"Extension Building Considered Painful": Session Summary
========================================================

by Greg Ward

The "Extension Building Considered Painful" session at IPC7 was
    very productive, and there was a good consensus in the room as to
    what's needed, what will work for various classes of users, and what
    ideas to steal from other related systems (the closest being Red
    Hat's RPM and Perl's MakeMaker).

Decisions made
--------------

Everyone seemed to agree with my proposed mode of operation: the
    user downloads a package, unpacks it, and runs a Python script
    tentatively called setup.py (the fact that this name
    overlaps somewhat with the module description file in the Python
    distribution and in many large module distributions is deliberate,
    and may be construed as a bug or a feature).  See below for
    arguments to setup.py and what happens when it's run.

Also, nobody disagreed with my contention that the system should
    work on "extensions" (ie. modules written in C) or plain ol'
    "modules" (written in Python) with no difference in the user
    interface.  People also seemed to accept the idea of "building"
    everything -- C modules, Python modules, eventually documentation --
    to a temporary "build library" directory, tentatively called
    blib/.  (This is one of the few implementation details
    of Perl's MakeMaker that survived the session.)  The
    blib/directory serves (at least) two purposes: it makes
    installation near-trivial, and it provides a realistic-looking
    pseudo-installation tree for running test scripts.  The actual
    structure of the blib/ tree has yet to be decided
    (although I have definite ideas of how it should look!)

We talked about terminology a bit.  This is going to be a sticky
    issue, and will have to be one of the first things we thrash out on
    a SIG.  First, *module*, *extension module*
    (*extension* for short), and *package* will keep their
    conventional Pythonic meanings: a single .py file meant
    to be imported by other modules or scripts, a module written in C,
    and a collection of modules grouped under a directory containing an
    __init__.py file.

I proposed *distribution* (or *module distribution*
    when absolute clarity is needed) as a stand-in for *package*,
    which is already taken.  A module distribution contains one or more
    modules (including extension modules), their documentation, test
    suites, and a setup.py file.  (The documentation and
    test suites are optional but strongly recommended, especially if
    anybody ever comes up with a standard way of documenting Python
    modules.  But a distribution *must* have at least one module
    and a setup.py).  A single distribution will present
    many faces to the world: the developer's source tree, a source
    distribution, various binary distributions, the final installed
    product, etc.  (As I understand things, the source and binary
    distributions are what Trove will call *resources*.)

One thing we didn't have time to decide on was a name for the
    silly thing.  For a long and formal name, my vote is **Module
    Distribution Utilities**, or **distutils** for
    short.  The short name will be needed to group all the various
    modules into a package: for instance, we plan to have
    distutils.build, distutils.install,
    distutils.gen_make, and so forth.

Roles of setup.py
-----------------

The planned interface to and tasks for setup.py
    evolved rapidly throughout the session, mainly driven by the
    division of labour identified by Eric Raymond and clearly written
    down by Greg Stein, and the workflow diagram drawn by ??? and
    expanded upon by me (see below).

It's clear that setup.py has to contain 1) metadata
    about the package, and 2) any custom code needed to configure the
    distribution for the current machine.  It's not yet clear how these
    should be expressed.  The first idea is to steal
    MakeMaker's idea of calling a function with a bunch of
    named arguments, which then does all the work behind the scenes.  An
    example setup.py using this scheme might be:

.. code-block::

    #!/usr/bin/env python

        import distutils

        distutils.setup (name = 'mymod',
                         version_from = 'mymod.py',
                         pyfiles = ['mymod.py', 'othermod.py'],
                         cfiles = ['myext.c'])

    Obviously, custom configuration code would just be written in Python
    before or after the call to distutils.setup; it's not
    clear how to make this code interact with everything that lies
    behind distutils.setup.

The main competing idea is to do things in a more OO manner, by
    defining a subclass and overriding various attributes and methods.
    Here's an off-the-cuff illustration of the concept:

.. code-block::

    #!/usr/bin/env python

        from distutils import Setup

        class MySetup (Setup):
            name = 'mydist
            version_from = 'mymod.py'
            pyfiles = ['mymod.py', 'othermod.py']
            cfiles = ['myext.c']

    In this case, it's a bit clearer how to override specific behaviour
    of all the **distutils** classes: just subclass and
    override as needed.  Obviously, all of the classes would then
    have to be well-documented!

Workflow for module distribution
--------------------------------

The figure below illustrates the workflow involved in developing,
    packaging, building, and installing a module distribution (but not
    testing or documenting it, which ultimately should also be part of
    the plan).

.. image:: workflow.gif
   :width: 610
   :height: 642
   :alt: Diagram of module distribution workflow

Note the three kinds of people present in the diagram:
    **MISSING**
    (These are the divisions of labour identified by Eric Raymond and
    Greg Stein.)  Note also that the developer, packager(s), and user(s)
    are all smiling.  This feature is planned, but not yet implemented.

Developer utilities
~~~~~~~~~~~~~~~~~~~

Obviously, the workflow starts at the top, with the developer's
    source tree.  While the developer is toiling away, he will probably
    want a Makefile that knows about building Python
    modules and extension modules (especially the latter).  Rather than
    writing his own, he can ask setup.py to generate one
    for him (presumably using the distutils.gen_make
    module):

.. code-block::

    ./setup.py gen_make

    Then the developer can run make, make
    test, and so forth, just as he's probably used to doing
    (assuming he's an old-fashioned Unix weenie!).  If he doesn't like
    Makefiles, or doesn't need one because this is a tiny little
    project, he can just ask setup.py to build, test,
    etc. directly:

.. code-block::

    ./setup.py build
        ./setup.py test

    (The idea is that setup.py will support "commands" --
    build, test, etc. -- that correspond to
    Makefile targets.  That way, nobody ever has to depend
    on a Makefile, but one can be generated for the
    developer's convenience and efficiency (especially when working on
    large distributions with lots of extension modules to be compiled).)

Packager utilities
~~~~~~~~~~~~~~~~~~

When the developer is happy with the current state of his
    module(s) and it's time for a release, he puts on his "packager" hat
    and creates a source release:

.. code-block::

    make dist
        # or, equivalently
        ./setup.py dist

    This will bundle up all the files in the distribution (as listed in
    a MANIFEST file) into an archive file of some sort --
    perhaps .tar.gz under Unix, .zip under
    Windows, etc.  The name of the archive file would be derived from
    the name and version of the module distribution:
    mydist-1.2.3.tar.gz, for instance.

If he wishes, the developer can stop there and upload his source
    release to an archive.  Or, he can create *built
    distributions* for all the architectures to which he has access.
    (Note that I'm explicitly avoiding use of the more familiar term
    *binary distribution*.  That is because a module
    distribution might well contain nothing more than .py
    files and their associated documentation.  Even in those cases,
    though, there are reasons for a downloadable resource that can be
    immediately installed.  The main reason is consistency: it's nice if
    naive users only have to deal with one kind of file for Python
    module distributions (eg. Red Hat Linux users can just download and
    install a bunch of RPMs; whether those RPMs contain .py
    or .so files or both is immaterial).  Second, there
    might be non-binary files that are generated from files in the
    source release, such as man pages generated from SGML source.  The
    built distribution for a Unix platform might include man pages ready
    for installation, so no documentation processing would be
    necessary.)

It is important to underscore the concept of packager as a
    person separate from the developer.  This is necessary to support
    built distributions for multiple platforms, since not many developers
    have access to a couple of Unix variants, Windows, and Mac --
    they'll presumably need some help to make built distributions for
    one or more platforms.  This help may come in the form of a friend
    (down the hall or around the world) who does have access to a
    particular platform; it might come in the form of someone who
    volunteers to keep certain distributions up-to-date for certain
    platforms; or it might take the form of an archive robot that
    automates the procedure.  Security concerns become increasingly more
    relevant traversing that list.

I have in mind a couple of possible interfaces for creating built
    distributions; furthermore, the idea of "dumb" vs "smart" built
    distributions has been forming in my head since Developer's Day.
    (Thus it probably doesn't really belong here, since this is meant to
    be a summary of the Developer's Day session.  So sue me.)  First,
    consider the creation of a traditional Unix built distribution: a
    .tar.gz file to be unpacked under
    /usr/local (or, more likely in the Python library
    context, /usr/local/lib/python1.x).  This could be
    accomplished with:

.. code-block::

    ./setup.py bdist

    which would do a build (to put a mock installation tree into
    ./blib/) and package the build tree to an archive file
    named after the distribution name and version number, and the
    current platform, e.g. mydist-1.2.3-sunos5.tar.gz
    or mydist-1.2.3-win32.zip.

However, there's a lot of interest in "smart" installers like Red
    Hat's RPM (and I got the impression that there are a couple of
    competing possibilities for the Windows world -- someone from the
    dark side will have to fill me in on that).  My current thinking is
    that there should be a separate command (or Makefile
    target) for each of these, so you might run 

.. code-block::

    make rpm

    on a Red Hat Linux box, and 

.. code-block::

    setup.py *xxx*

    on a Windows machine (where *xxx* is the abbreviated name of
    some smart installer for Windows).  Supporting the old-fashioned
    "dumb" built distribution model is important, though -- not everyone
    will have that fancy new installer (or they might have a different
    smart installer).

User utilities
~~~~~~~~~~~~~~

Finally, and perhaps most importantly, we most consider the lucky
    user who wishes to install a Python module distribution on his
    computer.  Users come in all shapes and sizes, but we're mainly
    concerned with two distinctions:
    - built distribution users: anyone on a popular platform for           which a built distribution is available (or necessary:            many Mac and Windows people won't have a compiler)
- source distribution users: people on less-popular platforms           for which a compiler (and other possibly necessary tools)           will most likely be available

    Obviously, things should be utterly painless and simple for naive
    users who just want to install some modules (possibly pure Python,
    possibly extensions -- it shouldn't matter!) to get something else
    working.  Smart installers like RPM will help here, but it should be
    almost as easy to start with a "dumb" built distribution or a source
    distribution.  We must also keep in mind that there will be many
    people who have to use source distributions who are not necessarily
    programmers, and just want to get this silly thing installed and
    working -- so using a source distribution should be just as easy
    (although it will require more machine time and a few more commands)
    as using a built distribution.  Even experienced hackers who
    *could* dive into the source and mess around with it, or
    fiddle with Makefiles, or supply the locations of
    needed libraries, rarely *want* to do such things.

Where to go next
----------------

First, I think this topic is big enough to warrant a new sig,
    which I'm tentatively calling the distutils-sig.  The proposed
    charter for that {will be|has been} posted to the meta-sig, so run
    over there if you think the whole concept is hopeless and you want
    to shoot me down in flames before this even gets started (or if you
    think the name sucks).

Once the sig is created, I'd like to spend *some* time
    discussing meta-issues: does anyone violently disagree with the
    whole idea? is 'distutils' a good enough name? what functionality
    should be present in the first pass, and what's needed for a full
    release?  Then we can dive into nitty-gritty design and
    implementation issues.