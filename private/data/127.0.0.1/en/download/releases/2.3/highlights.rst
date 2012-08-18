What's new in Python 2.3
------------------------

Here are the (subjective) highlights of what's new in Python 2.3.

Faster
------

According to a couple of `simple benchmark <http://mail.python.org/pipermail/python-dev/2003-July/036864.html>`_, Python 2.3 is about 20-30% faster than Python
2.2.3.  Some of this speed-up was obtained by removing the SET_LINENO
opcodes, which means that the difference is less impressive when
comparing &quot;python -O&quot;; the rest was various careful tune-ups.

New Tools
---------

A brand new version of
`IDLE </idle/>`_ (from the
`IDLEfork project <http://idlefork.sf.net>`_ at
SourceForge) is now included as Lib/idlelib.  The old Tools/idle is
no more.

New or upgraded built-ins
-------------------------

- ``sum()`` - a new function to sum a sequence of numbers. &quot;sum(seq, start)&quot; is faster and easier to understand than &quot;reduce(operator.add, seq, start)&quot;.  (New in 2.3b1.)

- ``enumerate()`` - an iterator taking a sequence returning tuples of (index, item).  This solves the old &quot;for i in range(len(seq))&quot; problem more elegantly.  (`PEP 279 </dev/peps/pep-0279>`_)

- ``basestring`` - an abstract string type which is the base class for str (8-bit strings) and unicode.  Primarily used to simplify tests for string-ness to isinstance(x, basestring).

- ``bool, True, False`` - these were introduced as ints in Python 2.2.1, but are now a separate type (a subtype of int).  This means that True and False are now printed as the strings 'True' and 'False', respectively.  As of 2.3b1, bool() without arguments returns False. (`PEP 285 </dev/peps/pep-0285>`_)

- ``compile(), eval(), exec`` - fully support Unicode, and no longer issue a SyntaxError when their input doesn't end with a newline.  (New in 2.3a2.)

- ``range()`` - as of 2.3b1 supports long arguments with a magnitude larger than sys.maxint.  E.g., range(2**100, 2**101, 2**100) is the following list:   [1267650600228229401496703205376L].

- ``dict()`` - two new features for dict construction: keyword arguments to the dict() constructor are now a shorthand for creating a dictionary from the key/value pairs, and dict.fromkeys(iterable) returns a dict whose keys are taken from the given iterable (the values default to None).  Also a new dict method was added, pop(key), which removes and returns the value corresponding to the given key.

- ``filter()`` - now returns Unicode when the input is Unicode. Various bugs with subclasses of built-in types fixed.  (New in 2.3a2.)

- ``int()`` - this can now return a long when converting a string with many digits, rather than raising OverflowError.  (New in 2.3a2: issues a FutureWarning when sign-folding an unsigned hex or octal literal.)

- ``isinstance(), super()`` - Now support instances whose type() is not equal to their __class__.  (New in 2.3a2.)  As of 2.3b1, super() no longer ignores data descriptors, except for __class__.

- ``raw_input()`` - can now return Unicode objects (if sys.stdin is Unicode-capable).  (New in 2.3a2.)

- ``slice()`` and ``buffer()`` - these are now types rather than functions.  The constructors have the same signature as the functions in the past.

- ``PyThreadState_SetAsyncEnc()`` - A new API (deliberately accessible only from C) to interrupt a thread by sending it an exception.

New or upgraded modules and packages
------------------------------------

- Many new ``doctest`` extensions from Jim Fulton, which among other enhancements, allows doctests to be run by unittests.

- ``csv`` - support for reading and writing files in so-called comma-separated-value format.  (New in 2.3b1.)

- ``timeit`` - module to time the speed of code snippets.  (New in 2.3b1.)

- ``platform`` - find out everything you always wanted to know about your platform, but were afraid to ask.  (New in 2.3b1; by Marc-Andre Lemburg.)

- ``shelve`` - optionally supports automatic writeback, and exposes pickle protocol versions.  (New in 2.3b1.)

- ``DocXMLRPCServer`` - a self-documenting XML server library. (New in 2.3b1.)

- ``rotor`` - this module is deprecated.  It is too easily cracked.  (New in  2.3b1.)

- ``re`` - the .*? pattern is now special-cased to avoid the recursion limit.  (New in 2.3b1.)

- ``Bastion`` and ``rexec`` - these modules are *disabled*, because they aren't safe in Python 2.3 (nor in Python 2.2).  (New in 2.3a2.)

