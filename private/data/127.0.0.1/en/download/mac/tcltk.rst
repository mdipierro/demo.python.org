IDLE and tkinter with Tcl/Tk on Mac OS X
========================================

Important 

Only use IDLE or tkinter from the Python 3.2.3 64-bit/32-bit
installer
on Mac OS X 10.6 if you also have ActiveTcl 8.5 installed.  If you cannot
install ActiveTcl 8.5, use the *3.2.3 32-bit-only installer* instead.

Only use IDLE or Tkinter from the Python 2.7.3 64-bit/32-bit
installer
on Mac OS X 10.6 if you also have ActiveTcl 8.5 installed.  If you cannot
install ActiveTcl 8.5, use the *2.7.3 32-bit-only installer* instead.

Do not use IDLE or Tkinter from the Apple-supplied Python 2.6.1 in
Mac OS X 10.6.  If possible, use one of the *Python 2.7.3 installers* instead;
otherwise, install a newer version of `Python 2.6 <http://python.org/download/releases/2.6.6/>`_.

Read the details below.

Python's integrated development environment,
`IDLE <http://docs.python.org/py3k/library/idle.html>`_, and the
`tkinter GUI toolkit <http://docs.python.org/py3k/library/tkinter.html>`_
it uses, depend on the `Tk GUI toolkit <http://www.tcl.tk/>`_ which is
not part of Python itself.  For best results, it is important that the
proper release of Tcl/Tk is installed on your machine.
For recent Python installers for Mac OS X downloadable from this website,
here is a summary of current recommendations followed by more detailed
information.

**MISSING**
**Python Release**   **Installer Variant**   **Mac OS X Release**   **Recommended Tcl/Tk**   **Alternate Tcl/Tk**   **Not Recommended**
3.2.3   64-/32-bit   10.7   ActiveTcl 8.5.11   Apple 8.5.9

10.6   ActiveTcl 8.5.11      Apple 8.5.7

32-bit   10.6   ActiveTcl 8.4.19   Apple 8.4.19

10.5   ActiveTcl 8.4.19   Apple 8.4.7

10.4   ActiveTcl 8.4.19   Apple 8.4.7

10.3.9   ActiveTcl 8.4.19

2.7.3   64-/32-bit   10.7   ActiveTcl 8.5.11   Apple 8.5.9

10.6   ActiveTcl 8.5.11      Apple 8.5.7

32-bit   10.6   ActiveTcl 8.4.19   Apple 8.4.19

10.5   ActiveTcl 8.4.19   Apple 8.4.7

10.4   ActiveTcl 8.4.19   Apple 8.4.7

10.3.9   ActiveTcl 8.4.19

Tk On Mac OS X
--------------

There are currently three major variants of Tk in common use on Mac OS X: 

**MISSING**

Note 

In this document the terms **Tcl/Tk** and **Tk** are used
interchangeably.  Keep in mind that while Tcl and Tk are
separate frameworks and libraries, they are closely related and are
generally installed or updated simultaneously.  You should not
attempt to mix-and-match Tcl and Tk versions.  References to
a specific version of Tk assume the corresponding version of
Tcl is installed as well

How Python Chooses Which Tk Release To Use
------------------------------------------

The Python for Mac OS X installers downloaded from this website dynamically
link at runtime to Tcl/Tk Mac OS X frameworks.  The Tcl/Tk major version is
determined when the installer is created and cannot be overridden.
As of this writing, the Python 3.2.x 64-bit/32-bit and 2.7.x 64-bit/32-bit
Mac OS X installers dynamically link to Tcl/Tk 8.5 frameworks.
All other Python installers for Mac OS X dynamically link to Tcl/Tk 8.4
frameworks.

In either case, the dynamically linking occurs when tkinter (Python 3)
or Tkinter (Python 2) is first imported (specifically, the internal
_tkinter C extension module).  By default, the Mac OS X dynamic linker
looks first in ``/Library/Frameworks`` for Tcl and Tk frameworks with
the proper major version.  This is the standard location for third-party
or built from source frameworks, including the ActiveTcl releases.
If frameworks of the proper major version are not found there,
the dynamic linker looks for the same version in
``/System/Library/Frameworks``, the location for Apple-supplied
frameworks shipped with Mac OS X.  (Note, you should normally not modify
or delete files in ``/System/Library``.)

Warning 

This search order does not apply to the *Python 2.7.1
Mac OS X 64-bit/32-bit x86-64/i386 installer for Mac OS X 10.6*.  This
installer was built and released before ActiveState Tcl 8.5.9 was
available so this version of Python links only with the Apple 8.5.7
released with Mac OS X 10.6.  As noted below, IDLE is known to hang
or crash when using this combination.  Python 2.7.1 is no longer
current or supported.  Use a newer Python 2.7.x installer instead.
(This warning also applies to the IDLE and Tkinter
in the Apple-supplied Python 2.6.1 shipped with Mac OS X 10.6.)

