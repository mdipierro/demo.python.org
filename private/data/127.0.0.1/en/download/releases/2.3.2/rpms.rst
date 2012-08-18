Linux RPMs for Python 2.3.2
===========================

Except where noted, these RPMs are made available by Sean Reifschneider 
(`jafo-rpms@tummy.com <mailto:jafo-rpms@tummy.com>`_).

Having Problems?
~~~~~~~~~~~~~~~~

If you are having problems, please see the RPM Frequently
Asked Questions section at the end of this document for possible
solutions.

RPMs For Other Platforms
~~~~~~~~~~~~~~~~~~~~~~~~

For platforms in which binaries aren't available here, you can
easily build binary RPMs directly from the Python SRPM.  Simply
download one of the .src.rpm files below, and run "rpmbuild --rebuild
python-<;version>.src.rpm".  Note toward the end of the output, the
lines starting with "Wrote:" indicate where the binary RPMs were written.

The benefit of building binary RPMs in this way is that they are built
using exactly the set of libraries and versions of packages that you have
installed on your system.  Because the SRPMs encompass all the steps
required to build binary RPMs, it is a "fire and forget" process -- the
simplest source build ever.

Download
~~~~~~~~

- **Signature:** - Many of the following packages were signed with the GPG key in `KRUD-GPG-KEY </ftp/python/2.3.2/rpms/KRUD-GPG-KEY>`_
- **Source:** - `python2.3-2.3.2-1pydotorg.src.rpm </ftp/python/2.3.2/rpms/python2.3-2.3.2-1pydotorg.src.rpm>`_ (Red Hat 9 Source RPM, 9676906 bytes) - `python2.3-2.3.2-2pydotorg.src.rpm </ftp/python/2.3.2/rpms/python2.3-2.3.2-2pydotorg.src.rpm>`_ (Fedora Core 1 Source RPM, 9677319 bytes)
- **Binaries for Fedora Core 1 (and similar):** - `python2.3-debuginfo-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-debuginfo-2.3.2-2pydotorg.i386.rpm>`_ (Fedora Core 1 base RPM, 3460747 bytes) - `python2.3-devel-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-devel-2.3.2-2pydotorg.i386.rpm>`_ (Fedora Core 1 development RPM, 676799 bytes) - `python2.3-docs-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-docs-2.3.2-2pydotorg.i386.rpm>`_ (Fedora Core 1 HTML documentation RPM, 1838448 bytes) - `python2.3-tkinter-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-tkinter-2.3.2-2pydotorg.i386.rpm>`_ (Fedora Core 1 Tk GUI RPM, 268199 bytes) - `python2.3-tools-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-tools-2.3.2-2pydotorg.i386.rpm>`_ (Fedora Core 1 tools RPM, 688521 bytes)
- **Binaries for Red Hat 9 (and similar):** - `python2.3-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-2.3.2-1pydotorg.i386.rpm>`_ (Red Hat 9 base RPM, 7516651 bytes) - `python2.3-devel-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-devel-2.3.2-1pydotorg.i386.rpm>`_ (Red Hat 9 development RPM, 660855 bytes) - `python2.3-docs-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-docs-2.3.2-1pydotorg.i386.rpm>`_ (Red Hat 9 HTML documentation RPM, 1837504 bytes) - `python2.3-tkinter-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-tkinter-2.3.2-1pydotorg.i386.rpm>`_ (Red Hat 9 Tk GUI RPM, 361826 bytes) - `python2.3-tools-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-tools-2.3.2-1pydotorg.i386.rpm>`_ (Red Hat 9 tools RPM, 688462 bytes)

