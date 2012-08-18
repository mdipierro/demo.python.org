Python 2.4 Release Notes
========================

(editors: check NEWS.help for information about editing NEWS using ReST.) 

What's New in Python 2.4 final?
-------------------------------

*Release date: 30-NOV-2004* 

Core and builtins
~~~~~~~~~~~~~~~~~

- Bug 875692: Improve signal handling, especially when using threads, by forcing an early re-execution of PyEval_EvalFrame() &quot;periodic&quot; code when things_to_do is not cleared by Py_MakePendingCalls().

What's New in Python 2.4 (release candidate 1)
----------------------------------------------

*Release date: 18-NOV-2004* 

Core and builtins
~~~~~~~~~~~~~~~~~

- Bug 1061968:  Fixes in 2.4a3 to address thread bug 1010677 reintroduced the years-old thread shutdown race bug 225673.  Numeric history lesson aside, all bugs in all three reports are fixed now.

Library
~~~~~~~

- Bug 1052242: If exceptions are raised by an atexit handler function an attempt is made to execute the remaining handlers.  The last exception raised is re-raised.

- ``doctest``'s new support for adding ``pdb.set_trace()`` calls to doctests was broken in a dramatic but shallow way.  Fixed.

- Bug 1065388:  ``calendar``'s ``day_name``, ``day_abbr``, ``month_name``, and ``month_abbr`` attributes emulate sequences of locale-correct spellings of month and day names.  Because the locale can change at any time, the correct spelling is recomputed whenever one of these is indexed.  In the worst case, the index may be a slice object, so these recomputed every day or month name each time they were indexed.  This is much slower than necessary in the usual case, when the index is just an integer.  In that case, only the single spelling needed is recomputed now; and, when the index is a slice object, only the spellings needed by the slice are recomputed now.

- Patch 1061679: Added ``__all__`` to pickletools.py.

Build
~~~~~

- Bug 1034277 / Patch 1035255: Remove compilation of core against CoreServices and CoreFoundation on OS X.  Involved removing PyMac_GetAppletScriptFile() which has no known users.  Thanks Bob Ippolito.

C API
~~~~~

- The PyRange_New() function is deprecated.

What's New in Python 2.4 beta 2?
--------------------------------

*Release date: 03-NOV-2004* 

License
~~~~~~~

The Python Software Foundation changed the license under which Python
is released, to remove Python version numbers.  There were no other
changes to the license.  So, for example, wherever the license for
Python 2.3 said &quot;Python 2.3&quot;, the new license says &quot;Python&quot;.  The
intent is to make it possible to refer to the PSF license in a more
durable way.  For example, some people say they're confused by that
the Open Source Initiative's entry for the Python Software Foundation
License:

.. code-block::

    http://www.opensource.org/licenses/PythonSoftFoundation.php

says &quot;Python 2.1.1&quot; all over it, wondering whether it applies only
to Python 2.1.1.

The official name of the new license is the Python Software Foundation
License Version 2.

Core and builtins
~~~~~~~~~~~~~~~~~

- Bug #1055820 Cyclic garbage collection was not protecting against that calling a live weakref to a piece of cyclic trash could resurrect an insane mutation of the trash if any Python code ran during gc (via running a dead object's __del__ method, running another callback on a weakref to a dead object, or via any Python code run in any other thread that managed to obtain the GIL while a __del__ or callback was running in the thread doing gc).  The most likely symptom was &quot;impossible&quot; ``AttributeEror`` exceptions, appearing seemingly at random, on weakly referenced objects.  The cure was to clear all weakrefs to unreachable objects before allowing any callbacks to run.

- Bug #1054139 _PyString_Resize() now invalidates its cached hash value.

Extension Modules
~~~~~~~~~~~~~~~~~

- Bug #1048870:  the compiler now generates distinct code objects for functions with identical bodies.  This was producing confusing traceback messages which pointed to the function where the code object was first defined rather than the function being executed.

Library
~~~~~~~

- Patch #1056967 changes the semantics of Template.safe_substitute() so that no ValueError is raised on an 'invalid' match group.  Now the delimiter is returned.

- Bug #1052503 pdb.runcall() was not passing along keyword arguments.

- Bug #902037: XML.sax.saxutils.prepare_input_source() now combines relative paths with a base path before checking os.path.isfile().

- The whichdb module can now be run from the command line.

- Bug #1045381: time.strptime() can now infer the date using %U or %W (week of the year) when the day of the week and year are also specified.

- Bug #1048816: fix bug in Ctrl-K at start of line in curses.textpad.Textbox

- Bug #1017553: fix bug in tarfile.filemode()

- Patch #737473: fix bug that old source code is shown in tracebacks even if the source code is updated and reloaded.

Build
~~~~~

- Patch #1044395: --enable-shared is allowed in FreeBSD also.

What's New in Python 2.4 beta 1?
--------------------------------

*Release date: 15-OCT-2004* 

Core and builtins
~~~~~~~~~~~~~~~~~

- Patch #975056: Restartable signals were not correctly disabled on BSD systems. Consistently use PyOS_setsig() instead of signal().

- The internal portable implementation of thread-local storage (TLS), used by the ``PyGILState_Ensure()``/``PyGILState_Release()`` API, was not thread-correct.  This could lead to a variety of problems, up to and including segfaults.  See bug 1041645 for an example.

- Added a command line option, -m module, which searches sys.path for the module and then runs it.  (Contributed by Nick Coghlan.)

- The bytecode optimizer now folds tuples of constants into a single constant.

- SF bug #513866:  Float/long comparison anomaly.  Prior to 2.4b1, when an integer was compared to a float, the integer was coerced to a float. That could yield spurious overflow errors (if the integer was very large), and to anomalies such as ``long(1e200)+1 == 1e200 == long(1e200)-1``.  Coercion to float is no longer performed, and cases like ``long(1e200)-1 <; 1e200``, ``long(1e200)+1 > 1e200`` and ``(1 <;<; 20000) > 1e200`` are computed correctly now.

Extension modules
~~~~~~~~~~~~~~~~~

- ``collections.deque`` objects didn't play quite right with garbage collection, which could lead to a segfault in a release build, or an assert failure in a debug build.  Also, added overflow checks, better detection of mutation during iteration, and shielded deque comparisons from unusual subclass overrides of the __iter__() method.

Library
~~~~~~~

- Patch 1046644: distutils build_ext grew two new options - --swig for specifying the swig executable to use, and --swig-opts to specify options to pass to swig. --swig-opts=&quot;-c++&quot; is the new way to spell --swig-cpp.

- Patch 983206: distutils now obeys environment variable LDSHARED, if it is set.

