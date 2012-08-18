Bugs in Python 2.3
==================

- IDLE now executes code in a separate process.  To communicate between the main process and executing processes, IDLE opens a socket to 127.0.0.1 (the local machine).  Some firewalls running on Windows machines interfere with this and can cause either silent failures or erroneous popup windows from the firewall.  This problem only occurs if you run a firewall on the same machine as IDLE.

- IDLE fails to start on Windows if installed to a directory with a space (e.g. ``C:\Program Files``).  Fix the problem by installing Python in a different directory.  See SF bugs `780451 <http://www.python.org/sf/780451>`_ and `784183 <http://www.python.org/sf/784183>`_.

- The test for the ossaudiodev module hangs on some Red Hat systems.  (This test is only run when regrtest.py is invoked with ``-u audio`` as argument.)

- It has been reported that untarring the source tarball using Solaris tar can fail.  This is caused by some pathnames being too long for Solaris tar to handle.  Using `GNU tar <http://www.gnu.org/software/tar/tar.html>`_ should allow for untarring on Solaris.

- Some tests may unexpectedly fail on certain platforms.  Here are failures that we know (something) about and intend to fix in a following patch release.  These bugs may simply be in the test suite, but they may indicate bugs in Python.

- test_grp and test_pwd may fail.  We've had reports of this on Unix systems that use a &quot;+&quot; at the beginning of a line in the /etc/group or /etc/passwd file to indicate NIS/YP or LDAP consultation.  The bugs may also be related to duplicate id in these files.  See SourceForge bug reports number `775964 <http://python.org/sf/775964>`_ and `779218 <http://python.org/sf/779218>`_.

- ``AssertionError: AEST`` from test_time.  We've had reports of this test failing on RedHat 6.2 and SuSE 7.1 or 7.2 but have not developed a fix for this yet.  See SourceForge bug report number `763153 <http://python.org/sf/763153>`_.

- There have been some reports on Debian systems about test_ioctl failures.  We haven't be able to more widely reproduce this.  See SourceForge bug report number `777867 <http://python.org/sf/777867>`_

To report a bug not listed above, always check the SourceForge `Bug Tracker <http://sourceforge.net/bugs/?group_id=5470>`_ to
see if they've already been reported.  Use the bug tracker to report
new bugs.  If
you have a patch, please use the SourceForge `Patch Manager <http://sourceforge.net/patch/?group_id=5470>`_.
Please mention that you are reporting a bug in 2.3, and note that you
must have a SourceForge account and be logged in to submit a bug
report or patch (we require this in case we need more information from
you).