Bugs in Python 2.4.1
====================

- The Windows installer package required VBScripts. On systems which do not have VBScript available, installer will report an error 2738. On systems which have VBScript available, but in an insufficiently old version, installer will report an error 2262 (and log a DEBUG error 2896). In either case, please install Microsoft Windows Script from `http://msdn.microsoft.com/downloads/list/webdev.asp <http://msdn.microsoft.com/downloads/list/webdev.asp>`_

- The Windows installer will not add correct IDLE and PyDoc entries when the Python target directory contains a space in its name (e.g. C:\Program Files\python24). In this case, manually delete the shortcut, and create new shortcuts with the command     &quot;C:\Program Files\python24\pythonw.exe&quot;      and the command line options      &quot;C:\Program Files\python24\Lib\idlelib\idle.pyw&quot;      and      &quot;C:\Program Files\python24\Tools\scripts\pydocgui.pyw&quot;      This will not be a problem if Python is installed into its default location (i.e. c:\python24).

- IDLE now executes code in a separate process.  To communicate between the main process and executing processes, IDLE opens a socket to 127.0.0.1 (the local machine).  Some firewalls running on Windows machines interfere with this and can cause either silent failures or erroneous popup windows from the firewall.  This problem only occurs if you run a firewall on the same machine as IDLE.

- The test for the ossaudiodev module hangs on some Red Hat systems. (This test is only run when regrtest.py is invoked with ``-u audio`` as argument.)

- It has been reported that untarring the source tarball using Solaris tar can  fail.  This is caused by some pathnames being too long for Solaris tar to  handle.  Using `GNU tar <http://www.gnu.org/software/tar/tar.html>`_ should  allow for untarring on Solaris.

- Some tests may unexpectedly fail on certain platforms.  Here are failures that we know (something) about and intend to fix in a following patch release.  These bugs may simply be in the test suite, but they may indicate bugs in Python.         - test_grp and test_pwd may fail.  We've had reports of this on *nix systems that use a &quot;+&quot; at the beginning of a line in the /etc/group or /etc/passwd file to indicate NIS/YP or LDAP consultation.  The bugs may also be related to duplicate id in these files.  See SourceForge bug reports number `775964 <http://python.org/sf/775964>`_ and `779218 <http://python.org/sf/779218>`_.          - There have been some reports on Debian systems about test_ioctl failures.  We haven't been able to more widely reproduce this. See SourceForge bug report number `777867 <http://python.org/sf/777867>`_

To report a bug not listed above, always check the SourceForge
`Bug Tracker <http://sourceforge.net/bugs/?group_id=5470>`_ to see if
they've already been reported.  Use the bug tracker to report new
bugs.  If you have a patch, please use the SourceForge
`Patch Manager <http://sourceforge.net/patch/?group_id=5470>`_.
Please mention that
you are reporting a bug in 2.4.1, and note that you must have a
SourceForge account and be logged in to submit a bug report or patch
(we require this in case we need more information from you).