- Added Peter Astrand's subprocess.py module.  See PEP 324 for details.

- time.strptime() now properly escapes timezones and all other locale-specific strings for regex-specific symbols.  Was breaking under Japanese Windows when the timezone was specified as &quot;Tokyo (standard time)&quot;. Closes bug #1039270.

- Updates for the email package:- email.Utils.formatdate() grew a 'usegmt' argument for HTTP support.  - All deprecated APIs that in email 2.x issued warnings have been removed: _encoder argument to the MIMEText constructor, Message.add_payload(), Utils.dump_address_pair(), Utils.decode(), Utils.encode()  - New deprecations: Generator.__call__(), Message.get_type(), Message.get_main_type(), Message.get_subtype(), the 'strict' argument to the Parser constructor.  These will be removed in email 3.1.  - Support for Python earlier than 2.3 has been removed (see PEP 291).  - All defect classes have been renamed to end in 'Defect'.  - Some FeedParser fixes; also a MultipartInvariantViolationDefect will be added to messages that claim to be multipart but really aren't.  - Updates to documentation.

- re's findall() and finditer() functions now take an optional flags argument just like the compile(), search(), and match() functions.  Also, documented the previously existing start and stop parameters for the findall() and finditer() methods of regular expression objects.

- rfc822 Messages now support iterating over the headers.

- The (undocumented) tarfile.Tarfile.membernames has been removed; applications should use the getmember function.

- httplib now offers symbolic constants for the HTTP status codes.

- SF bug #1028306:  Trying to compare a ``datetime.date`` to a ``datetime.datetime`` mistakenly compared only the year, month and day. Now it acts like a mixed-type comparison:  ``False`` for ``==``, ``True`` for ``!=``, and raises ``TypeError`` for other comparison operators.  Because datetime is a subclass of date, comparing only the base class (date) members can still be done, if that's desired, by forcing using of the approprate date method; e.g., ``a_date.__eq__(a_datetime)`` is true if and only if the year, month and day members of ``a_date`` and ``a_datetime`` are equal.

- bdist_rpm now supports command line options --force-arch, {pre,post}-install,  {pre,post}-uninstall, and {prep,build,install,clean,verify}-script.

- SF patch #998993: The UTF-8 and the UTF-16 stateful decoders now support decoding incomplete input (when the input stream is temporarily exhausted). ``codecs.StreamReader`` now implements buffering, which enables proper readline support for the UTF-16 decoders. ``codecs.StreamReader.read()`` has a new argument ``chars`` which specifies the number of characters to return. ``codecs.StreamReader.readline()`` and ``codecs.StreamReader.readlines()`` have a new argument ``keepends``. Trailing &quot;n&quot;s will be stripped from the lines if ``keepends`` is false.

- The documentation for doctest is greatly expanded, and now covers all the new public features (of which there are many).

- ``doctest.master`` was put back in, and ``doctest.testmod()`` once again updates it.  This isn't good, because every ``testmod()`` call contributes to bloating the &quot;hidden&quot; state of ``doctest.master``, but some old code apparently relies on it.  For now, all we can do is encourage people to stitch doctests together via doctest's unittest integration features instead.

- httplib now handles ipv6 address/port pairs.

- SF bug #1017864: ConfigParser now correctly handles default keys, processing them with ``ConfigParser.optionxform`` when supplied, consistent with the handling of config file entries and runtime-set options.

- SF bug #997050: Document, test, & check for non-string values in ConfigParser.  Moved the new string-only restriction added in rev. 1.65 to the SafeConfigParser class, leaving existing ConfigParser & RawConfigParser behavior alone, and documented the conditions under which non-string values work.

Build
~~~~~

- Building on darwin now includes /opt/local/include and /opt/local/lib for building extension modules.  This is so as to include software installed as a DarwinPorts port <;`http://darwinports.opendarwin.org/ <http://darwinports.opendarwin.org/>`_>

- pyport.h now defines a Py_IS_NAN macro.  It works as-is when the platform C computes true for ``x != x`` if and only if X is a NaN. Other platforms can override the default definition with a platform- specific spelling in that platform's pyconfig.h.  You can also override pyport.h's default Py_IS_INFINITY definition now.

C API
~~~~~

- SF patch 1044089:  New function ``PyEval_ThreadsInitialized()`` returns non-zero if PyEval_InitThreads() has been called.

- The undocumented and unused extern int ``_PyThread_Started`` was removed.

- The C API calls ``PyInterpreterState_New()`` and ``PyThreadState_New()`` are two of the very few advertised as being safe to call without holding the GIL.  However, this wasn't true in a debug build, as bug 1041645 demonstrated.  In a debug build, Python redirects the ``PyMem`` family of calls to Python's small-object allocator, to get the benefit of its extra debugging capabilities.  But Python's small-object allocator isn't threadsafe, relying on the GIL to avoid the expense of doing its own locking.  ``PyInterpreterState_New()`` and ``PyThreadState_New()`` call the platform ``malloc()`` directly now, regardless of build type.

- PyLong_AsUnsignedLong[Mask] now support int objects as well.

- SF patch #998993: ``PyUnicode_DecodeUTF8Stateful`` and ``PyUnicode_DecodeUTF16Stateful`` have been added, which implement stateful decoding.

Tests
~~~~~

- test__locale ported to unittest

Mac
~~~

- ``plistlib`` now supports non-dict root objects.  There is also a new interface for reading and writing plist files: ``readPlist(pathOrFile)`` and ``writePlist(rootObject, pathOrFile)``

Tools/Demos
~~~~~~~~~~~

- The text file comparison scripts ``ndiff.py`` and ``diff.py`` now read the input files in universal-newline mode.  This spares them from consuming a great deal of time to deduce the useless result that, e.g., a file with Windows line ends and a file with Linux line ends have no lines in common.

What's New in Python 2.4 alpha 3?
---------------------------------

*Release date: 02-SEP-2004* 

Core and builtins
~~~~~~~~~~~~~~~~~

- SF patch #1007189: ``from ... import ...`` statements now allow the name list to be surrounded by parentheses.

- Some speedups for long arithmetic, thanks to Trevor Perrin.  Gradeschool multiplication was sped a little by optimizing the C code.  Gradeschool squaring was sped by about a factor of 2, by exploiting that about half the digit products are duplicates in a square.  Because exponentiation uses squaring often, this also speeds long power.  For example, the time to compute 17**1000000 dropped from about 14 seconds to 9 on my box due to this much.  The cutoff for Karatsuba multiplication was raised, since gradeschool multiplication got quicker, and the cutoff was aggressively small regardless.  The exponentiation algorithm was switched from right-to-left to left-to-right, which is more efficient for small bases.  In addition, if the exponent is large, the algorithm now does 5 bits (instead of 1 bit) at a time.  That cut the time to compute 17**1000000 on my box in half again, down to about 4.5 seconds.

