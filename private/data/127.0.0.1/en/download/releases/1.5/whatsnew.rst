What's new in Python 1.5 and beyond
===================================

If you download the source release, there's a loooong list of
changes since release 1.4 in the file Misc/NEWS.  Below are some
highlights.  (Or go directly to the listings of `what's new in 1.5b1 <#b1>`_, `what's new in 1.5b2 <#b2>`_, and `what's new in 1.5 (final) <#final>`_.)

- For an essay on the (difficult!) subject of metaprogramming, see my essay `Metaprogramming in Python 1.5 </doc/essays/metaclasses/>`_.

- See also the description of some major new features in version 1.5: `Built-in Package Support </doc/essays/packages.html>`_ and `Standard Exception Classes </doc/essays/stdexceptions.html>`_.

From 1.5 to 1.5.1 - Highlights
------------------------------

- The documentation is now unbundled -- download it from the `documentation </doc/>`_ page.

- New python-mode.el (Emacs/Xemacs editing mode).

- Printing of recursive dictionaries and lists no longer causes a core dump.

- A raise statement without arguments re-raises the last exception raised in the current function.

- The import statement is now serialized between different threads.

- The finalization order is much more sensible.

- On Mac and Windows, the case of module file names must match the case as used in the import statement.  (On Unix, this was always true, of course.)

- When you specify the -t option, the tokenizer warns about inconsistent mixing of spaces and tabs.  Two -t options and this causes syntax errors instead.  See also Tools/scripts/tabnanny.py. All library modules are warning-free.

- The freeze tool now supports hierarchical module names.

- New standard modules: threading, getpass, imaplib, poplib, smtplib, Tkdnd (Tkinter drag-and-drop).

- Some modules that were declared obsolete a while ago have been moved out of the standard library path.

From 1.4 To 1.5 - Highlights
----------------------------

- It's much faster (almost twice for the Lib/test/pystone.py benchmark.)

- There is now an assert statement: ``assert <;condition>`` or ``assert <;condition>, <;errormessage>``.  It raises AssertionError if the condition evaluates to false.  The default error message is empty; the source text of the assertion statement is printed as part of the traceback.

- There is now built-in support for importing hierarchical module names (e.g. &quot;import spam.ham.eggs&quot;); ni is declared obsolete.  Note that the built-in package support is somewhat simpler (no __ and __domain__) and differs in one crucial aspect: __init__.py is required, and loaded in the package's namespace instead of as a submodule.  For more information, see `Built-in Package Support </doc/essays/packages.html>`_.

- The new &quot;re&quot; module (Perl style regular expressions) is here.  It is based on Philip Hazel's pcre code; the Python interfaces were put together by Andrew Kuchling.  The regex module is declared obsolete.

- In support of the re module, a new form of string literals is introduced, &quot;raw strings&quot;: e.g. r&quot;n&quot; is equal to &quot;\n&quot;.

- All standard exceptions and most exceptions defined in standard extension modules are now classes.  Use python -X to revert back to string exceptions.  See `Standard Exception Classes </doc/essays/stdexceptions.html>`_ for more info.

- Comparisons can now raise exceptions (previously, exceptions occurring during comparisons were swept under the rug).

- New dictionary methods: .clear(), .copy(), .update(), .get().  The first two are obvious; d1.update(d2) is equivalent to the for loop ``for k in d2.keys(): d1[k] = d2[k]``; and d.get(k) returns d[k] if it exists and None (or the optional second argument) if not.

- There is a new regression test harness, which tests many more modules.  (To run the tests, do &quot;import test.autotest&quot;.)

- The interpreter is much smarter about the initial value for sys.path; you can control it easier using $PYTHONHOME (see the usage message, e.g. try ``python -h``).  In most situations, the interpreter can be installed at an arbitrary location without having to recompile.

- The build process now builds a single library (libpython1.5.a) which contains everything except for the main() entry point.  This makes life much easier for applications that embed Python.

