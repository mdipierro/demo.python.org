Bugs in Python 2.3.2
~~~~~~~~~~~~~~~~~~~~

- IDLE now executes code in a separate process.  To communicate between the main process and executing processes, IDLE opens a socket to 127.0.0.1 (the local machine).  Some firewalls running on Windows machines interfere with this and can cause either silent failures or erroneous popup windows from the firewall.  This problem only occurs if you run a firewall on the same machine as IDLE.

Build bugs
##########

Some platforms require some tinkering to get a clean build of 
Python. These bugs were all discovered at a point where it was 
too late to fit them into 2.3.2. They should hopefully be fixed
in a 2.3.3 release.

- Some sort of weird dynamic linker error causes dbmmodule to fail     on OSF/1 5.1, at least on the HP test machines.
- It has been reported that untarring the source tarball using     Solaris tar or HP/UX tar can fail.  This is caused by some pathnames      being too long for the tar shipped by the vendor to handle.  Using     `GNU tar <http://www.gnu.org/software/tar/tar.html>`_ should     allow for untarring on Solaris and HP/UX.
- A bug in the /usr/include/ncurses.h header file on FreeBSD and      MacOS X 10.2 means that the cursesmodule will fail to build. Edit the     configure.in file and remove the line        .. code-block::      AC_DEFINE(_XOPEN_SOURCE_EXTENDED, 1, Define to activate Unix95-and-earlier features)       and then run 'autoconf' to rebuild the configure file. This bug is      fixed in OS X 10.3, and will hopefully be fixed in a future release     of FreeBSD. If you don't have autoconf installed, a      `patch <freebsd-curses.patch>`_ is available.
- A bug in SGI's header files means that socketmodule.c might fail     to compile with an error about INET_ADDRSTRLEN. A      `patch <sgi-socketmodule.patch>`_ for this is here.

Test suite bugs
###############

Some tests may unexpectedly fail on certain platforms.  Here are
failures that we know (something) about and intend to fix in a
following patch release.  These bugs may simply be in the test suite,
but they may indicate bugs in Python.

- The test for the ossaudiodev module hangs on some Red Hat     systems.  (This test is only run when regrtest.py is invoked with     -u audio as argument.)

- test_grp and test_pwd may fail.  We've had reports of this on     *nix systems that use a "+" at the beginning of a line in the     /etc/group or /etc/passwd file to indicate NIS/YP or LDAP     consultation.  The bugs may also be related to duplicate id in     these files.  See SourceForge bug reports number     `775964 <http://python.org/sf/775964>`_ and     `779218 <http://python.org/sf/779218>`_.

- There have been some reports on Debian systems about     test_ioctl failures.  We haven't be able to more widely reproduce     this.  See SourceForge bug report number     `777867 <http://python.org/sf/777867>`_

- There have been reports that test_bsddb may fail on some      systems. This appears to be a fault in the test suite - code      using bsddb seems to be fine.
- test_tempfile and test_popen fail on Windows if Python     is installed to a path with a space in the name. This failure     is only in the test suite.
- test_tempfile may fail on HP/UX if your maximum number of     filedescriptors is low (it appears to be 60 by default).
- When running the tests in random order (regrtest.py -r)      test_mimetypes may fail. This is a fault in the test suite,      the library code itself is fine.

To report a bug not listed above, always check the SourceForge `Bug Tracker <http://sourceforge.net/bugs/?group_id=5470>`_ to
see if they've already been reported.  Use the bug tracker to report
new bugs.  If
you have a patch, please use the SourceForge `Patch Manager <http://sourceforge.net/patch/?group_id=5470>`_.
Please mention that you are reporting a bug in 2.3, and note that you
must have a SourceForge account and be logged in to submit a bug
report or patch (we require this in case we need more information from
you).

If you have access to an "unusual" platform, you might want to
consider adding your report to the Wiki page Python
2.3.1 Platform Reports.