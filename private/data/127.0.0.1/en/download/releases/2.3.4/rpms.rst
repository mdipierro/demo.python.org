Linux RPMs for Python 2.3.4
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

- **Signature:** - Many of the following packages were signed with the GPG key in `KRUD-GPG-KEY </ftp/python/2.3.4/rpms/KRUD-GPG-KEY>`_
- **Source:** - `python2.3-2.3.4-3pydotorg.src.rpm </ftp/python/2.3.4/rpms/python2.3-2.3.4-3pydotorg.src.rpm>`_ (Fedora Core 1 Source RPM, 9747665 bytes)
- **Binaries for Fedora Core 1 (and similar):** - `python2.3-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-2.3.4-3pydotorg.i386.rpm>`_ (Fedora Core 1 base RPM, 7565683 bytes) - `python2.3-devel-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-devel-2.3.4-3pydotorg.i386.rpm>`_ (Fedora Core 1 development RPM, 678130 bytes) - `python2.3-docs-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-docs-2.3.4-3pydotorg.i386.rpm>`_ (Fedora Core 1 HTML documentation RPM, 1885396 bytes) - `python2.3-tkinter-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-tkinter-2.3.4-3pydotorg.i386.rpm>`_ (Fedora Core 1 Tk GUI RPM, 362227 bytes) - `python2.3-tools-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-tools-2.3.4-3pydotorg.i386.rpm>`_ (Fedora Core 1 tools RPM, 690451 bytes)
- **Binaries for Mandrake 9.2 (and similar, provided by Fabien Wahl):** - `python2.3-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-2.3.4-3pydotorg.i586.rpm>`_ (Mandrake 9.2 base RPM, 6156262 bytes) - `python2.3-devel-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-devel-2.3.4-3pydotorg.i586.rpm>`_ (Mandrake 9.2 development RPM, 2988509 bytes) - `python2.3-docs-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-docs-2.3.4-3pydotorg.i586.rpm>`_ (Mandrake 9.2 HTML documentation RPM, 1861451 bytes) - `python2.3-tkinter-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-tkinter-2.3.4-3pydotorg.i586.rpm>`_ (Mandrake 9.2 Tk GUI RPM, 269812 bytes) - `python2.3-tools-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-tools-2.3.4-3pydotorg.i586.rpm>`_ (Mandrake 9.2 tools RPM, 682970 bytes)

Packages of Python Tools
~~~~~~~~~~~~~~~~~~~~~~~~

Packages of other Python libraries have been made available by symbiont
at `http://python.org/pyvault/ <http://python.org/pyvault/>`_.

Files, `MD5 <../md5sum.py>`_ checksums and sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    **Based on python.org SRPM:**
       **Source:**
          01f9339fc61f222c6d9497b7f1ea10da `python2.3-2.3.4-3pydotorg.src.rpm </ftp/python/2.3.4/rpms/python2.3-2.3.4-3pydotorg.src.rpm>`_ (9747665 bytes)

       **Fedora Core 1 Binaries:**
          21f36fa2d820ab1c7bea6924c9790fd9 `python2.3-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-2.3.4-3pydotorg.i386.rpm>`_ (7565683 bytes)
          77602572f4cc6be79b8ae2aaaad4b156 `python2.3-devel-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-devel-2.3.4-3pydotorg.i386.rpm>`_ (678130 bytes)
          8477cd5f1db9b0e02a09c7d8012745f7 `python2.3-docs-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-docs-2.3.4-3pydotorg.i386.rpm>`_ (1885396 bytes)
          ab078ca6a20e130524de849482cebb39 `python2.3-tkinter-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-tkinter-2.3.4-3pydotorg.i386.rpm>`_ (362227 bytes)
          1e9484b52c282677dd9d349a61a12911 `python2.3-tools-2.3.4-3pydotorg.i386.rpm </ftp/python/2.3.4/rpms/fedora-1/python2.3-tools-2.3.4-3pydotorg.i386.rpm>`_ (690451 bytes)

       **Mandrake 9.2 Binaries (provided by Fabien Wahl):**
          e1b66cf83cdfc3d1984af52c80a1bb4e `python2.3-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-2.3.4-3pydotorg.i586.rpm>`_ (6156262 bytes)
          56bf79939c1ad039ba50ac99ce655fe5 `python2.3-devel-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-devel-2.3.4-3pydotorg.i586.rpm>`_ (2988509 bytes)
          9fd2bd1dae07d3c096d9472af827b47a `python2.3-docs-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-docs-2.3.4-3pydotorg.i586.rpm>`_ (1861451 bytes)
          805d5991e8b1859f4193f63df1b00e9e `python2.3-tkinter-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-tkinter-2.3.4-3pydotorg.i586.rpm>`_ (269812 bytes)
          a580da0acf73037320b9071650502491 `python2.3-tools-2.3.4-3pydotorg.i586.rpm </ftp/python/2.3.4/rpms/mandrake-9.2/python2.3-tools-2.3.4-3pydotorg.i586.rpm>`_ (682970 bytes)

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
- Q) I'm trying to build the RPMS, but I get:   .. code-block::      RPM build errors:         File not found by glob:     /var/tmp/python2.3-2.3.4-root/usr/lib/python2.3/lib-dynload/_tkinter.so*
- A) You need to have the Tk development package installed.  This       package is usually called "tk-devel", and can be obtained from the       same place that you normally find packages for your system.  You may       also need to install the "tcl-devel" package, if your distribution       includes one.
- Q) When I try to build the RPM, I get:   .. code-block::      myhost$ rpmbuild -rebuild python2.3-2.3.4-2pydotorg.src.rpm     rpmbuild: arguments to --root (-r) must begin with a /     myhost$
- A) The option to rpmbuild is not "-rebuild", it's "--rebuild",    with two hyphens (-) instead of one.  The above command runs "rpmbuild"    with the "ebuild" argument to the "-r" option, as the error message    above mentions.  The second hyphen is not optional.  Perhaps you need to    change your web-browser to use a font that makes "-" and "--" more    distinctive?  :-)