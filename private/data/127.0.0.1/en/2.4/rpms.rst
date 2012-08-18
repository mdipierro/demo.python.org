Linux RPMs for Python 2.4
=========================

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

- **Signature:** - Many of the following packages were signed with the GPG key in `KRUD-GPG-KEY </ftp/python/2.4/rpms/KRUD-GPG-KEY>`_
- **Yum:** - A yum repository is available for your convenience.  For Fedora Core       3, create "/etc/yum.repos.d/python24.repo" with the following lines:    .. code-block::      [python24]     name=Fedora Core $releasever - $basearch - Python 2.4     baseurl=http://www.python.org/ftp/python/2.4/rpms/fedora-$releasever/     enabled=1     gpgcheck=1 - Add the `KRUD <http://www.tummy.com/Products/krud/>`_ GPG    key by running: "rpm --import http://www.python.org/ftp/python/2.4/rpms/KRUD-GPG-KEY" - Install Python 2.4 by running: "yum install python2.4".  Note that    this will only install the base RPM, list "python2.4-devel" or other    packages to install them as well.
- **Source:** - `python2.4-2.4-1pydotorg.src.rpm </ftp/python/2.4/rpms/python2.4-2.4-1pydotorg.src.rpm>`_ (Fedora Core 3 Source RPM, 7839258 bytes)
- **Binaries for Fedora Core 3 (and similar):** - `python2.4-2.4-1pydotorg.i386.rpm </ftp/python/2.4/rpms/fedora-3/python2.4-2.4-1pydotorg.i386.rpm>`_ (Fedora Core 3 base RPM, 8064671 bytes) - `python2.4-devel-2.4-1pydotorg.i386.rpm </ftp/python/2.4/rpms/fedora-3/python2.4-devel-2.4-1pydotorg.i386.rpm>`_ (Fedora Core 3 development RPM, 711722 bytes) - `python2.4-tkinter-2.4-1pydotorg.i386.rpm </ftp/python/2.4/rpms/fedora-3/python2.4-tkinter-2.4-1pydotorg.i386.rpm>`_ (Fedora Core 3 Tk GUI RPM, 285655 bytes) - `python2.4-tools-2.4-1pydotorg.i386.rpm </ftp/python/2.4/rpms/fedora-3/python2.4-tools-2.4-1pydotorg.i386.rpm>`_ (Fedora Core 3 tools RPM, 753428 bytes)
- **Binaries for Mandrake 9.2 (and similar, provided by Fabien Wahl):** - `python2.4-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-2.4-1pydotorg.i586.rpm>`_ (Fedora Core 3 base RPM, 7359837 bytes) - `python2.4-devel-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-devel-2.4-1pydotorg.i586.rpm>`_ (Fedora Core 3 development RPM, 3184990 bytes) - `python2.4-docs-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-docs-2.4-1pydotorg.i586.rpm>`_ (Fedora Core 3 HTML documentation RPM, 2076688 bytes) - `python2.4-tkinter-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-tkinter-2.4-1pydotorg.i586.rpm>`_ (Fedora Core 3 Tk GUI RPM, 263661 bytes) - `python2.4-tools-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-tools-2.4-1pydotorg.i586.rpm>`_ (Fedora Core 3 tools RPM, 746145 bytes)

Packages of Python Tools
~~~~~~~~~~~~~~~~~~~~~~~~

Packages of other Python libraries have been made available by symbiont
at `http://python.org/pyvault/ <http://python.org/pyvault/>`_.

Files, `MD5 <../md5sum.py>`_ checksums and sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    **Based on python.org SRPM:**
       **Source:**
          e2d04732c850ed291ab4d57cd9a029de `python2.4-2.4-1pydotorg.src.rpm </ftp/python/2.4/rpms/python2.4-2.4-1pydotorg.src.rpm>`_ (7839258 bytes)

       **Fedora Core 3 Binaries:**
          eb548833ba525bd4f8c296759f8894c8 `python2.4-2.4-1pydotorg.i386.rpm </ftp/python/2.4/rpms/fedora-3/python2.4-2.4-1pydotorg.i386.rpm>`_ (8064671 bytes)
          89df0a54426cbd856aa2836f327c977f `python2.4-devel-2.4-1pydotorg.i386.rpm </ftp/python/2.4/rpms/fedora-3/python2.4-devel-2.4-1pydotorg.i386.rpm>`_ (711722 bytes)
          c59c0703d6fe32934a6d57e637c3f05c `python2.4-tkinter-2.4-1pydotorg.i386.rpm </ftp/python/2.4/rpms/fedora-3/python2.4-tkinter-2.4-1pydotorg.i386.rpm>`_ (285655 bytes)
          f5935c47afde4bd37512032f5168920e `python2.4-tools-2.4-1pydotorg.i386.rpm </ftp/python/2.4/rpms/fedora-3/python2.4-tools-2.4-1pydotorg.i386.rpm>`_ (753428 bytes)

       **Mandrake 9.2 Binaries (provided by Fabien Wahl):**
          3bb053a3d166b9377ad7c2e1094ed61f `python2.4-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-2.4-1pydotorg.i586.rpm>`_ (7359837 bytes)
          9b96bcd70f9c922879af85834507977c `python2.4-devel-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-devel-2.4-1pydotorg.i586.rpm>`_ (3184990 bytes)
          0d36672858c93703612ff2fb06b2ebea `python2.4-docs-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-docs-2.4-1pydotorg.i586.rpm>`_ (2076688 bytes)
          90f2cc1137b23c033c3d56266c042edb `python2.4-tkinter-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-tkinter-2.4-1pydotorg.i586.rpm>`_ (263661 bytes)
          32beacdc724ff2480156823876c4e223 `python2.4-tools-2.4-1pydotorg.i586.rpm </ftp/python/2.4/rpms/mandrake-9.2/python2.4-tools-2.4-1pydotorg.i586.rpm>`_ (746145 bytes)