- OverflowWarning is no longer generated.  PEP 237 scheduled this to occur in Python 2.3, but since OverflowWarning was disabled by default, nobody realized it was still being generated.  On the chance that user code is still using them, the Python builtin OverflowWarning, and corresponding C API PyExc_OverflowWarning, will exist until Python 2.5.

- Py_InitializeEx has been added.

- Fix the order of application of decorators.  The proper order is bottom-up; the first decorator listed is the last one called.

- SF patch #1005778.  Fix a seg fault if the list size changed while calling list.index().  This could happen if a rich comparison function modified the list.

- The ``func_name`` (a.k.a. ``__name__``) attribute of user-defined functions is now writable.

- code_new (a.k.a new.code()) now checks its arguments sufficiently carefully that passing them on to PyCode_New() won't trigger calls to Py_FatalError() or PyErr_BadInternalCall().  It is still the case that the returned code object might be entirely insane.

- Subclasses of string can no longer be interned.  The semantics of interning were not clear here -- a subclass could be mutable, for example -- and had bugs.  Explicitly interning a subclass of string via intern() will raise a TypeError.  Internal operations that attempt to intern a string subclass will have no effect.

- Bug 1003935:  xrange() could report bogus OverflowErrors.  Documented what xrange() intends, and repaired tests accordingly.

Extension modules
~~~~~~~~~~~~~~~~~

- difflib now supports HTML side-by-side diff.

- os.urandom has been added for systems that support sources of random data.

- Patch 1012740:  truncate() on a writeable cStringIO now resets the position to the end of the stream.  This is consistent with the original StringIO module and avoids inadvertently resurrecting data that was supposed to have been truncated away.

- Added socket.socketpair().

- Added CurrentByteIndex, CurrentColumnNumber, CurrentLineNumber members to xml.parsers.expat.XMLParser object.

- The mpz, rotor, and xreadlines modules, all deprecated in earlier versions of Python, have now been removed.

Library
~~~~~~~

- Patch #934356: if a module defines __all__, believe that rather than using heuristics for filtering out imported names.

- Patch #941486: added os.path.lexists(), which returns True for broken symlinks, unlike os.path.exists().

- the random module now uses os.urandom() for seeding if it is available. Added a new generator based on os.urandom().

- difflib and diff.py can now generate HTML.

- bdist_rpm now includes version and release in the BuildRoot, and replaces - by ``_`` in version and release.

- distutils build/build_scripts now has an -e option to specify the path to the Python interpreter for installed scripts.

- PEP 292 classes Template and SafeTemplate are added to the string module.

- tarfile now generates GNU tar files by default.

- HTTPResponse has now a getheaders method.

- Patch #1006219: let inspect.getsource handle '@' decorators. Thanks Simon Percivall.

- logging.handlers.SMTPHandler.date_time has been removed; the class now uses email.Utils.formatdate to generate the time stamp.

- A new function tkFont.nametofont was added to return an existing font. The Font class constructor now has an additional exists argument which, if True, requests to return/configure an existing font, rather than creating a new one.

- Updated the decimal package's min() and max() methods to match the latest revision of the General Decimal Arithmetic Specification. Quiet NaNs are ignored and equal values are sorted based on sign and exponent.

- The decimal package's Context.copy() method now returns deep copies.

- Deprecated sys.exitfunc in favor of the atexit module.  The sys.exitfunc attribute will be kept around for backwards compatability and atexit will just become the one preferred way to do it.

- patch #675551: Add get_history_item and replace_history_item functions to the readline module.

- bug #989672: pdb.doc and the help messages for the help_d and help_u methods of the pdb.Pdb class gives have been corrected. d(own) goes to a newer frame, u(p) to an older frame, not the other way around.

- bug #990669: os.path.realpath() will resolve symlinks before normalizing the path, as normalizing the path may alter the meaning of the path if it contains symlinks.

- bug #851123: shutil.copyfile will raise an exception when trying to copy a file onto a link to itself. Thanks Gregory Ball.

- bug #570300: Fix inspect to resolve file locations using os.path.realpath() so as to properly list all functions in a module when the module itself is reached through a symlink.  Thanks Johannes Gijsbers.

- doctest refactoring continued.  See the docs for details.  As part of this effort, some old and little- (never?) used features are now deprecated:  the Tester class, the module is_private() function, and the isprivate argument to testmod().  The Tester class supplied a feeble &quot;by hand&quot; way to combine multiple doctests, if you knew exactly what you were doing.  The newer doctest features for unittest integration already did a better job of that, are stronger now than ever, and the new DocTestRunner class is a saner foundation if you want to do it by hand.  The &quot;private name&quot; filtering gimmick was a mistake from the start, and testmod() changed long ago to ignore it by default.  If you want to filter out tests, the new DocTestFinder class can be used to return a list of all doctests, and you can filter that list by any computable criteria before passing it to a DocTestRunner instance.

- Bug #891637, patch #1005466: fix inspect.getargs() crash on def foo((bar)).

Tools/Demos
~~~~~~~~~~~

- IDLE's shortcut keys for windows are now case insensitive so that Control-V works the same as Control-v.

- pygettext.py: Generate POT-Creation-Date header in ISO format.

Build
~~~~~

- Backward incompatibility:  longintrepr.h now triggers a compile-time error if SHIFT (the number of bits in a Python long &quot;digit&quot;) isn't divisible by 5.  This new requirement allows simple code for the new 5-bits-at-a-time long_pow() implementation.  If necessary, the restriction could be removed (by complicating long_pow(), or by falling back to the 1-bit-at-a-time algorithm), but there are no plans to do so.

- bug #991962: When building with --disable-toolbox-glue on Darwin no attempt to build Mac-specific modules occurs.

- The --with-tsc flag to configure to enable VM profiling with the processor's timestamp counter now works on PPC platforms.

- patch #1006629: Define _XOPEN_SOURCE to 500 on Solaris 8/9 to match GCC's definition and avoid redefinition warnings.

- Detect pthreads support (provided by gnu pth pthread emulation) on GNU/k*BSD systems.

- bug #1005737, #1007249: Fixed several build problems and warnings found on old/legacy C compilers of HP-UX, IRIX and Tru64.

C API
~~~~~

Documentation
~~~~~~~~~~~~~

- patch #1005936, bug #1009373: fix index entries which contain an underscore when viewed with Acrobat.