As is common on Mac OS X, the installed Pythons and the Tcl and Tk
frameworks are built to run on multiple CPU architectures (*universal
binaries*) and across multiple Mac OS X levels (*minimum deployment
target*).  For Python to be able to dynamically link with a particular
Tcl and Tk version, the available architectures in the Tcl/Tk frameworks
must include the architecture that Python is running in and their
minimum deployment target should be no greater than that of Python.
As of this writing, the Python *3.2.x 64-bit/32-bit* and *2.7.x 64-bit/32-bit*
Mac OS X installers are built with Intel-64 (``x86_64``) and Intel-32 (``i386``)
architectures and a minimum deployment target of Mac OS X 10.6.  The
Apple 8.5.9 and ActiveTcl 8.5.11 releases discussed below are compatible
with these installers.  All other current Python installers for Mac OS X
from this web site are built with Intel-32 (``i386``) and PowerPC-32 (``ppc``)
architectures with a minimum deployment target of Mac OS X 10.3.9 and
are compatible with all current releases of Apple 8.4.x and ActiveTcl 8.4.x.

Tcl/Tk Releases
---------------

ActiveTcl 8.5.11
~~~~~~~~~~~~~~~~

ActiveState provides binary distributions of Tcl/Tk which are upward compatible
with and generally more up-to-date than those provided by Apple in Mac OS X
releases.  You can download an installer for this release from
`the ActiveState web site <http://www.activestate.com/activetcl/downloads>`_.
Note that ActiveState Community Edition binaries are not open source and
are covered by an ActiveState license.  You should read the license
before downloading to verify that your usage complies with its terms of use.

Make sure that you are using the most recent release which, as of this writing,
is 8.5.11.1 (released 2012-02-27).  This is an *Aqua Cocoa Tk*.

Apple 8.5.9
~~~~~~~~~~~

This release is included in Mac OS X 10.7.  As of this writing, Mac OS X
10.7.3 is current and there are at least two known issues with Tk 8.5.9 that
are present in Apple 8.5.9 Tk but fixed in the most recent 8.5 release
from ActiveState.  The more serious problem is an immediate crash in Tk
when entering a composition character, like ``Option-u`` on a US keyboard.
(This problem is documented as
`Tk bug 2907388 <http://sourceforge.net/tracker/index.php?func=detail&aid=2907388&group_id=12997&atid=112997>`_.)
Until and if the fix for
this problem is released in an update for Apple 8.5.9 in OS X 10.7, we
recommend using ActiveTcl 8.5.11 where possible.  This is an *Aqua Cocoa Tk*.

Apple 8.5.7
~~~~~~~~~~~

This release is included in Mac OS X 10.6.  As of this writing, Mac OS X
10.6.8 is current and IDLE is known to hang or crash when used with the
Apple 8.5.7 included in all versions of Mac OS X 10.6.x up to now.
We strongly recommend that you do not attempt to use it with Python!
If possible, install ActiveTcl 8.5.11 but see the `warning <#warning>`_ above about
Python 2.7.1 and the Apple-supplied Python 2.6.1.  This is an *Aqua Cocoa Tk*.

ActiveTcl 8.4.19
~~~~~~~~~~~~~~~~

ActiveState provides binary distributions of Tcl/Tk which are upward compatible
with and generally more up-to-date than those provided by Apple in Mac OS X
releases.  You can download an installer for this release from
`the ActiveState web site <http://www.activestate.com/activetcl/downloads>`_.
Note that ActiveState Community Edition binaries are not open source and
are covered by an ActiveState license.  You should read the license
before downloading to verify that your usage complies with its terms of use.
This is an *Aqua Carbon Tk*.

Apple 8.4.19
~~~~~~~~~~~~

This release is included in Mac OS X 10.7 and 10.6.  This is an *Aqua
Carbon Tk*.

Apple 8.4.7
~~~~~~~~~~~

This release is included in Mac OS X 10.5 and 10.4.  This is an *Aqua
Carbon Tk*.

Revision history
----------------

- 2012-04-11 - updated for 3.2.3 final and 2.7.3 final

- 2012-03-18 - updated for 3.2.3rc2 and 2.7.3rc2

- 2012-03-04 - updated for ActiveTcl 8.5.11.1, 3.2.3rc1, 2.7.3rc1, removed 3.1.4

- 2011-11-12 - updated for ActiveTcl 8.5.11

- 2011-09-04 - updated for 3.2.2 final

- 2011-07-21 - updated for OS X 10.7 and ActiveTcl 8.5.10.1

- 2011-07-09 - updated for 3.2.1 final and ActiveTcl 8.5.10

- 2011-06-12 - updated for 2.7.2 final and 3.1.4 final

- 2011-05-30 - updated for 3.2.1rc, 2.7.2rc, and 3.1.4rc

- 2011-03-08 - add warnings and include details on how Python links with Tcl/Tk releases

- 2011-02-20 - updated for 3.2 final

- 2011-01-31 draft 1 - preliminary info for 3.2rc2

- 2011-01-14 draft 0