Bugs in Python 2.3.5
====================

- IDLE now executes code in a separate process.  To communicate between the main process and executing processes, IDLE opens a socket to 127.0.0.1 (the local machine).  Some firewalls running on Windows machines interfere with this and can cause either silent failures or erroneous popup windows from the firewall.  This problem only occurs if you run a firewall on the same machine as IDLE.

Build bugs
----------

Some platforms require some tinkering to get a clean build of
Python.

- Some sort of weird dynamic linker error causes dbmmodule to fail on OSF/1 5.1, at least on the HP test machines.

- It has been reported that untarring the source tarball using Solaris tar or HP/UX tar can fail. This is caused by some pathnames being too long for the tar shipped by the vendor to handle. Using `GNU tar <http://www.gnu.org/software/tar/tar.html>`_ should allow for untarring on Solaris and HP/UX.

Test suite bugs
---------------

Some tests may unexpectedly fail on certain platforms.  Here are
failures that we know (something) about and intend to fix in a
following patch release.  These bugs may simply be in the test suite,
but they may indicate bugs in Python.

- The test for the ossaudiodev module hangs on some Red Hat systems.  (This test is only run when regrtest.py is invoked with ``-u audio`` as argument.)

- test_grp and test_pwd may fail.  We've had reports of this on Unix systems that use a &quot;+&quot; at the beginning of a line in the     /etc/group or /etc/passwd file to indicate NIS/YP or LDAP     consultation.  The bugs may also be related to duplicate id in     these files.  See SourceForge bug reports number     `775964 <http://python.org/sf/775964>`_ and     `779218 <http://python.org/sf/779218>`_.

- There have been some reports on Debian systems about     test_ioctl failures.  We haven't be able to more widely reproduce     this.  See SourceForge bug report number     `777867 <http://python.org/sf/777867>`_

- There have been reports that test_bsddb may fail on some systems. This appears to be a fault in the test suite - we believe that this is now fixed, but if you still see the problem, please open a bug report on Sourceforge.

- test_tempfile may fail on HP/UX if your maximum number of filedescriptors is low (it appears to be 60 by default).

To report a bug not listed above, always check the SourceForge `Bug Tracker <http://sourceforge.net/bugs/?group_id=5470>`_ to
see if they've already been reported.  Use the bug tracker to report
new bugs.  If
you have a patch, please use the SourceForge `Patch Manager <http://sourceforge.net/patch/?group_id=5470>`_.
Please mention that you are reporting a bug in 2.3, and note that you
must have a SourceForge account and be logged in to submit a bug
report or patch (we require this in case we need more information from
you).

If you have access to an &quot;unusual&quot; platform, you might want to
consider adding your report to the Wiki page
`Python 2.3.3 Platform Reports <http://www.python.org/moin/Python_202_2e3_2e1_20Platform_20Reports>`_.