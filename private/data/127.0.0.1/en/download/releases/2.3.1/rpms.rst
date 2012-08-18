Linux RPMs for Python 2.3.1
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

- **Signature:** - Many of the following packages were signed with the GPG key in `KRUD-GPG-KEY </ftp/python/2.3.1/rpms/KRUD-GPG-KEY>`_
- **Source:** - `python2.3-2.3.1-1pydotorg.src.rpm </ftp/python/2.3.1/rpms/python2.3-2.3.1-1pydotorg.src.rpm>`_ (Red Hat 9 Source RPM, 9702241 bytes)
- **Binaries for Red Hat 9 (and similar):** - `python2.3-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-2.3.1-1pydotorg.i386.rpm>`_ (Red Hat 9 base RPM, 7514331 bytes) - `python2.3-devel-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-devel-2.3.1-1pydotorg.i386.rpm>`_ (Red Hat 9 development RPM, 660541 bytes) - `python2.3-docs-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-docs-2.3.1-1pydotorg.i386.rpm>`_ (Red Hat 9 HTML documentation RPM, 1886131 bytes) - `python2.3-tkinter-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-tkinter-2.3.1-1pydotorg.i386.rpm>`_ (Red Hat 9 Tk GUI RPM, 361734 bytes) - `python2.3-tools-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-tools-2.3.1-1pydotorg.i386.rpm>`_ (Red Hat 9 tools RPM, 688223 bytes)

Files, `MD5 <../md5sum.py>`_ checksums and sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    **Based on python.org SRPM:**
       **Source:**
          bec106e3d15f393cdf8f26dafa794323 `python2.3-2.3.1-1pydotorg.src.rpm </ftp/python/2.3.1/rpms/python2.3-2.3.1-1pydotorg.src.rpm>`_ (9702241 bytes)

       **Red Hat 9 Binaries:**

          ff67b4c5c292d84bec258b6092f5108a `python2.3-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-2.3.1-1pydotorg.i386.rpm>`_ (7514331 bytes)
          11514e6298b9d20a4972560fd2ac3d2d `python2.3-devel-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-devel-2.3.1-1pydotorg.i386.rpm>`_ (660541 bytes)
          5eab46b88f5f926fbd6cb930a89aa5e1 `python2.3-docs-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-docs-2.3.1-1pydotorg.i386.rpm>`_ (1886131 bytes)
          76bbd97abd3bd1ef648113a9c6c65eff `python2.3-tkinter-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-tkinter-2.3.1-1pydotorg.i386.rpm>`_ (361734 bytes)
          2eb4c525118194a2a4ce7c1ab9e14409 `python2.3-tools-2.3.1-1pydotorg.i386.rpm </ftp/python/2.3.1/rpms/redhat-9/python2.3-tools-2.3.1-1pydotorg.i386.rpm>`_ (688223 bytes)

RPM Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Q) When running "rpm -ba", "rpm -ta" or "rpm --rebuild" I get       the error "-ba: unknown option" or "--rebuild: unknown option" or       "-ta: unknown option".
- A) With the Red Hat 8.0 release, the building options were removed       from the "rpm" command.  Use the "rpmbuild" command instead       ("rpmbuild --rebuild python2.3-2.3-1pydotorg.src.rpm").
- Q) I'm getting the "-ba: unknown option" when trying to build RPMs       using distutils "python setup.py bdist_rpm".
- A) As noted above, Red Hat broke the "build" functionality out of       the base "rpm" command with the 8.0 release.  Unfortunately,       they didn't patch their python RPM to account for this, and they       don't appear to be planning to release any errata to fix this.       If you upgrade to the 2.2.2-7 or newer RPMs on this page, distutils       should work.  Note that this seems to be fixed in the Red Hat 9       release (which uses Python 2.2.2 and has a patched distutils).
- Q) When trying to build RPMs, I get "rpmbuild: command not found".
- A) The "rpmbuild" command is part of a separate RPM named "rpm-build".       You will need to install this package before you can build RPMs.