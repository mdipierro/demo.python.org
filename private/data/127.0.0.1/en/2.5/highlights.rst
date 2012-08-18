Highlights: Python 2.5
----------------------

Here are some of the (subjective) highlights of Python 2.5.  More detail on
almost all of the new features can be found in the document What's New In
Python 2.5

More Reliable
-------------

Python now uses the Buildbot tool for continuous testing on a wide range of
platforms. This allows us to spot problems faster during development, and
resulted in a much more robust release.

Andrew Kuchling determined that there were over 350 patches and over 450 bugs
fixed since Python 2.4.

Faster
------

A number of optimizations came out of the NeedForSpeed sprint in Iceland.
There were major speedups in exception handling and string operations, as
well as a number of other changes to improve performance.

New language features
---------------------

Internally, the Python compiler now converts the source code to an
abstract syntax tree (AST) before producing the bytecode.

The 'with' operator replaces a common try/finally idiom that results in much
cleaner and safer code.

Generators gained send, throw and close methods. Values passed to send
will be returned by the yield statement when the generator is resumed.
throw takes an exception and causes the yield statement to raise the
passed exception in the generator. close is used to terminate a generator.
This turns generators into a form of coroutine and makes them even more
powerful.

Conditional expressions of the form (TrueValue if Condition else FalseValue)
were added.

import can use both relative and absolute imports when inside packages. 

Try/except/finally were changed so that it's now possible to have both except
blocks and a finally block for the same try block.

Exceptions have become new-style classes, and the exception hierarchy has
been rearranged a bit.

Internally, Python was changed to use the Py_ssize_t type - this means that
many structures that were limited to 2^32 objects can now hold up to 2^64
instead.

New or upgraded built-ins
-------------------------

partition and rpartition methods were added to str and unicode. This
greatly simplifies the process of searching and splitting strings.

New builtins any and all evaluate whether an iterator contains any or all
True values, respectively.

min and max gained a key keyword parameter, analogous to sort.

New or upgraded modules and packages
------------------------------------

In keeping with the theme of adding tried and true packages to the standard
library, in 2.5 we've added ctypes, ElementTree, hashlib, sqlite3 and wsgiref
to the standard library that ships with Python.

Google's summer of code resulted in a new cProfile profiling module. This is a
much more efficient version of the venerable profile.py module that's shipped
with Python for many many years. GSoC also gave us a rewritten mailbox module
that can both read and write mailboxes in a variety of formats.

The struct module was updated to support a new Struct object. These are similar
to the re module's compiled form of regular expressions.

Some other smaller modules added to the standard library include uuid, msilib
and spwd.