Linux RPMs for Python 2.1
=========================

Made available by Sean Reifschneider. 

- Source:  - `python2-2.1-5.src.rpm </ftp/python/2.1/python2-2.1-5.src.rpm>`_ - `expat-1.1-4tummy.src.rpm </ftp/python/2.1/expat-1.1-4tummy.src.rpm>`_  (Needed for building Python SRPM, for systems that don't provide expat-devel)
- Binary for RedHat-7.0-based systems:  - `python2-2.1-5.i386.rpm </ftp/python/2.1/python2-2.1-5.i386.rpm>`_ (RedHat-based 7.0 base RPM) - `python2-tkinter-2.1-5.i386.rpm </ftp/python/2.1/python2-tkinter-2.1-5.i386.rpm>`_ (RedHat-based 7.0 tkinter RPM) - `python2-devel-2.1-5.i386.rpm </ftp/python/2.1/python2-devel-2.1-5.i386.rpm>`_ (RedHat-based 7.0 development RPM) - `python2-tools-2.1-5.i386.rpm </ftp/python/2.1/python2-tools-2.1-5.i386.rpm>`_ (RedHat-based 7.0 Tools RPM, including IDLE)

Sean's change log for 2.1-5:
- Added entry to disable building tkinter.  (Mentioned by Msquared)
- Added gdbm-devel build pre-req.  (Thanks to Pat Callahan)
- Added db1-devel build pre-req.  (Thanks to Pat Callahan)
- Changed expat build pre-req to expat-devel.  (Thanks to Pat Callahan)
- Ugh, can't have spaces in defattr.  (Thanks to Pat Callahan)

Shy of RPMs because of library or other dependancy problems with
most of the RPMs you pick up?  The cure, in my experience is to pick
up an SRPM (Source RPM).  All you need to do to build a binary package
tailored to your system is run

.. code-block::

    rpm --rebuild <;packagename>.src.rpm