- ``bsddb`` - the old bsddb module has finally been retired.  The formerly 3rd party `PyBSDDB <http://pybsddb.sf.net/>`_ wrapper is now available in Python 2.3, as the bsddb package.  This is compatible with `Sleepycat Berkeley DB <http://www.sleepycat.com/>`_ versions 3.0 to 4.1.  New in 2.3a2: the Windows installer now ships with Sleepycat's 4.1.25.NC, the latest release without strong cryptography.     The old bsddb module code is still available as the bsddb185 module, but this is not built by default.  Should you still be using a system which only has Berkeley DB 1.85 installed (often indicated by the presence of /usr/include/db.h but not /usr/lib/libdb.a file), the following changes should keep you running.   - Add this line:      .. code-block::      bsddb185 bsddbmodule.c     to Modules/Setup. In most cases you should not require any -I, -L or -l flags.  It seems on those systems which still ship 1.85, /usr/include/db.h is the include file and the symbols are present in libc.    To force that version of the module to be used as the default when importing the name &quot;bsddb&quot;, add the following line to your sitecustomize.py file:     .. code-block::      import bsddb185 as bsddb

- ``bz2`` - interface to the bz2 compression library, by Gustavo Niemeyer.

- ``datetime`` - a fast, compact implementation in C of date and time calculations ranging from the year 1 to 9999, with optional timezone support; written by Tim Peters.  (New in 2.3a2: too much to list here; see `Misc/NEWS <NEWS.txt>`_.)

- ``heapq`` - implements the heap queue algoritm known from 1st year algorithms classes.  Code by Kevin O'Connor, write-up by Fran?ois Pinard, many improvements by Tim Peters.

- ``imaplib`` - added SSL support.

- ``imp`` - exposed the &quot;import lock&quot;.  (New in 2.3a2.)

- ``itertools`` - high speed, memory efficient looping constructs inspired by Haskell and SML.  (New in 2.3a2.)  (Some improvements in 2.3b1, including subsumption of times() into repeat(), and addition of chain() and cycle().)

- ``logging`` - a flexible, configurable logging package based on log4j and our own `PEP 282 </dev/peps/pep-0282>`_; written by Vinay Sajip.  (New in 2.3a2: warn/WARN renamed to warning/WARNING; logging module actually included in the Windows installer.)

- ``optparse`` - a powerful command line option parser, by Greg Ward (based on his Optik package).

- ``ossaudiodev`` - an interface to OSS (Open Sound System), the standard audio API for Linux and some BSD flavors.  Code by Greg Ward, based on the (now deprecated) linuxaudiodev module by Peter Bosch. (New in 2.3a2: because of driver issues, the tests for these modules is not run by default unless &quot;regrtest.py -u audio&quot; is used.)

- ``pickle``, ``cPickle`` and ``copy`` - a new pickling protocol was added for more efficient pickling of (especially) new-style class instances and to allow more pickling flexibility.  (`PEP 307 </dev/peps/pep-0307>`_) (New in 2.3a2.)

- ``random`` - this now uses a new core generator, the Mersenne Twister algorithm.  This is the current best practice random number generator algorithm, widely tested, with a period of 2**19937-1.  Code by Raymond Hettinger.

- ``sets`` - a new module implementing two flexible set data types.  Code by a cast of thousands, including Greg V. Wilson, Alex Martelli, Tim Peters, and Raymond Hettinger.  (`PEP 218 </dev/peps/pep-0218>`_)

- ``socket`` - sockets now support an optional timeout on all operations.  Code by Michael Gilfix and Bernard Yue, based on Tim O'Malley's timeoutsocket.py.  Some bugs in this feature were fixed in 2.3b1; as a result, all platforms now use a Python wrapper class for socket objects.  Also new in 2.3b1, support for inet_pton() and inet_ntop().

- ``ssl`` - the Windows installer now incorporates SSL support. (New in 2.3a2: timeouts set on the underlying socket are now handled correctly.)

- ``Tkinter`` - now returns Tcl objects instead of strings. Support for Tcl/Tk 8.0 and 8.1 is dropped; support for threaded Tcl/Tk is added, as is support for various Tk 8.4 features.  The Windows installer now ships with Tcl/Tk 8.4.3.  In 2.3b1, variable wrappers now also pass objects directly to Tcl, instead of converting them to strings.

- ``trace`` - a tool for tracing program execution and reporting code coverage

- ``textwrap`` - simple but effective text paragraph wrapping, by Greg Ward.

- ``zipimport`` - import modules from zipfiles, implemented in C by Just van Rossum based upon earlier code by James Ahlstrom.  (New in 2.3a2: several serious bugs discovered in 2.3a1 fixed.)

General
-------

- ``PYTHONINSPECT`` - A program can now set the environment variable $PYTHONINSPECT to some string value in Python, and cause the interpreter to enter the interactive prompt at program exit, as if Python had been invoked with the -i option.

