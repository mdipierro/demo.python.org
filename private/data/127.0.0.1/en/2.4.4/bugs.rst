Bugs in Python 2.4.4
====================

- In the default installation directory (C:Python24), NTFS permission inheritance gives write access to the Python installation for all users of the system. If untrusted users have access to the system, there are two solutions to the problem: either install to the Program Files folder (where only Power Users get write access to the installation), or edit the access control list to remove the write permission. If write control should only be granted to Administrators, the command:     .. code-block::      cacls.exe <;pythondir> /t /g users:r administrators:f     can be used (notice that you might have to replace the account names with the localized strings). For more information, see `bug #1284316 <http://www.python.org/sf/1284316>`_

- IDLE now executes code in a separate process.  To communicate between the main process and executing processes, IDLE opens a socket to 127.0.0.1 (the local machine).  Some firewalls running on Windows machines interfere with this and can cause either silent failures or erroneous popup windows from the firewall.  This problem only occurs if you run a firewall on the same machine as IDLE.

- The test for the ossaudiodev module hangs on some Red Hat systems. (This test is only run when regrtest.py is invoked with ``-u audio`` as argument.)

- It has been reported that untarring the source tarball using Solaris tar can fail.  This is caused by some pathnames being too long for Solaris tar to handle.  Using `GNU tar <http://www.gnu.org/software/tar/tar.html>`_ should allow for untarring on Solaris.  This has also been reported as a problem with DEC OSF1/Digital Unix/Digital Tru64/Compaq Tru64/HP Tru64. Other platforms may have the same problem - if you get an error about &quot;@LongLink: invalid file type&quot; or similar, you'll need to get GNU tar.

- It has been reported that building Python on AIX requires you to build in 32 bit mode.

- Some tests may unexpectedly fail on certain platforms.  Here are failures that we know (something) about and intend to fix in a following patch release.  These bugs may simply be in the test suite, but they may indicate bugs in Python.         - test_grp and test_pwd may fail.  We've had reports of this on *nix systems that use a &quot;+&quot; at the beginning of a line in the /etc/group or /etc/passwd file to indicate NIS/YP or LDAP consultation.  The bugs may also be related to duplicate id in these files.  See SourceForge bug reports number `775964 <http://python.org/sf/775964>`_ and `779218 <http://python.org/sf/779218>`_.

To report a bug not listed above, always check the `Bug Tracker <http://bugs.python.org/>`_ to see if they've already been reported.  Use the
bug tracker to report new bugs.  If you have a patch, please use the Bug
Tracker, selecting &quot;patch&quot; in the keywords field.
Please mention that you are reporting a bug in 2.4.4 by selecting &quot;Python 2.4&quot;
in the versions field and that you're using 2.4.4 in the description.  Note
that you must have an account for the tracker and be logged in to submit a bug
report or patch; we require this in case we need more information from you.
You can create an account by clicking on &quot;Register&quot; from the tracker.