- bug #990669: os.path.normpath may alter the meaning of a path if it contains symbolic links. This has been documented in a comment since 1992, but is now in the library reference as well.

New platforms
~~~~~~~~~~~~~

- FreeBSD 6 is now supported.

Tests
~~~~~

Windows
~~~~~~~

- Boosted the stack reservation for python.exe and pythonw.exe from the default 1MB to 2MB.  Stack frames under VC 7.1 for 2.4 are enough bigger than under VC 6.0 for 2.3.4 that deeply recursive progams within the default sys.getrecursionlimit() default value of 1000 were able to suffer undetected C stack overflows.  The standard test program test_compiler was one such program.  If a Python process on Windows &quot;just vanishes&quot; without a trace, and without an error message of any kind, but with an exit code of 128, undetected stack overflow may be the problem.

Mac
~~~

What's New in Python 2.4 alpha 2?
---------------------------------

*Release date: 05-AUG-2004* 

Core and builtins
~~~~~~~~~~~~~~~~~

- Patch #980695:  Implements efficient string concatenation for statements of the form s=s+t and s+=t.  This will vary across implementations. Accordingly, the str.join() method is strongly preferred for performance sensitive code.

- PEP-0318, Function Decorators have been added to the language. These are implemented using the Java-style @decorator syntax, like so:     .. code-block::      @staticmethod     def foo(bar):     (The PEP needs to be updated to reflect the current state)

- When importing a module M raises an exception, Python no longer leaves M in sys.modules.  Before 2.4a2 it did, and a subsequent import of M would succeed, picking up a module object from sys.modules reflecting as much of the initialization of M as completed before the exception was raised. Subsequent imports got no indication that M was in a partially- initialized state, and the importers could get into arbitrarily bad trouble as a result (the M they got was in an unintended state, arbitrarily far removed from M's author's intent).  Now subsequent imports of M will continue raising exceptions (but if, for example, the source code for M is edited between import attempts, then perhaps later attempts will succeed, or raise a different exception).     This can break existing code, but in such cases the code was probably working before by accident.  In the Python source, the only case of breakage discovered was in a test accidentally relying on a damaged module remaining in sys.modules.  Cases are also known where tests deliberately provoking import errors remove damaged modules from sys.modules themselves, and such tests will break now if they do an unconditional del sys.modules[M].

- u'%s' % obj will now try obj.__unicode__() first and fallback to obj.__str__() if no __unicode__ method can be found.

- Patch #550732: Add PyArg_VaParseTupleAndKeywords().  Analogous to PyArg_VaParse().  Both are now documented.  Thanks Greg Chapman.

- Allow string and unicode return types from .encode()/.decode() methods on string and unicode objects.  Added unicode.decode() which was missing for no apparent reason.

- An attempt to fix the mess that is Python's behaviour with signal handlers and threads, complicated by readline's behaviour. It's quite possible that there are still bugs here.

- Added C macros Py_CLEAR and Py_VISIT to ease the implementation of types that support garbage collection.

- Compiler now treats None as a constant.

- The type of values returned by __int__, __float__, __long__, __oct__, and __hex__ are now checked.  Returning an invalid type will cause a TypeError to be raised.  This matches the behavior of Jython.

- Implemented bind_textdomain_codeset() in locale module.

- Added a workaround for proper string operations in BSDs.  str.split and str.is* methods can now work correctly with UTF-8 locales.

- Bug #989185: unicode.iswide() and unicode.width() is dropped and the East Asian Width support is moved to unicodedata extension module.

- Patch #941229: The source code encoding in interactive mode now refers sys.stdin.encoding not just ISO-8859-1 anymore.  This allows for non-latin-1 users to write unicode strings directly.

Extension modules
~~~~~~~~~~~~~~~~~

- cpickle now supports the same keyword arguments as pickle.

Library
~~~~~~~

- Added new codecs and aliases for ISO_8859-11, ISO_8859-16 and TIS-620

- Thanks to Edward Loper, doctest has been massively refactored, and many new features were added.  Full docs will appear later.  For now the doctest module comments and new test cases give good coverage. The refactoring provides many hook points for customizing behavior (such as how to report errors, and how to compare expected to actual output).  New features include a <;BLANKLINE> marker for expected output containing blank lines, options to produce unified or context diffs when actual output doesn't match expectations, an option to normalize whitespace before comparing, and an option to use an ellipsis to signify &quot;don't care&quot; regions of output.

- Tkinter now supports the wish -sync and -use options.

- The following methods in time support passing of None: ctime(), gmtime(), and localtime().  If None is provided, the current time is used (the same as when the argument is omitted). [SF bug 658254, patch 663482]

- nntplib does now allow to ignore a .netrc file.

- urllib2 now recognizes Basic authentication even if other authentication schemes are offered.

- Bug #1001053.  wave.open() now accepts unicode filenames.

- gzip.GzipFile has a new fileno() method, to retrieve the handle of the underlying file object (provided it has a fileno() method).  This is needed if you want to use os.fsync() on a GzipFile.

- imaplib has two new methods: deleteacl and myrights.

- nntplib has two new methods: description and descriptions. They use a more RFC-compliant way of getting a newsgroup description.

- Bug #993394.  Fix a possible red herring of KeyError in 'threading' being raised during interpreter shutdown from a registered function with atexit when dummy_threading is being used.

- Bug #857297/Patch #916874.  Fix an error when extracting a hard link from a tarfile.

- Patch #846659.  Fix an error in tarfile.py when using GNU longname/longlink creation.

- The obsolete FCNTL.py has been deleted.  The builtin fcntl module has been available (on platforms that support fcntl) since Python 1.5a3, and all FCNTL.py did is export fcntl's names, after generating a deprecation warning telling you to use fcntl directly.

- Several new unicode codecs are added: big5hkscs, euc_jis_2004, iso2022_jp_2004, shift_jis_2004.

- Bug #788520.  Queue.{get, get_nowait, put, put_nowait} have new implementations, exploiting Conditions (which didn't exist at the time Queue was introduced).  A minor semantic change is that the Full and Empty exceptions raised by non-blocking calls now occur only if the queue truly was full or empty at the instant the queue was checked (of course the Queue may no longer be full or empty by the time a calling thread sees those exceptions, though).  Before, the exceptions could also be raised if it was &quot;merely inconvenient&quot; for the implementation to determine the true state of the Queue (because the Queue was locked by some other method in progress).

- Bugs #979794 and #980117: difflib.get_grouped_opcodes() now handles the case of comparing two empty lists.  This affected both context_diff() and unified_diff(),

- Bug #980938: smtplib now prints debug output to sys.stderr.