Files, `MD5 <../md5sum.py>`_ checksums and sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    **Based on python.org SRPM:**
       **Source:**
          d485146fded38aa8bc896b6e14b5f29a `python2.3-2.3.2-1pydotorg.src.rpm </ftp/python/2.3.2/rpms/python2.3-2.3.2-1pydotorg.src.rpm>`_ (9676906 bytes)
    a8c0c8c3cfff5f6ac262aee35d2dd508 `python2.3-2.3.2-2pydotorg.src.rpm </ftp/python/2.3.2/rpms/python2.3-2.3.2-2pydotorg.src.rpm>`_ (9677319 bytes)

       **Red Hat 9 Binaries:**
          23d1a25d1288eb4a338fdab45c1e68c0 `python2.3-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-2.3.2-1pydotorg.i386.rpm>`_ (7516651 bytes)
          3de12bcc6b77a6071e6250f7a6e202dd `python2.3-devel-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-devel-2.3.2-1pydotorg.i386.rpm>`_ (660855 bytes)
          f5eb6e0fd73fa944aa99852c3d7a75fc `python2.3-docs-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-docs-2.3.2-1pydotorg.i386.rpm>`_ (1837504 bytes)
          3467cb56d66ec15c092ec0059a3eaf57 `python2.3-tkinter-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-tkinter-2.3.2-1pydotorg.i386.rpm>`_ (361826 bytes)
          1b30be9323cda75ea53289a55faaec48 `python2.3-tools-2.3.2-1pydotorg.i386.rpm </ftp/python/2.3.2/rpms/redhat-9/python2.3-tools-2.3.2-1pydotorg.i386.rpm>`_ (688462 bytes)

       **Fedora Core 1 Binaries:**
          916ffe1fa03e57c3b9edf5dcf27f5884 `python2.3-debuginfo-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-debuginfo-2.3.2-2pydotorg.i386.rpm>`_ (3460747 bytes)
          58cdbd538b3eaac9998989d28f5ebf14 `python2.3-devel-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-devel-2.3.2-2pydotorg.i386.rpm>`_ (676799 bytes)
          01e15c260a6c8925e0d24f28a679e5c7 `python2.3-docs-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-docs-2.3.2-2pydotorg.i386.rpm>`_ (1838448 bytes)
          10a69b430725c4838e1b84563f94941f `python2.3-tkinter-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-tkinter-2.3.2-2pydotorg.i386.rpm>`_ (268199 bytes)
          bc7963cecc75f41e9603705fb05f6151 `python2.3-tools-2.3.2-2pydotorg.i386.rpm </ftp/python/2.3.2/rpms/fedora-1/python2.3-tools-2.3.2-2pydotorg.i386.rpm>`_ (688521 bytes)

RPM Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Q) When running "rpm -ba", "rpm -ta" or "rpm --rebuild" I get       the error "-ba: unknown option" or "--rebuild: unknown option" or       "-ta: unknown option".
- A) With the Red Hat 8.0 release, the building options were removed       from the "rpm" command.  Use the "rpmbuild" command instead       ("rpmbuild --rebuild python2.3-2.3-1pydotorg.src.rpm").
- Q) I'm getting the "-ba: unknown option" when trying to build RPMs       using distutils "python setup.py bdist_rpm".
- A) As noted above, Red Hat broke the "build" functionality out of       the base "rpm" command with the 8.0 release.  Unfortunately,       they didn't patch their python RPM to account for this, and they       don't appear to be planning to release any errata to fix this.       If you upgrade to the 2.2.2-7 or newer RPMs on this page, distutils       should work.  Note that this seems to be fixed in the Red Hat 9       release (which uses Python 2.2.2 and has a patched distutils).
- Q) When trying to build RPMs, I get "rpmbuild: command not found".
- A) The "rpmbuild" command is part of a separate RPM named "rpm-build".       You will need to install this package before you can build RPMs.
- Q) Is it safe to install these RPMs on a Red Hat system?  Will       they over-write the system python and cause problems with other Red Hat       applications that expect a different version of Python?
- A) The RPMs that start with "python2.3" are built to not interfere       with the system Python.  They install as "/usr/bin/python2.3" and will       not conflict with the system Python unless you are running on a system       that ships the a version of Python which has the same major/minor       number.         To invoke the interpreter with these packages, you will explicitly       have to run "python2.3".  Note that all Python RPMs provided by       Python.org and Red Hat provide a "/usr/bin/python2.3" (or similar,       with major/minor number), even if they also provide       "/usr/bin/python".  So, yes, it should be safe.    Note that you may need to build and install a second copy of any       packages which you need access to with the supplemental version of       Python.  You can build packages of these files for the Python 2.3       interpreters for packages which use Distutils, by using the command       "python2.3 setup.py bdist_rpm".
- Q) How do I build a version of these RPMs which will install as       "/usr/bin/python".
- A) First of all, realize that you are likely to break many Red Hat       provided programs which rely on having a version of Python with the       same major/minor version as that which was shipped.  Also, any       additional packages which were installed will not be available for       the new version, you will probably have to rebuild the packages from       source or Source RPM.         You can tweek several settings in the built RPMs by modifying the       SPEC file that builds the RPMs.  To do this, download the .src.rpm       release and install it as you normally would an RPM package.  This       will install the source and the build control file ("SPEC" file).       The .spec file is probably installed in "/usr/src/redhat/SPECS".    Edit the .spec file and change the "config_binsuffix" line to "none".       Build new RPMs with "rpmbuild -ba python.spec" (where "python.spec"       is the name of the .spec file you edited).  At the end of this       process, you should be presented with several lines saying "Wrote".       These lines specify where the binary RPMs were saved.  You can then       install these packages.