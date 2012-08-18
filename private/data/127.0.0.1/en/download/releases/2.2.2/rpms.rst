Linux RPMs for Python 2.2.2
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

For platforms in which binaries aren't available here, you can easily build
binary RPMs directly from the Python source tar file.  Simply download it
and run "rpmbuild -ta Python-2.2.2.tgz".  Note toward the end of the
output, the lines starting with "Wrote:" indicate where the binary RPMs
were written.

The benefit of building binary RPMs in this way is that they are built
using exactly the set of libraries and versions of packages that you have
installed on your system.  Because the SRPMs encompass all the steps
required to build binary RPMs, it is a "fire and forget" process -- the
simplest source build ever...

Download
~~~~~~~~

- **Signature:** - Many of the following packages were signed with the GPG key in `KRUD-GPG-KEY </ftp/python/2.2.2/rpms/KRUD-GPG-KEY>`_
- **Source:** - **The base Python tar-file has a problem that prevents it from being built as an RPM.  Use the following instead:** - `python2.2.2-2.2.2-1.src.rpm </ftp/python/2.2.2/rpms/python2.2.2-2.2.2-1.src.rpm>`_ (Python.org Source RPM, 6667399 bytes)
- **Red Hat 8.0, Red Hat RPM:** - These RPMs are built from Red Hat's SRPM, not the python.org tar-file.  These RPMs are meant to more closely match the standard Python provided by Red Hat. - `python-2.2.2-7.src.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-2.2.2-7.src.rpm>`_ (Source RPM, 6952435 bytes) - `python-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-2.2.2-7.i386.rpm>`_ (Red Hat 8.0 base RPM, 4221481 bytes) - `python-devel-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-devel-2.2.2-7.i386.rpm>`_ (Red Hat 8.0 development RPM, 1120252 bytes) - `python-docs-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-docs-2.2.2-7.i386.rpm>`_ (Documentation in HTML and info formats, 1805611 bytes) - `python-tools-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-tools-2.2.2-7.i386.rpm>`_ (Red Hat 8.0 additional Python tools RPM, 35856 bytes) - `tkinter-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/tkinter-2.2.2-7.i386.rpm>`_ (Red Hat 8.0 Tk GUI library, 265454 bytes) - `sip-3.3.2-4tummy.src.rpm </ftp/python/2.2.2/rpms/redhat8.0/sip-3.3.2-4tummy.src.rpm>`_ (Red Hat 8.0 sip SRPM patched for 2.2.2, 161437 bytes) - `sip-3.3.2-4tummy.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/sip-3.3.2-4tummy.i386.rpm>`_ (Red Hat 8.0 sip RPM for 2.2.2, 97762 bytes) - `sip-devel-3.3.2-4tummy.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/sip-devel-3.3.2-4tummy.i386.rpm>`_ (Red Hat 8.0 sip devel RPM, 9889 bytes)
- **SuSE 8.1 RPM:** `IDLE-0.8-1.noarch.rpm </ftp/python/2.2.2/rpms/suse8.1/IDLE-0.8-1.noarch.rpm>`_ (211393 bytes, most likely works on any other Linux distribution)

Files, `MD5 <../md5sum.py>`_ checksums and sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    **Source (python.org SRPM)**
       cee208ea027bbe4634ab7d8b313d86e6 `python2.2.2-2.2.2-1.src.rpm </ftp/python/2.2.2/rpms/python2.2.2-2.2.2-1.src.rpm>`_ (6667399 bytes)
      **Red Hat 8.0 (based on Red Hat's SRPM)**
       ff9660dde4d5f736c42409c8815f1634 `python-2.2.2-7.src.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-2.2.2-7.src.rpm>`_ (6952435 bytes)
       4263943b81be5554df3f8c10a5ff406a `python-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-2.2.2-7.i386.rpm>`_ (4221481 bytes)
       e8876066aa09f7faaa6f65cef454d154 `python-devel-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-devel-2.2.2-7.i386.rpm>`_ (1120252 bytes)
       53cda5b684e1fdbacd45d54af7030fbd `python-docs-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-docs-2.2.2-7.i386.rpm>`_ (1805611 bytes)
       5df2626864e7ebd873d21eac137f86de `python-tools-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/python-tools-2.2.2-7.i386.rpm>`_ (35856 bytes)
       7dd780a09e58609bf2cb4ce1432e0196 `tkinter-2.2.2-7.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/tkinter-2.2.2-7.i386.rpm>`_ (265454 bytes)
       62ec85229cbf98af26abfef81cf8b17d `sip-3.3.2-4tummy.src.rpm </ftp/python/2.2.2/rpms/redhat8.0/sip-3.3.2-4tummy.src.rpm>`_ (161437 bytes)
       b96bb61ce8428d31d485d1da8cf5dffa `sip-3.3.2-4tummy.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/sip-3.3.2-4tummy.i386.rpm>`_ (97762 bytes)
       141405d7d7eea35e3494e0ca11373aa6 `sip-devel-3.3.2-4tummy.i386.rpm </ftp/python/2.2.2/rpms/redhat8.0/sip-devel-3.3.2-4tummy.i386.rpm>`_ (9889 bytes)

RPM Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Q) Why I try to run "rpmbuild -ta Python-2.2.2.tgz", I get the       error: "error: File /root/Python-2.2.2b1.tgz: No such file or       directory".
- A) Yes, there's a problem with the .spec file in the base tar       file.  Use the SRPM that is on this page...
- Q) When running "rpm -ba", "rpm -ta" or "rpm --rebuild" I get       the error "-ba: unknown option" or "--rebuild: unknown option" or       "-ta: unknown option".
- A) With the Red Hat 8.0 release, the building options were removed       from the "rpm" command.  Use the "rpmbuild" command instead       ("rpmbuild -ta Python-2.2.2.tgz").
- Q) I'm getting the "-ba: unknown option" when trying to build RPMs       using distutils "python setup.py bdist_rpm".
- A) As noted above, Red Hat broke the "build" functionality out of       the base "rpm" command with the 8.0 release.  Unfortunately, they didn't       patch their python RPM to account for this, and they don't appear to be       planning to release any errata to fix this.  If you upgrade to the       2.2.2-7 RPMs on this page, distutils should work.  Note that this       seems to be fixed in the Red Hat 9 release (which uses Python 2.2.2,       which has a patched distutils).
- Q) When trying to build RPMs, I get "rpmbuild: command not found".
- A) The "rpmbuild" command is part of a separate RPM "rpm-build".       You will need to install this package before you can build RPMs.