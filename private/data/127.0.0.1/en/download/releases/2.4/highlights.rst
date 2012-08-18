Highlights: Python 2.4
----------------------

Here are the (subjective) highlights of what's new in Python 2.4.

Faster
------

A number of modules that were added in Python 2.3 (such as sets and
heapq) have been recoded in C. In addition, there's been a number of
other speedups to the interpreter. (See section 8.1, Optimizations, of
the &quot;What's New&quot; document for more).

New language features
---------------------

- **multi-line imports** - when using imports in the form  ``from foo import bar, baz, bing, bang``, you can surround the imported names with brackets, and they can be split across  lines. This is part of PEP 328.

- **Farewell to OverflowWarning** - as documented in PEP 237, Python no longer generates OverflowWarnings.

- **function/method decorators** - function and method decorators, first described in PEP 318, have been added to the language, using  'pie-decorator' syntax. Decorators are on the line before the 'def', and prefixed with an '@' sign. (`PEP 318 </dev/peps/pep-0318>`_)

- **Assigning to None** - the compiler now treats assigning to None as a SyntaxError.

- **Failed import cleanup** - when a module import failed,  versions of Python prior to 2.4a2 would leave a broken module in sys.modules - subsequent attempts to import the failing module  would silently succeed, but use the broken module object. The  import machinery now removes the failing module from sys.modules if the import fails.

- **The -m command line option** - python -m modulename will find a module in the standard library, and invoke it. For example, python -m pdb is equivalent to python /usr/lib/python2.4/pdb.py

New or upgraded built-ins
-------------------------

- **built-in sets** - the sets module, introduced in 2.3,  has now been implemented in C, and the set and frozenset types are available as built-in types (`PEP 218 </dev/peps/pep-0218>`_)

- **unification of integers and long integers** - an operation that would return a number too big for an integer will automatically return a long integer. (`PEP 237 </dev/peps/pep-0237>`_)

- **generator expressions** - generator expressions are similar to a list comprehension, but instead of creating the entire list of results they create a generator that returns the results one by one. This allows for efficient handling of very large lists. (`PEP 289 </dev/peps/pep-0289>`_)

- **reversed()** - a new builtin that takes a sequence and returns an iterator that loops over the elements of the sequence in reverse order (`PEP 322 </dev/peps/pep-0322>`_)

- **new sort() keyword arguments** - sort() now accepts keyword arguments cmp, key and reverse

- **sorted()** - a new builtin sorted() acts like an in-place list.sort() but can be used in expressions, as it returns a copy of the sequence, sorted.

- **string methods** - strings gained an rsplit() method, and  the string methods ljust(), rjust() and center() accept an argument to specify the fill character.

- **eval()** now accepts any form of object that acts as a mapping as its argument for locals, rather than only accepting a dictionary. There's all sorts of new and shiny evil possible thanks to this little change.

New or upgraded modules and packages
------------------------------------

- a new subprocess module for spawning processes in a platform-independent way (see PEP 324)

- **decimal** - a new numeric type that allows for the accurate representation of floating point numbers (avoiding the problems of binary floating point) (`PEP 327 </dev/peps/pep-0327>`_)

- os.urandom() has been added for systems that support a  source of random data (entropy)

- The mpz, rotor and xreadlines modules have been removed.

- The difflib module now includes an HtmlDiff class that creates an HTML table showing a side by side comparison of two versions of a text.

- The socket module gained the socketpair() function, on systems that support it.

- os.path.lexists(), which tests whether the path is a symlink.

- The doctest module has been massively refactored, with many new features added, and many new hooks for customizing behavior.

- Non-blocking SSL sockets work again.

- time.strptime() can now infer the date using %U or %W (week of the year) when the day of the week and year are also specified.

- The optparse module was updated to Optik 1.5a1.

- The new module cookielib supports client-side HTTP cookies. urllib2  gained a new class HTTPCookieProcessor that uses this new module.

- The CJKCodecs collection of East Asian codecs, maintained by Hye-Shik Chang, was integrated into 2.4.

- The email package's Parser was completely rewritten to better handle malformed email messages. It should now never fail to parse a message and  will annotate the parsed message to indicate what problems were found  during the parsing. There is also a new FeedParser that allows messages to be fed into the parser as they are read in.

- The bisect module now has an underlying C implementation for improved performance.

- There is a new collections module for various specialized collection datatypes. Currently it contains just one type, deque, a double-ended queue that supports efficiently adding and removing elements from either end.

- The asyncore module's loop() now has a count parameter that lets you perform a limited number of passes through the polling loop. The default is still to loop forever.

- The curses module now supports the ncurses extension use_default_colors(). On platforms where the terminal supports transparency, this makes it possible to use a transparent background.

- imaplib now supports the IMAP THREAD command

- heapq has two new functions nlargest() and nsmallest() to find the N largest or smallest values in a dataset.

- itertools has a new function groupby() that acts a little like an SQL &quot;GROUP BY&quot; statement. It also gained a function tee() that returns N independent iterators that replicate the iterator passed as an argument.

- A new function basicConfig() was added to the logging package to simplify setup for logging. There is also a new TimedRotatingLogFileHandler which automatically rotates log files at a fixed interval.

- The operator module gained functions attrgetter() and itemgetter()

- The posix module (available as os) has a new function getsid()

- poplib supports POP over SSL

- profile can now profile C extension functions

- random has a new method getrandbits(N) to return a random integer N bits long.

- The re module was extended to allow simple conditional expressions in regular expressions. In addition, the underlying SRE engine is now non-recursive (previously, certain types of regular expression would run into troubles with recursion).

- The weakref module now supports a wider variety of Python objects includes Python functions, class instances, sets, frozensets, deques, arrays, files, sockets and regular expression objects. In addition, the weakref type is now a new-style object which can be subclassed.

- xmlrpclib now supports a multi-call extension for transmitting multiple XML-RPC calls in a single HTTP operation.

- The base64 module now supports Base64, Base32 and Base16 encoding and decoding, and more complete support for RFC 3548.