- Bug #930024: posixpath.realpath() now handles infinite loops in symlinks by returning the last point in the path that was not part of any loop.  Thanks AM Kuchling.

- Bug #980327: ntpath not handles compressing erroneous slashes between the drive letter and the rest of the path.  Also clearly handles UNC addresses now as well.  Thanks Paul Moore.

- bug #679953: zipfile.py should now work for files over 2 GB.  The packed data for file sizes (compressed and uncompressed) was being stored as signed instead of unsigned.

- decimal.py now only uses signals in the IBM spec.  The other conditions are no longer part of the public API.

- codecs module now has two new generic APIs: encode() and decode() which don't restrict the return types (unlike the unicode and string methods of the same name).

- Non-blocking SSL sockets work again; they were broken in Python 2.3. SF patch 945642.

- doctest unittest integration improvements:      o Improved the unitest test output for doctest-based unit tests    **MISSING**

- The threading module has a new class, local, for creating objects that provide thread-local data.

- Bug #990307: when keep_empty_values is True, cgi.parse_qsl() no longer returns spurious empty fields.

- Implemented bind_textdomain_codeset() in gettext module.

- Introduced in gettext module the l*gettext() family of functions, which return translation strings encoded in the preferred encoding, as informed by locale module's getpreferredencoding().

- optparse module (and tests) upgraded to Optik 1.5a1.  Changes:    - Add expansion of default values in help text: the string &quot;%default&quot; in an option's help string is expanded to str() of that option's default value, or &quot;none&quot; if no default value.  - Bug #955889: option default values that happen to be strings are now processed in the same way as values from the command line; this allows generation of nicer help when using custom types.  Can be disabled with parser.set_process_default_values(False).  - Bug #960515: don't crash when generating help for callback options that specify 'type', but not 'dest' or 'metavar'.  - Feature #815264: change the default help format for short options that take an argument from e.g. &quot;-oARG&quot; to &quot;-o ARG&quot;; add set_short_opt_delimiter() and set_long_opt_delimiter() methods to HelpFormatter to allow (slight) customization of the formatting.  - Patch #736940: internationalize Optik: all built-in user- targeted literal strings are passed through gettext.gettext().  (If you want translations (.po files), they're not included with Python -- you'll find them in the Optik source distribution from `http://optik.sourceforge.net/ <http://optik.sourceforge.net/>`_ .)  - Bug #878453: respect $COLUMNS environment variable for wrapping help output.  - Feature #988122: expand &quot;%prog&quot; in the 'description' passed to OptionParser, just like in the 'usage' and 'version' strings. (This is *not* done in the 'description' passed to OptionGroup.)

C API
~~~~~

- PyImport_ExecCodeModule() and PyImport_ExecCodeModuleEx():  if an error occurs while loading the module, these now delete the module's entry from sys.modules.  All ways of loading modules eventually call one of these, so this is an error-case change in semantics for all ways of loading modules.  In rare cases, a module loader may wish to keep a module object in sys.modules despite that the module's code cannot be executed.  In such cases, the module loader must arrange to reinsert the name and module object in sys.modules. PyImport_ReloadModule() has been changed to reinsert the original module object into sys.modules if the module reload fails, so that its visible semantics have not changed.