RPM Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Q) When running "rpm -ba", "rpm -ta" or "rpm --rebuild" I get       the error "-ba: unknown option" or "--rebuild: unknown option" or       "-ta: unknown option".
- A) With the Red Hat 8.0 release, the building options were removed       from the "rpm" command.  Use the "rpmbuild" command instead       ("rpmbuild --rebuild python2.4-2.4b1-1pydotorg.src.rpm").
- Q) I'm getting the "-ba: unknown option" when trying to build RPMs       using distutils "python setup.py bdist_rpm".
- A) As noted above, Red Hat broke the "build" functionality out of       the base "rpm" command with the 8.0 release.  Unfortunately,       they didn't patch their python RPM to account for this, and they       don't appear to be planning to release any errata to fix this.       If you upgrade to the 2.2.2-7 or newer RPMs on this page, distutils       should work.  Note that this seems to be fixed in the Red Hat 9       release (which uses Python 2.2.2 and has a patched distutils).
- Q) When trying to build RPMs, I get "rpmbuild: command not found".
- A) The "rpmbuild" command is part of a separate RPM named "rpm-build".       You will need to install this package before you can build RPMs.
- Q) Is it safe to install these RPMs on a Red Hat system?  Will       they over-write the system python and cause problems with other Red Hat       applications that expect a different version of Python?
- A) The RPMs that start with "python2.4" are built to not interfere       with the system Python.  They install as "/usr/bin/python2.4" and will       not conflict with the system Python unless you are running on a system       that ships the a version of Python which has the same major/minor       number.         To invoke the interpreter with these packages, you will explicitly       have to run "python2.4".  Note that all Python RPMs provided by       Python.org and Red Hat provide a "/usr/bin/python2.4" (or similar,       with major/minor number), even if they also provide       "/usr/bin/python".  So, yes, it should be safe.    Note that you may need to build and install a second copy of any       packages which you need access to with the supplemental version of       Python.  You can build packages of these files for the Python 2.4       interpreters for packages which use Distutils, by using the command       "python2.4 setup.py bdist_rpm".
- Q) How do I build a version of these RPMs which will install as       "/usr/bin/python".
- A) First of all, realize that you are likely to break many Red Hat       provided programs which rely on having a version of Python with the       same major/minor version as that which was shipped.  Also, any       additional packages which were installed will not be available for       the new version, you will probably have to rebuild the packages from       source or Source RPM.         You can tweek several settings in the built RPMs by modifying the       SPEC file that builds the RPMs.  To do this, download the .src.rpm       release and install it as you normally would an RPM package.  This       will install the source and the build control file ("SPEC" file).       The .spec file is probably installed in "/usr/src/redhat/SPECS".    Edit the .spec file and change the "config_binsuffix" line to "none".       Build new RPMs with "rpmbuild -ba python.spec" (where "python.spec"       is the name of the .spec file you edited).  At the end of this       process, you should be presented with several lines saying "Wrote".       These lines specify where the binary RPMs were saved.  You can then       install these packages.
- Q) I'm trying to build the RPMS, but I get:   .. code-block::      RPM build errors:         File not found by glob:     /var/tmp/python2.4-2.4-root/usr/lib/python2.4/lib-dynload/_tkinter.so*
- A) You need to have the Tk development package installed.  This       package is usually called "tk-devel", and can be obtained from the       same place that you normally find packages for your system.  You may       also need to install the "tcl-devel" package, if your distribution       includes one.
- Q) When I try to build the RPM, I get:   .. code-block::      myhost$ rpmbuild -rebuild python2.4-2.4-2pydotorg.src.rpm     rpmbuild: arguments to --root (-r) must begin with a /     myhost$
- A) The option to rpmbuild is not "-rebuild", it's "--rebuild",    with two hyphens (-) instead of one.  The above command runs "rpmbuild"    with the "ebuild" argument to the "-r" option, as the error message    above mentions.  The second hyphen is not optional.  Perhaps you need to    change your web-browser to use a font that makes "-" and "--" more    distinctive?  :-)