- ``os.walk()`` - generator-based replacement for os.path.walk().  (New in 2.3b1.)

- ``os.fsync()`` - now supported on Windows.  (New in 2.3b1.)

- ``winsound.MessageBeep()`` - new function on Windows.  (New in 2.3b1.)

- ``time.tzset()`` - interface to platform tzset().  (New in 2.3b1.)

- ``sys.getfilesystemencoding()`` - returns the file system default encoding.  (New in 2.3b1.)

- ``sys.exc_clear()`` - clears the current exception (sys.exc_type etc.).  (New in 2.3b1.)

- ``sys.call_tracing()`` - allows pdb to debug code recursively. (New in 2.3b1.)

- ``gc.get_referents()`` - returns a list of objects directly referenced by an object.  (New in 2.3b1.)

- ``dict.pop()`` - now takes an optional argument specifying a default value to return if the key is not in the dict.  (New in 2.3b1.)

- ``list.insert(i, x)`` now interprets negative i as it would be interpreted by slicing, so negative values count from the end of the list.  (New in 2.3b1.)  As of 2.3b2, list.index() now accepts optional start and end arguments.

- New-style classes that don't define __new__ or __init__ no longer ignore constructor arguments.  (New in 2.3a2.)

- Hex/oct literals prefixed with a minus sign were handled inconsistently.  This has been fixed in accordance with `PEP 237 </dev/peps/pep-0237>`_.  (New in 2.3a2.)

- Functions now have a __module__ attribute too.  (New in 2.3a2.)

- Passing a float to C functions expecting an integer now issues a DeprecationWarning; in the future this will become a TypeError.  (New in 2.3a2.)

- Package index and metadata for distutils.  This is support for the Python catalog, now open for business at `cheeseshop.python.org/pypi <http://cheeseshop.python.org/pypi>`_.  (`PEP 301 </dev/peps/pep-0301>`_)

- Support for generators is on by default -- 'yield' is always a keyword, 'from __future__ import generators' is no longer necessary (but still allowed).  (`PEP 255 </dev/peps/pep-0255>`_)

- ``Extended slices`` - the standard sequence types (string, list etc.)  now support extended slices.  Cute: s[::-1] reverses a string.

- ``None`` - assignment to variables or attributes named None will now trigger a warning.  In the future, None may become a keyword.

- New-style classes now allow assignment to ``__name__`` and ``__bases__``.

- Interned strings are no longer immortal.

- ``sys.setcheckinterval()`` - the default value for this feature has changed from 10 to 100, for faster execution of interleaving multiple threads (by switching threads less frequently).

- ``Universal newlines`` - files opened for reading with the special mode &quot;U&quot; (instead of &quot;r&quot;) translate all three commonly found line ending conventions (n, r, rn) into Python's standard n convention.  Contributed by Jack Jansen.  (`PEP 278 </dev/peps/pep-0278>`_)

- ``Encoding declarations`` - you can put a comment of the form &quot;# -*- coding: <;encodingname> -*-&quot; in the first or second line of a Python source file to indicate the encoding (e.g. utf-8).  (`PEP 263 </dev/peps/pep-0263>`_ phase 1)

- ``Codec error handling callbacks`` - this allows for flexible handling of encoding errors.  (`PEP 293 </dev/peps/pep-0293>`_)

- File objects are now their own iterators.  This makes multiple interrupted iterations over the same file more reliable.  The xreadlines() method and module are now deprecated.

- The ``in`` operator can now be used for substring testing, e.g. 'ca' in 'abracadabra' returns True.

- ``Import from zipfiles`` - the name of a zipfile placed on sys.path (or in $PYTHONPATH) causes import to look for modules and packages in the zipfile.  Other import hooks are also provided.  Code by Just van Rossum based upon an idea by James Ahlstrom.  (`PEP 273 </dev/peps/pep-0273>`_ and `PEP 302 </dev/peps/pep-0302>`_.)

- Unicode filenames on platforms that support them (specifically, Windows of the NT/2000/XP variety).  (`PEP 277 </dev/peps/pep-0277>`_)

- A new warning, ``FutureWarning``, is issued about certain uses of hex or octal constants that appear unsigned but are in fact negative, left shifts that can lose bits or change the sign, and certain conversions to hex or octal.

- Tim Peters rewrote his ``list.sort()`` implementation - this one is a &quot;stable sort&quot; (equal inputs appear in the same order in the output) and faster than before.

- Tim Peters also changed long int multiplication to use the Karatsuba algorithm, based on a patch by Christopher A. Craig. This speeds up multiplication of very long ints.