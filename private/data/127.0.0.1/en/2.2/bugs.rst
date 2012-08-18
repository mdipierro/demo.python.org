Known bugs in Python 2.2
------------------------

Real bugs
~~~~~~~~~

These are actual bugs, and we will make fixes available as soon as
we have them.  (There may be other bugs that aren't generally worth
knowing about; search the SourceForge bug
tracker; you can also use that to report new bugs you find, of
course.)

- The ftplib module's FTP class was supposed to default to passive mode.  Unfortunately it doesn't.  This means that urllib.urlopen() doesn't work from inside most firewalls.  If you have this problem, delete or comment out line 117, "self.passiveserver = 0", from file ftplib.py.
- The -Qnew option is implemented incompletely: it turns / into true division, but unfortunately not /=.  See `SourceForge bug report #496549 <http://sf.net/tracker/?func=detail&atid=105470&aid=496549&group_id=5470>`_.
- Attempting to pickle the result of time.localtime() causes infinite recursion.  See `SourceForge bug report #496873 <http://sourceforge.net/tracker/?func=detail&atid=105470&aid=496873&group_id=5470>`_.
- In Python 2.1, the StringIO module (though not cStringIO) supported Unicode.  This capability is accidentally not present in Python 2.2.
- A deep copy (using copy.deepcopy()) of a recursive data structure built out of new-style classes would cause infinite recursion.  See  `SourceForge bug report #497426 <http://sourceforge.net/tracker/?func=detail&atid=105470&aid=497426&group_id=5470>`_.
- The Demo/extend subdirectory should not have been shipped; it contains an obsolete example.  To build extensions, you should use distutils, which is documented extensively in the standard `documentation bundle <http://docs.python.org/>`_ ("Distributing Python Modules").

Incompatibilities between Python 2.1[.1] and Python 2.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following visible differences between Python 2.2 and previous
versions are intentional.

- Not everything is listed here; for the full list see the `Misc/NEWS <http://cvs.sourceforge.net/cgi-bin/viewcvs.cgi/~checkout~/python/python/dist/src/Misc/NEWS?rev=1.337.2.4 >`_ file in the distribution.
- Not listed here are various deprecated modules and features that may issue warnings: the warnings shouldn't affect the correct execution of your program, and they can be disabled with a command line option or programmatically; see the documentation for the warnings module.
- Also not listed are new constructs that used to be an error (e.g. "key in dict" is now a valid test where formerly it would always raise an exception).
- The dir() function behaves differently than in Python 2.1 and before.  Generally, dir() returns more information than it used to do in 2.1.  For example, dir([]) also reports the special methods that overload various operators ('__add__', '__getitem__', '__len__', etc.) as well as '__class__'.  For classes (classic as well as new-style), it returns the attributes of the class as well as of the base classes.
- The special attributes __members__ and __methods__ are no longer supported (for most built-in types).  Use the new and improved dir() function instead.
- type("").__name__ == "str" # was "string"
- type(0L).__name__ == "long" # was "long int"
- Overflowing int operations return the corresponding long value rather than raising the OverflowError exception.
- Conversion of long to float now raises OverflowError if the long is too big to represent as a C double.  This used to return an "infinity" value on most platforms.
- The 3-argument builtin pow() no longer allows a third non-None argument if either of the first two arguments is a float, or if both are of integer types and the second argument is negative (in which latter case the arguments are converted to float, so this is really the same restriction).
- An old tokenizer bug allowed floating point literals with an incomplete exponent, such as 1e and 3.1e-.  Such literals now raise SyntaxError.
- Nested scopes are standard in 2.2 (they were enabled per module through "from __future__ import nested_scopes" in 2.1[.1]).  This may change the meaning of code like the following:    .. code-block::      def f(**MISSING**):             def g(x): return **MISSING**(x)             return g    In this example, the use of **MISSING** inside the inner function g() now refers to the argument **MISSING** in the outer function f(); previously (without nested scopes), it would refer to the built-in function **MISSING**.
- Unbound method objects have their im_class field set differently.  In previous versions, the im_class field was set to the class that *defined* the method.  Now it is set to the class that was used to create the method object.  For example:    .. code-block::      class A:             def meth(self): ...         class B(A):             ... # doesn't define meth         class C(A):             def meth(self):                 B.meth(self) # error, C doesn't inherit from B    This code accidentally worked before, even though B is not a base class of C, because B.meth.im_class was set to A, and A is a base class of C!  Presumably long ago the inheritance tree was different and C did inherit from B; when that was changed the upcall wasn't fixed.  C will break when the unrelated class B gets a new definition of meth().  Also, previously, B().meth.im_class would return A; now it returns B (because it's a method bound to an instance of B).
- The C API to the GC module has changed incompatibly. Extensions written to support the 2.1 version of the GC module will still compile, but the GC feature will be disabled.
- The contents of gc.garbage is different; it used to contain all uncollectible cycles; now it contains only objects in uncollectible cycles with a __del__ method.
- The hash order of dict items is different than in previous versions.  (No code should rely on this order, but it's easy to forget this.)
- Assignment to __debug__ raises SyntaxError at compile-time.
- The UTF-16 codec was modified to be more RFC compliant. It will now only remove BOM characters at the start of the string and then only if running in native mode (UTF-16-LE and -BE won't remove a leading BMO character).
- Many error messages are different; in some cases an error condition raises a different exception (most common are cases where TypeError and AttributeError are swapped).

Differences between classic classes and new-style classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following differences between classic and new-style classes may
require attention when you are converting a classic class to a
new-style class.  Since previous versions of Python don't support
new-style classes, these can't be considered to be real bugs, but
since we've tried very hard to make the behavior of new-style classes
backwards compatible, it's important to note these differences.
(There are of course many more differences that become relevant if you
are writing a new-style class from scratch; this list only lists
changes in behavior relevant for the conversion of classic classes.)

- The method resolution order is different; see the `tutorial <../descrintro#mro>`_.
- New-style classes that overload binary operators (__add__ and so on) cannot rely on the __coerce__ method to coerce the arguments; the other argument will be whatever was present originally.  Thus, if x is a new-style class instance defining an __add__ method, x+1 causes a call to x.__add__(1).  The method implementation will have to analyze the other argument's type in order to be able to implement the operation correctly.  If the method implementation decides that it doesn't know how to implement the operation for this particular combination of argument types, it should return the special singleton value NotImplemented.  (This behavior is the same as for classic classes lacking a __coerce__ method; the difference is that the __coerce__ method is ignored by the new-style binary operators.)
- New-style class instances allow assignment to their __class__ attribute only if the C-level structure layout of the old and new class are the same.  This prevents disasters like taking a list and changing its __class__ to make it a dict.
- New-style class objects don't support assignment to their __bases__ attribute.
- (I'm sure there are more differences that are relevant to the conversion of classic classes to new-style classes), but I can't think of then right now.)

To report a bug not listed above, always use the SourceForge `Bug Tracker <http://sourceforge.net/bugs/?group_id=5470>`_.  If
you have a patch, please use the SourceForge `Patch Manager <http://sourceforge.net/patch/?group_id=5470>`_.
Please mention that you are reporting a bug in 2.2!