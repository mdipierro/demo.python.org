Linux RPMs for Python 2.2.3
===========================

Except where noted, these RPMs are made
available by Sean Reifschneider 
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
download one of the .src.rpmfiles below, and run "rpmbuild --rebuild
python2-2.2.3-1.src.rpm".  Note toward the end of the output, the lines
starting with "Wrote:" indicate where the binary RPMs were written.

The benefit of building binary RPMs in this way is that they are built
using exactly the set of libraries and versions of packages that you have
installed on your system.  Because the SRPMs encompass all the steps
required to build binary RPMs, it is a "fire and forget" process -- the
simplest source build ever.

Download
~~~~~~~~

- **Signature:** - Many of the following packages were signed with the GPG key in `KRUD-GPG-KEY </ftp/python/2.2.3/rpms/KRUD-GPG-KEY>`_
- **Source:** - **The base Python tar-file has a problem that prevents it from being built as an RPM.  Use the following instead:** - `python-2.2.3-26.src.rpm </ftp/python/2.2.3/rpms/python-2.2.3-26.src.rpm>`_ (Red Hat 9 updated Source RPM, 7007263 bytes) - `python2-2.2.3-1.src.rpm </ftp/python/2.2.3/rpms/python2-2.2.3-1.src.rpm>`_ (Python.org Source RPM, 7680544 bytes)
- **Red Hat 9, Red Hat RPM:**   Red Hat 8.x and 9 users probably want to use these.  These RPMs are built from Red Hat's SRPM, not the python.org tar-file.  These RPMs are meant to more closely match the standard Python provided by Red Hat.  - `python-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python-2.2.3-26.i386.rpm>`_ (Red Hat 9 base RPM, 5530686 bytes) - `python-devel-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python-devel-2.2.3-26.i386.rpm>`_ (Red Hat 9 development RPM, 1172632 bytes) - `python-docs-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python-docs-2.2.3-26.i386.rpm>`_ (Documentation in HTML and info formats, 1839344 bytes) - `python-tools-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python-tools-2.2.3-26.i386.rpm>`_ (Red Hat 9 additional Python tools RPM, 38312 bytes) - `tkinter-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/tkinter-2.2.3-26.i386.rpm>`_ (Red Hat 9 Tk GUI library, 352298 bytes)
- These RPMs are built from the python.org .spec file:  - `python2-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-2.2.3-1.i386.rpm>`_ (Red Hat 9 base RPM, 6232077 bytes) - `python2-devel-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-devel-2.2.3-1.i386.rpm>`_ (Red Hat 9 development RPM, 579465 bytes) - `python2-docs-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-docs-2.2.3-1.i386.rpm>`_ (Documentation in HTML and info formats, 1495357 bytes) - `python2-tkinter-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-tkinter-2.2.3-1.i386.rpm>`_ (Red Hat 9 Tk GUI library, 348414 bytes) - `python2-tools-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-tools-2.2.3-1.i386.rpm>`_ (Red Hat 9 additional Python tools RPM, 349117 bytes)

Files, `MD5 <../md5sum.py>`_ checksums and sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    **Red Hat 9 based SRPM, Red Hat 8.x and 9 users should use these:**
       **Source:**
        989b0372573f3fe296ae8fea709da9b7 `python2-2.2.3-26.src.rpm </ftp/python/2.2.3/rpms/python2-2.2.3-26.src.rpm>`_ (7007263 bytes)
       **Red Hat 9 Binaries:**
        31edfca30731a36d67c5d6a9cbacab95 `python-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python-2.2.3-26.i386.rpm>`_ (5530686 bytes)
        10b4c48921d2c05283296431ad14d0f1 `python-devel-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python-devel-2.2.3-26.i386.rpm>`_ (1172632 bytes)
        f81d53d0ccca8e7d6a482df36d879ffc `python-docs-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python-docs-2.2.3-26.i386.rpm>`_ (1839344 bytes)
        240922eb2055acbfe8dcc110e7c0c854 `python-tools-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python-tools-2.2.3-26.i386.rpm>`_ (38312 bytes)
        707fcae449f3acdc70c34a465eacf3b7 `tkinter-2.2.3-26.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/tkinter-2.2.3-26.i386.rpm>`_ (352298 bytes)

      **Based on python.org SRPM:**
       **Source:**
        356b7acd018f1b703d6427b30f070d97 `python2-2.2.3-1.src.rpm </ftp/python/2.2.3/rpms/python2-2.2.3-1.src.rpm>`_ (7680544 bytes)
       **Red Hat 9 Binaries:**
        f3725a1725a1d51bdbcc5bf09edad6f8 `python2-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-2.2.3-1.i386.rpm>`_ (6232077 bytes)
        e7799403d2fbcf3e13cca690bfb96ff1 `python2-devel-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-devel-2.2.3-1.i386.rpm>`_ (579465 bytes)
        710dcb6204ba0273a0413f4bb8823a2d `python2-docs-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-docs-2.2.3-1.i386.rpm>`_ (1495357 bytes)
        2f1ca332c535e1fe2c101f5dc8b9f055 `python2-tkinter-2.2.3-1.i386.rpm </ftp/python/2.2.3/rpms/redhat-9/python2-tkinter-2.2.3-1.i386.rpm>`_ (348414 bytes)
        0274dd2eee7df059b1e4689e650071cf `python2-tools-2.2.3-1.i386.rpm </ftp
    /python/2.2.3/rpms/redhat-9/python2-tools-2.2.3-1.i386.rpm>`_ (349117 bytes)

RPM Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Q) Why I try to run "rpmbuild -ta Python-2.2.3.tgz", I get an       error about unpackaged files.
- A) Yes, there's a problem with the .spec file in the base tar       file.  Use the SRPM that is on this page.
- Q) When running "rpm -ba", "rpm -ta" or "rpm --rebuild" I get       the error "-ba: unknown option" or "--rebuild: unknown option" or       "-ta: unknown option".
- A) With the Red Hat 8.0 release, the building options were removed       from the "rpm" command.  Use the "rpmbuild" command instead       ("rpmbuild --rebuild python2-2.2.3-1.src.rpm").
- Q) I'm getting the "-ba: unknown option" when trying to build RPMs       using distutils "python setup.py bdist_rpm".
- A) As noted above, Red Hat broke the "build" functionality out of       the base "rpm" command with the 8.0 release.  Unfortunately,       they didn't patch their python RPM to account for this, and they       don't appear to be planning to release any errata to fix this.       If you upgrade to the 2.2.2-7 or newer RPMs on this page, distutils       should work.  Note that this seems to be fixed in the Red Hat 9       release (which uses Python 2.2.2 and has a patched distutils).
- Q) When trying to build RPMs, I get "rpmbuild: command not found".
- A) The "rpmbuild" command is part of a separate RPM "rpm-build".       You will need to install this package before you can build RPMs.