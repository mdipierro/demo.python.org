Python Distutils-SIG
====================

(Prerequisites: please read the proposed
    interface before trying to plough through this design document;
    it is very much a sequel to the interface document.)

Design Proposal
---------------

The Distutils' point of view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**MISSING** only has to import one module,
    distutils.core.  This module is responsible for parsing
    all command-line arguments to **MISSING** (even though the
    interpretation of options is distributed across the various
    Distutils commands, and possibly the client **MISSING**).
    It also takes care of receiving control from **MISSING**,
    and passing it as appropriate to Distutils commands.  Most
    importantly, distutils.core defines the
    Distribution class, which is the heart and soul of the
    Distutils.  The client (**MISSING**) exists mainly to
    provide attributes for a Distribution instance, and all
    the Distutils commands operate on that instance.
    distutils.core also defines the Command
    class which comes in handy for implementing Distutils commands.

Speaking of Distutils commands: each one is implemented as a
    Python module, e.g. the build command is implemented by
    the distutils.build module.  Each command module is
    required to define one class, also named for the command --
    e.g. distutils.build.Build.  These command classes will
    inherit from the Command class, which (at the very
    least) will provide a means of dealing with command-specific
    options.  (Command will provide a constructor that
    takes a Distribution class and an optional list of
    arguments for this command, and parse the argument list by
    inspecting getopt-style option specifiers in the
    Command-derived instance.)  Each command class must
    provide a method run that uses the information in the
    Distribution instance and the command options to "do
    its thing".  Well-written command classes will parcel this task out
    into several well-defined (and documented) methods, so that the
    client setup.py may inherit from and override specific behaviours of
    a Distutils command class.  This also means that the
    Distribution class must have a way to communicate
    overridden command classes to the main dispatcher.

The client's point of view
~~~~~~~~~~~~~~~~~~~~~~~~~~

As I said above, the client (**MISSING**) only has to
    import distutils.core -- everything else Distutils-ish
    is taken care of by this core module.  However, the client needs a
    way to communicate its particular options into the Distutils core
    (and out to the command modules).

There are two possible schemes for this: one short and convenient
    (but not too extensible), and the other a bit verbose and clunky
    (but more OO and extensible).  There's no reason we can't have our
    cake and eat it too; the convenient interface could just be a
    wrapper around the full-blown interface for the many module
    distributions that don't need a lot of fancy customization.

First, here's an example of the simple interface, used for a
    module distribution with a single "pure Python" module (mymod.py).

.. code-block::

    from distutils.core import setup
        setup (name = "mymod",
               version = "1.2",
               author = "Greg Ward <;gward@cnri.reston.va.us>",
               description = "A very simple, one-module distribution")

    Note that we don't explicitly list **MISSING** anywhere:
    Distutils assumes that this is a one-horse distribution named after
    its sole module (mymod).

Those who enjoy defining subclasses might prefer to phrase this
    differently:

.. code-block::

    from distutils.core import Distribution, setup

        class MyDistribution (Distribution):
            name = "mymod"
            version = "1.2",
            author = "Greg Ward <;gward@cnri.reston.va.us>",
            description = "A very simple, one-module distribution")

        setup (distclass = MyDistribution)

    This is overkill for a small distribution: we're defining a new
    class solely to provide attribute values, when
    distutils.core.setup exists mainly to let us do this
    anyways.  Nevertheless, OO purists will like this -- and undoubtedly
    there will be times when the client *will* have to override
    behaviour, not just data, and the OO interface will be
    necessary.

And more complex module distributions, with lots of attributes to
    customize, might be easier to read/maintain with things broken up
    like this.  Consider a distribution with two pure Python modules
    (mymod and my_othermod) and a C extension
    (myext); the C extension must be linked with two
    ancillary C files and a C library.  Oh yeah, this distribution
    requires Python 1.5 and any version of the re module
    (ignoring the fact that one generally implies the other):

.. code-block::

    from distutils.core import Distribution, setup

        class MyDistribution (Distribution):
            name = "mydist",
            version = "1.3.4",
            author = "Greg Ward <;gward@cnri.reston.va.us>"
            description = """\
        This is an example module distribution.  It provides no useful code,
        but is an interesting example of the Distutils in action."""

            # Dependencies
            requires = { 'python': '1.5',  # I like class-based exceptions
                         're': '*',        # and I love Perl-style regexps! ;-)
                       }
            # Actual files that need to be processed and installed in some form
            py_modules = ['mymod.py', 'my_othermod.py'],
            ext_modules = {'myext.c': 
                            {'other_c': ['extra1.c', 'extra2.c'],
                             'c_libraries': ['mylib']}
                          }

        setup (distclass = MyDistribution)

A couple of things to note:
    - I'm not afraid to use deeply nested data structures; if you're           writing and distributing Python modules, this shouldn't be a           problem!
- every attribute has a particular type (string, list,           dictionary, ...)
- the attributes with complex types (especially dictionaries) will           have a well-known and well-documented internal structure, eg.   .. code-block::      """ext_modules is a hash mapping names of C source files (each         containing a Python extension module) to a nested hash of         information about how to build that module.  The allowed keys to         this nested hash are:            - other_c: other C files that must be compiled and linked with                       the main C file to create the module           - c_libraries: C libraries that must be included in the link           ...        """

No doubt the ext_modules nested hashes would have
    more options, and no doubt other Distribution
    attributes would have complex, documented structure.

Finally, the list of all Distribution attributes
    must be well-known and well-documented!  These seem to fall into a
    couple of broad categories.  Here's an initial attempt at a list:

    - Distribution meta-data       - name - version - author - description
- Dependencies         - requires
- Files to be processed and installed         - py_modules - ext_modules - doc_files
- Build directories (all under **MISSING** by default)       - build_lib      - where to put platform-independent library files - build_platlib  - where to put platform-dependent library files - build_exe      - where to put executable programs (ie. scripts) - build_html     - where to put processed documentation (HTML)
- Installation directories (under sysconfig.LIBDEST           by default)         - install_lib - install_platlib - install_exe - install_html

    ...well, that's a start.

The Distutils' point of view revisited
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To sum up, let's go through what happens when the user runs
    **MISSING**.  Whether **MISSING** is written in the
    simple (call-a-function) or general (define-a-subclass) form doesn't
    matter too much, so I won't split things up into two streams.

- **MISSING** imports distutils.core
- distutils.core startup code parses command-line           arguments: processes global options that it knows about, and           saves the rest for the client (**MISSING**) to deal           with; figures out the commands and options for each command,           saving them all up for later processing
- **MISSING** calls distutils.core.setup           (possibly with a distclass argument specifying a           subclass of Distribution, probably with a bunch           of other named arguments specifying various attributes for the           Distribution instance)
- distutils.core.setup instantiates           Distribution (or the subclass supplied by the           client), and uses its arguments (apart from           distclass) to override attributes of this           instance
- distutils.core.setup loads the command module           (eg. distutils.build)
- distutils.core.setup determines the command class           (usually just named for the command,           eg. distutils.build.Build, but possibly a class           supplied by the client as one of the attributes of the           Distribution instance) and instantiates it
- the command class constructor takes as arguments the           Distribution instance and any command-line           arguments specific to this command on the **MISSING**           command line
- the command class constructor parses its options to set/override           some instance attributes
- distutils.core.setup calls the run           method on the command object
- that method does whatever the command is supposed to do: build           modules, process documentation, install files, etc.
- distutils.core.setup determines the next command           class (if multiple commands were given), and proceeds as           before