- A large pile of datetime field-extraction macros is now documented, thanks to Anthony Tuininga (patch #986010).

Documentation
~~~~~~~~~~~~~

- Improved the tutorial on creating types in C.- point out the importance of reassigning data members before assigning their values  - correct my misconception about return values from visitprocs. Sigh.  - mention the labor saving Py_VISIT and Py_CLEAR macros.

- Major rewrite of the math module docs, to address common confusions.

Tests
~~~~~

- The test data files for the decimal test suite are now installed on platforms that use the Makefile.

- SF patch 995225:  The test file testtar.tar accidentally contained CVS keywords (like $Id: NEWS.txt 7812 2004-11-30 11:53:58Z anthony $), which could cause spurious failures in test_tarfile.py depending on how the test file was checked out.

What's New in Python 2.4 alpha 1?
---------------------------------

*Release date: 08-JUL-2004* 

Core and builtins
~~~~~~~~~~~~~~~~~

- weakref.ref is now the type object also known as weakref.ReferenceType; it can be subclassed like any other new-style class.  There's less per-entry overhead in WeakValueDictionary objects now (one object instead of three).

- Bug #951851: Python crashed when reading import table of certain Windows DLLs.

- Bug #215126.  The locals argument to eval(), execfile(), and exec now accept any mapping type.

- marshal now shares interned strings. This change introduces a new .pyc magic.

- Bug #966623. classes created with type() in an exec(, {}) don't have a __module__, but code in typeobject assumed it would always be there.

- Python no longer relies on the LC_NUMERIC locale setting to be the &quot;C&quot; locale; as a result, it no longer tries to prevent changing the LC_NUMERIC category.

- Bug #952807:  Unpickling pickled instances of subclasses of datetime.date, datetime.datetime and datetime.time could yield insane objects.  Thanks to Jiwon Seo for a fix.

- Bug #845802: Python crashes when __init__.py is a directory.

- Unicode objects received two new methods: iswide() and width(). These query East Asian width information, as specified in Unicode TR11.

- Improved the tuple hashing algorithm to give fewer collisions in common cases.  Fixes bug  #942952.

- Implemented generator expressions (PEP 289).  Coded by Jiwon Seo.

- Enabled the profiling of C extension functions (and builtins) - check new documentation and modified profile and bdb modules for more details

- Set file.name to the object passed to open (instead of a new string)

- Moved tracebackobject into traceback.h and renamed to PyTracebackObject

- Optimized the byte coding for multiple assignments like &quot;a,b=b,a&quot; and &quot;a,b,c=1,2,3&quot;.  Improves their speed by 25% to 30%.

- Limit the nested depth of a tuple for the second argument to isinstance() and issubclass() to the recursion limit of the interpreter. Fixes bug  #858016 .

- Optimized dict iterators, creating separate types for each and having them reveal their length.  Also optimized the methods:  keys(), values(), and items().

- Implemented a newcode opcode, LIST_APPEND, that simplifies the generated bytecode for list comprehensions and further improves their performance (about 35%).

- Implemented rich comparisons for floats, which seems to make comparisons involving NaNs somewhat less surprising when the underlying C compiler actually implements C99 semantics.

- Optimized list.extend() to save memory and no longer create intermediate sequences.  Also, extend() now pre-allocates the needed memory whenever the length of the iterable is known in advance -- this halves the time to extend the list.

- Optimized list resize operations to make fewer calls to the system realloc().  Significantly speeds up list appends, list pops, list comprehensions, and the list contructor (when the input iterable length is not known).

- Changed the internal list over-allocation scheme.  For larger lists, overallocation ranged between 3% and 25%.  Now, it is a constant 12%. For smaller lists (n<;8), overallocation was upto eight elements.  Now, the overallocation is no more than three elements -- this improves space utilization for applications that have large numbers of small lists.

- Most list bodies now get re-used rather than freed.  Speeds up list instantiation and deletion by saving calls to malloc() and free().

- The dict.update() method now accepts all the same argument forms as the dict() constructor.  This now includes item lists and/or keyword arguments.

- Support for arbitrary objects supporting the read-only buffer interface as the co_code field of code objects (something that was only possible to create from C code) has been removed.

- Made omitted callback and None equivalent for weakref.ref() and weakref.proxy(); the None case wasn't handled correctly in all cases.

- Fixed problem where PyWeakref_NewRef() and PyWeakref_NewProxy() assumed that initial existing entries in an object's weakref list would not be removed while allocating a new weakref object.  Since GC could be invoked at that time, however, that assumption was invalid.  In a truly obscure case of GC being triggered during creation for a new weakref object for an referent which already has a weakref without a callback which is only referenced from cyclic trash, a memory error can occur.  This consistently created a segfault in a debug build, but provided less predictable behavior in a release build.

- input() builtin function now respects compiler flags such as __future__ statements.  SF patch 876178.

- Removed PendingDeprecationWarning from apply().  apply() remains deprecated, but the nuisance warning will not be issued.

- At Python shutdown time (Py_Finalize()), 2.3 called cyclic garbage collection twice, both before and after tearing down modules.  The call after tearing down modules has been disabled, because too much of Python has been torn down then for __del__ methods and weakref callbacks to execute sanely.  The most common symptom was a sequence of uninformative messages on stderr when Python shut down, produced by threads trying to raise exceptions, but unable to report the nature of their problems because too much of the sys module had already been destroyed.

- Removed FutureWarnings related to hex/oct literals and conversions and left shifts.  (Thanks to Kalle Svensson for SF patch 849227.) This addresses most of the remaining semantic changes promised by PEP 237, except for repr() of a long, which still shows the trailing 'L'.  The PEP appears to promise warnings for operations that changed semantics compared to Python 2.3, but this is not implemented; we've suffered through enough warnings related to hex/oct literals and I think it's best to be silent now.

- For str and unicode objects, the ljust(), center(), and rjust() methods now accept an optional argument specifying a fill character other than a space.

- When method objects have an attribute that can be satisfied either by the function object or by the method object, the function object's attribute usually wins.  Christian Tismer pointed out that that this is really a mistake, because this only happens for special methods (like __reduce__) where the method object's version is really more appropriate than the function's attribute.  So from now on, all method attributes will have precedence over function attributes with the same name.

- Critical bugfix, for SF bug 839548:  if a weakref with a callback, its callback, and its weakly referenced object, all became part of cyclic garbage during a single run of garbage collection, the order in which they were torn down was unpredictable.  It was possible for the callback to see partially-torn-down objects, leading to immediate segfaults, or, if the callback resurrected garbage objects, to resurrect insane objects that caused segfaults (or other surprises) later.  In one sense this wasn't surprising, because Python's cyclic gc had no knowledge of Python's weakref objects.  It does now.  When weakrefs with callbacks become part of cyclic garbage now, those weakrefs are cleared first.  The callbacks don't trigger then, preventing the problems.  If you need callbacks to trigger, then just as when cyclic gc is not involved, you need to write your code so that weakref objects outlive the objects they weakly reference.

- Critical bugfix, for SF bug 840829:  if cyclic garbage collection happened to occur during a weakref callback for a new-style class instance, subtle memory corruption was the result (in a release build; in a debug build, a segfault occurred reliably very soon after). This has been repaired.

- Compiler flags set in PYTHONSTARTUP are now active in __main__.

- Added two builtin types, set() and frozenset().

- Added a reversed() builtin function that returns a reverse iterator over a sequence.

- Added a sorted() builtin function that returns a new sorted list from any iterable.

- CObjects are now mutable (on the C level) through PyCObject_SetVoidPtr.

- list.sort() now supports three keyword arguments:  cmp, key, and reverse. The key argument can be a function of one argument that extracts a comparison key from the original record:  mylist.sort(key=str.lower). The reverse argument is a boolean value and if True will change the sort order as if the comparison arguments were reversed.  In addition, the documentation has been amended to provide a guarantee that all sorts starting with Py2.3 are guaranteed to be stable (the relative order of records with equal keys is unchanged).

- Added test whether wchar_t is signed or not. A signed wchar_t is not usable as internal unicode type base for Py_UNICODE since the unicode implementation assumes an unsigned type.

- Fixed a bug in the cache of length-one Unicode strings that could lead to a seg fault.  The specific problem occurred when an earlier, non-fatal error left an uninitialized Unicode object in the freelist.

- The % formatting operator now supports '%F' which is equivalent to '%f'.  This has always been documented but never implemented.

- complex(obj) could leak a little memory if obj wasn't a string or number.

- zip() with no arguments now returns an empty list instead of raising a TypeError exception.

- obj.__contains__() now returns True/False instead of 1/0.  SF patch 820195.

- Python no longer tries to be smart about recursive comparisons. When comparing containers with cyclic references to themselves it will now just hit the recursion limit.  See SF patch 825639.

- str and unicode builtin types now have an rsplit() method that is same as split() except that it scans the string from the end working towards the beginning.  See SF feature request 801847.

- Fixed a bug in object.__reduce_ex__ when using protocol 2.  Failure to clear the error when attempts to get the __getstate__ attribute fail caused intermittent errors and odd behavior.

- buffer objects based on other objects no longer cache a pointer to the data and the data length.  Instead, the appropriate tp_as_buffer method is called as necessary.

- fixed: if a file is opened with an explicit buffer size >= 1, repeated close() calls would attempt to free() the buffer already free()ed on the first call.

Extension modules
~~~~~~~~~~~~~~~~~

- Added socket.getservbyport(), and make the second argument in getservbyname() and getservbyport() optional.

- time module code that deals with input POSIX timestamps will now raise ValueError if more than a second is lost in precision when the timestamp is cast to the platform C time_t type.  There's no chance that the platform will do anything sensible with the result in such cases.  This includes ctime(), localtime() and gmtime().  Assorted fromtimestamp() and utcfromtimestamp() methods in the datetime module were also protected.  Closes bugs #919012 and 975996.

- fcntl.ioctl now warns if the mutate flag is not specified.

- nt now properly allows to refer to UNC roots, e.g. in nt.stat().

- the weakref module now supports additional objects:  array.array, sre.pattern_objects, file objects, and sockets.

- operator.isMappingType() and operator.isSequenceType() now give fewer false positives.

- socket.sslerror is now a subclass of socket.error .  Also added socket.error to the socket module's C API.

- Bug #920575: A problem where the _locale module segfaults on nl_langinfo(ERA) caused by GNU libc's illegal NULL return is fixed.

- array objects now support the copy module.  Also, their resizing scheme has been updated to match that used for list objects.  This improves the performance (speed and memory usage) of append() operations. Also, array.array() and array.extend() now accept any iterable argument for repeated appends without needing to create another temporary array.

- cStringIO.writelines() now accepts any iterable argument and writes the lines one at a time rather than joining them and writing once. Made a parallel change to StringIO.writelines().  Saves memory and makes suitable for use with generator expressions.

- time.strftime() now checks that the values in its time tuple argument are within the proper boundaries to prevent possible crashes from the platform's C library implementation of strftime().  Can possibly break code that uses values outside the range that didn't cause problems previously (such as sitting day of year to 0).  Fixes bug #897625.

- The socket module now supports Bluetooth sockets, if the system has <;bluetooth/bluetooth.h>

- Added a collections module containing a new datatype, deque(), offering high-performance, thread-safe, memory friendly appends and pops on either side of the deque.

- Several modules now take advantage of collections.deque() for improved performance:  Queue, mutex, shlex, threading, and pydoc.

- The operator module has two new functions, attrgetter() and itemgetter() which are useful for creating fast data extractor functions for map(), list.sort(), itertools.groupby(), and other functions that expect a function argument.

- socket.SHUT_{RD,WR,RDWR} was added.

- os.getsid was added.

- The pwd module incorrectly advertised its struct type as struct_pwent; this has been renamed to struct_passwd.  (The old name is still supported for backwards compatibility.)

- The xml.parsers.expat module now provides Expat 1.95.7.

- socket.IPPROTO_IPV6 was added.

- readline.clear_history was added.

- select.select() now accepts sequences for its first three arguments.

- cStringIO now supports the f.closed attribute.

- The signal module now exposes SIGRTMIN and SIGRTMAX (if available).

- curses module now supports use_default_colors().  [patch #739124]

- Bug #811028: ncurses.h breakage on FreeBSD/MacOS X

- Bug #814613: INET_ADDRSTRLEN fix needed for all compilers on SGI

- Implemented non-recursive SRE matching scheme (#757624).

- Implemented (?(id/name)yes|no) support in SRE (#572936).

- random.seed() with no arguments or None uses time.time() as a default seed.  Modified to match Py2.2 behavior and use fractional seconds so that successive runs are more likely to produce different sequences.

- random.Random has a new method, getrandbits(k), which returns an int with k random bits.  This method is now an optional part of the API for user defined generators.  Any generator that defines genrandbits() can now use randrange() for ranges with a length >= 2**53.  Formerly, randrange would return only even numbers for ranges that large (see SF bug #812202).  Generators that do not define genrandbits() now issue a warning when randrange() is called with a range that large.

- itertools has a new function, groupby() for aggregating iterables into groups sharing the same key (as determined by a key function). It offers some of functionality of SQL's groupby keyword and of the Unix uniq filter.

- itertools now has a new tee() function which produces two independent iterators from a single iterable.

- itertools.izip() with no arguments now returns an empty iterator instead of raising a TypeError exception.

- Fixed #853061: allow BZ2Compressor.compress() to receive an empty string as parameter.

Library
~~~~~~~

- Bug #981530: Fix UnboundLocalError in shutil.rmtree().  This affects the documented behavior: the function passed to the onerror() handler can now also be os.listdir.

- Bug #754449: threading.Thread objects no longer mask exceptions raised during interpreter shutdown with another exception from attempting to handle the original exception.

- Added decimal.py per PEP 327.

- Bug #981299: rsync is now a recognized protocol in urlparse that uses a &quot;netloc&quot; portion of a URL.

- Bug #919012: shutil.move() will not try to move a directory into itself. Thanks Johannes Gijsbers.

- Bug #934282: pydoc.stripid() is now case-insensitive.  Thanks Robin Becker.

- Bug #823209:  cmath.log() now takes an optional base argument so that its API matches math.log().

- Bug #957381: distutils bdist_rpm no longer fails on recent RPM versions that generate a -debuginfo.rpm

- os.path.devnull has been added for all supported platforms.

- Fixed #877165: distutils now picks the right C++ compiler command on cygwin and mingw32.

- urllib.urlopen().readline() now handles HTTP/0.9 correctly.

- refactored site.py into functions.  Also wrote regression tests for the module.

- The distutils install command now supports the --home option and installation scheme for all platforms.

- asyncore.loop now has a repeat count parameter that defaults to looping forever.

- The distutils sdist command now ignores all .svn directories, in addition to CVS and RCS directories.  .svn directories hold administrative files for the Subversion source control system.

- Added a new module: cookielib.  Automatic cookie handling for HTTP clients.  Also, support for cookielib has been added to urllib2, so urllib2.urlopen() can transparently handle cookies.

- stringprep.py now uses built-in set() instead of sets.Set().

- Bug #876278: Unbounded recursion in modulefinder

- Bug #780300: Swap public and system ID in LexicalHandler.startDTD. Applications relying on the wrong order need to be corrected.

- Bug #926075: Fixed a bug that returns a wrong pattern object for a string or unicode object in sre.compile() when a different type pattern with the same value exists.

- Added countcallers arg to trace.Trace class (--trackcalls command line arg when run from the command prompt).

- Fixed a caching bug in platform.platform() where the argument of 'terse' was not taken into consideration when caching value.

- Added two new command-line arguments for profile (output file and default sort).

- Added global runctx function to profile module

- Add hlist missing entryconfigure and entrycget methods.

- The ptcp154 codec was added for Kazakh character set support.

- Support non-anonymous ftp URLs in urllib2.

- The encodings package will now apply codec name aliases first before starting to try the import of the codec module. This simplifies overriding built-in codecs with external packages, e.g. the included CJK codecs with the JapaneseCodecs package, by adjusting the aliases dictionary in encodings.aliases accordingly.

- base64 now supports RFC 3548 Base16, Base32, and Base64 encoding and decoding standards.

- urllib2 now supports processors.  A processor is a handler that implements an xxx_request or xxx_response method.  These methods are called for all requests.

- distutils compilers now compile source files in the same order as they are passed to the compiler.

- pprint.pprint() and pprint.pformat() now have additional parameters indent, width and depth.

- Patch #750542: pprint now will pretty print subclasses of list, tuple and dict too, as long as they don't overwrite __repr__().

- Bug #848614: distutils' msvccompiler fails to find the MSVC6 compiler because of incomplete registry entries.

- httplib.HTTP.putrequest now offers to omit the implicit Accept-Encoding.

- Patch #841977: modulefinder didn't find extension modules in packages

- imaplib.IMAP4.thread was added.

- Plugged a minor hole in tempfile.mktemp() due to the use of os.path.exists(), switched to using os.lstat() directly if possible.

- bisect.py and heapq.py now have underlying C implementations for better performance.

- heapq.py has two new functions, nsmallest() and nlargest().

- traceback.format_exc has been added (similar to print_exc but it returns a string).

- xmlrpclib.MultiCall has been added.

- poplib.POP3_SSL has been added.

- tmpfile.mkstemp now returns an absolute path even if dir is relative.

- urlparse is RFC 2396 compliant.

- The fieldnames argument to the csv module's DictReader constructor is now optional.  If omitted, the first row of the file will be used as the list of fieldnames.

- encodings.bz2_codec was added for access to bz2 compression using &quot;a long string&quot;.encode('bz2')

- Various improvements to unittest.py, realigned with PyUnit CVS.

- dircache now passes exceptions to the caller, instead of returning empty lists.

- The bsddb module and dbhash module now support the iterator and mapping protocols which make them more substitutable for dictionaries and shelves.

- The csv module's DictReader and DictWriter classes now accept keyword arguments.  This was an omission in the initial implementation.

- The email package handles some RFC 2231 parameters with missing CHARSET fields better.  It also includes a patch to parameter parsing when semicolons appear inside quotes.

- sets.py now runs under Py2.2.  In addition, the argument restrictions for most set methods (but not the operators) have been relaxed to allow any iterable.

- _strptime.py now has a behind-the-scenes caching mechanism for the most recent TimeRE instance used along with the last five unique directive patterns.  The overall module was also made more thread-safe.

- random.cunifvariate() and random.stdgamma() were deprecated in Py2.3 and removed in Py2.4.

- Bug #823328: urllib2.py's HTTP Digest Auth support works again.

- Patch #873597: CJK codecs are imported into rank of default codecs.

Tools/Demos
~~~~~~~~~~~

- A hotshotmain script was added to the Tools/scripts directory that makes it easy to run a script under control of the hotshot profiler.

- The db2pickle and pickle2db scripts can now dump/load gdbm files.

- The file order on the command line of the pickle2db script was reversed. It is now [ picklefile ] dbfile.  This provides better symmetry with db2pickle.  The file arguments to both scripts are now source followed by destination in situations where both files are given.

- The pydoc script will display a link to the module documentation for modules determined to be part of the core distribution.  The documentation base directory defaults to `http://www.python.org/doc/current/lib/ <http://www.python.org/doc/current/lib/>`_ but can be changed by setting the PYTHONDOCS environment variable.

- texcheck.py now detects double word errors.

- md5sum.py mistakenly opened input files in text mode by default, a silent and dangerous change from previous releases.  It once again opens input files in binary mode by default.  The -t and -b flags remain for compatibility with the 2.3 release, but -b is the default now.

- py-electric-colon now works when pending-delete/delete-selection mode is in effect

- py-help-at-point is no longer bound to the F1 key - it's still bound to C-c C-h

- Pynche was fixed to not crash when there is no ~/.pynche file and no -d option was given.

Build
~~~~~

- Bug #978645: Modules/getpath.c now builds properly in --disable-framework build under OS X.

- Profiling using gprof is now available if Python is configured with --enable-profiling.

- Profiling the VM using the Pentium TSC is now possible if Python is configured --with-tsc.

- In order to find libraries, setup.py now also looks in /lib64, for use on AMD64.

- Bug #934635: Fixed a bug where the configure script couldn't detect getaddrinfo() properly if the KAME stack had SCTP support.

- Support for missing ANSI C header files (limits.h, stddef.h, etc) was removed.

- Systems requiring the D4, D6 or D7 variants of pthreads are no longer supported (see PEP 11).

- Universal newline support can no longer be disabled (see PEP 11).

- Support for DGUX, SunOS 4, IRIX 4 and Minix was removed (see PEP 11).

- Support for systems requiring --with-dl-dld or --with-sgi-dl was removed (see PEP 11).

- Tests for sizeof(char) were removed since ANSI C mandates that sizeof(char) must be 1.

C API
~~~~~

- Thanks to Anthony Tuininga, the datetime module now supplies a C API containing type-check macros and constructors.  See new docs in the Python/C API Reference Manual for details.

- Private function _PyTime_DoubleToTimet added, to convert a Python timestamp (C double) to platform time_t with some out-of-bounds checking.  Declared in new header file timefuncs.h.  It would be good to expose some other internal timemodule.c functions there.

- New public functions PyEval_EvaluateFrame and PyGen_New to expose generator objects.

- New public functions Py_IncRef() and Py_DecRef(), exposing the functionality of the Py_XINCREF() and Py_XDECREF macros. Useful for runtime dynamic embedding of Python.  See patch #938302, by Bob Ippolito.

- Added a new macro, PySequence_Fast_ITEMS, which retrieves a fast sequence's underlying array of PyObject pointers.  Useful for high speed looping.

- Created a new method flag, METH_COEXIST, which causes a method to be loaded even if already defined by a slot wrapper.  This allows a __contains__ method, for example, to co-exist with a defined sq_contains slot.  This is helpful because the PyCFunction can take advantage of optimized calls whenever METH_O or METH_NOARGS flags are defined.

- Added a new function, PyDict_Contains(d, k) which is like PySequence_Contains() but is specific to dictionaries and executes about 10% faster.

- Added three new macros: Py_RETURN_NONE, Py_RETURN_TRUE, and Py_RETURN_FALSE. Each return the singleton they mention after Py_INCREF()ing them.

- Added a new function, PyTuple_Pack(n, ...) for constructing tuples from a variable length argument list of Python objects without having to invoke the more complex machinery of Py_BuildValue().  PyTuple_Pack(3, a, b, c) is equivalent to Py_BuildValue(&quot;(OOO)&quot;, a, b, c).

Windows
~~~~~~~

- The _winreg module could segfault when reading very large registry values, due to unchecked alloca() calls (SF bug 851056).  The fix is uses either PyMem_Malloc(n) or PyString_FromStringAndSize(NULL, n), as appropriate, followed by a size check.

- file.truncate() could misbehave if the file was open for update (modes r+, rb+, w+, wb+), and the most recent file operation before the truncate() call was an input operation.  SF bug 801631.