- There is much better support for embedding, including threads, multiple interpreters(!), uninitialization, and access to the global interpreter lock.

- There is a -O option that removes SET_LINENO instructions, assert statements and code prefixed with ``if __debug__: ...``.  (It still only makes a few percent difference, so don't get all worked up about this.)

- The Grand Renaming is completed: all linker-visible symbols defined by Python now have a &quot;Py&quot; or &quot;_Py&quot; prefix, and the same is true for most macros and typedefs.

From 1.5a4 to 1.5b1
-------------------

If you were an alpha tester, here are the most relevant changes since
1.5a4 (of course all known bugs have been fixed, leaks plugged, and
some documentation has been added).  The full list of changes since
1.5a4 is presented at the end of the Misc/NEWS file.

- Package directories now *require* the presence of __init__.py (or .pyc/.pyo as applicable).  Packages can now contain shared library modules.

- New module 'fileinput' to iterate over the lines of a list of files.

- New module 'locale' for localized number formatting and string case sensitivity.

- New module 'xmllib' to parse XML files.

- Some more support for Tk extensions (PIL, TIX, BLT, TOGL).

- Fixed address list parsing in module 'rfc822'.

- More deployment (and only one fix) for the 're' module.

- New Python mode for Emacs.

- OS/2 support.

From 1.5b1 to 1.5b2
-------------------

- Thanks to all who contributed doc strings for library modules!

- The portability problems caused by indented preprocessor commands and C++ style comments should be gone now.

- Lots of improvements to python-mode.el again.

- Changes in pickle.py and cPickle.c: when unpickling an instance of a class that doesn't define the __getinitargs__() method, the __init__() constructor is no longer called.  This makes a much larger group of classes picklable by default, but may occasionally change semantics.  To force calling __init__() on unpickling, define a __getinitargs__() method.  Other changes too, in particular cPickle now handles classes defined in packages correctly.  The same change applies to copying instances with copy.py.

- Locale support in the &quot;re&quot; (Perl regular expressions) module.  Use the flag re.L (or re.LOCALE) to enable locale-specific matching rules for w and b.  The in-line syntax for this flag is (?L).

- The built-in function isinstance(x, y) now also succeeds when y is a type object and type(x) is y.

- repr() and str() of class and instance objects now reflect the package/module in which the class is defined.

- Module &quot;ni&quot; has been removed.  (If you really need it, it's been renamed to &quot;ni1&quot;.  Let me know if this causes any problems for you. Package authors are encouraged to write __init__.py files that support both ni and 1.5 package support, so the same version can be used with Python 1.4 as well as 1.5.)

- The thread module is now automatically included when threads are configured.  (You must remove it from your existing Setup file, since it is now in its own Setup.thread file.)

- New command line option &quot;-x&quot; to skip the first line of the script; handy to make executable scripts on non-Unix platforms.

- In importdl.c, add the RTLD_GLOBAL to the dlopen() flags.  I haven't checked how this affects things, but it should make symbols in one shared library available to the next one.

- The Windows configuration adds a new main program, &quot;pythonw&quot;, and registers a new extension, &quot;.pyw&quot; that invokes this.  This is a standard Python interpreter that does not pop up a console window; handy for pure Tkinter applications.  All output to the original stdout and stderr is lost; reading from the original stdin yields EOF.

From 1.5b2 to 1.5 (final)
-------------------------

- Thanks to all who contributed doc strings or other documentation!

- Many small improvements to the quality of the documentation, both PostScript, HTML and even Emacs info (library manual only).

- New module telnetlib.py.

- New tool versioncheck.

- Two bugs with ftp URLs fixed in urllib.py.

- Fixed infinite recursion when printing __builtins__.

- A bunch of small problems fixed in Tkinter.py.

- Ported zlibmodule.c and bsddbmodule.c to NT.

- Better NT support in tempfile.py.

- Fixed 4294967296==0.

- Latest re and pcre modules (versions of Dec. 22).