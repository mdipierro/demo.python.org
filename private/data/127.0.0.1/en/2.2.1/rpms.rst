Linux RPMs for Python 2.2.1
===========================

Except where noted, these RPMs are made
available by Sean Reifschneider 
(`jafo-rpms@tummy.com <mailto:jafo-rpms@tummy.com>`_).

Having Problems?
~~~~~~~~~~~~~~~~

If you are having problems, please see the RPM Frequently
Asked Questions section at the end of this document for possible
solutions.

New in version 2.2.1-2
~~~~~~~~~~~~~~~~~~~~~~

- The -devel package includes a Makefile.pre.in, for building Zope.
- Installs "python2.2" as well as "python2.2".  This should allow it       to interoperate better with the Red Hat provided Python 2.2 package       in 7.3.
- Available as source and binaries for Red Hat 7.3.

**Warning:** These packages install as "/usr/bin/python2".  This is
because many of the Red Hat tools rely on "/usr/bin/python" being 1.5.
For Python code which requires 2.2, they should probably change to use
"/usr/bin/python2".  The SRPM can be modified to build packages which
install as "/usr/bin/python" -- count on things breaking if you do this.

Download
~~~~~~~~

- Signature:  - The following packages were signed with the GPG key in `KRUD-GPG-KEY </ftp/python/2.2.1/rpms/KRUD-GPG-KEY>`_
- Source:  - The base Python tar-file can be used to build binary RPMs using the command "rpm -ta Python-2.2.1.tgz".   **Note:** the tar file includes the 2.2.1-1 .spec file, use the next link for 2.2.1-2. - `python2-2.2.1-2.src.rpm </ftp/python/2.2.1/rpms/python2-2.2.1-2.src.rpm>`_ - (optional) `expat-1.1-4tummy.src.rpm </ftp/python/2.1/expat-1.1-4tummy.src.rpm>`_  (Needed for building Python SRPM, for systems that don't provide expat-devel)
- Red Hat 7.3 Binaries:   **RH 7.3 Note:** Red Hat 7.3 ships with a copy of Python 2.2 (not 2.2.1).  - `python2-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-2.2.1-2.i386.rpm>`_ (RedHat-based 7.3 base RPM) - `python2-tkinter-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-tkinter-2.2.1-2.i386.rpm>`_ (RedHat-based 7.3 tkinter RPM) - `python2-devel-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-devel-2.2.1-2.i386.rpm>`_ (RedHat-based 7.3 development RPM) - `python2-tools-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-tools-2.2.1-2.i386.rpm>`_ (RedHat-based 7.3 Tools RPM, including IDLE) - `python2-docs-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-docs-2.2.1-2.i386.rpm>`_ (Documentation in HTML and info formats)
- Red Hat 7.2 Binaries:  - **Note:** These RPMs are built from the 2.2.1-1 release.  Use the src.rpm above to create 2.2.1-2 RPMs. - `python2-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-2.2.1-1.i386.rpm>`_ (RedHat-based 7.2 base RPM) - `python2-tkinter-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-tkinter-2.2.1-1.i386.rpm>`_ (RedHat-based 7.2 tkinter RPM) - `python2-devel-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-devel-2.2.1-1.i386.rpm>`_ (RedHat-based 7.2 development RPM) - `python2-tools-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-tools-2.2.1-1.i386.rpm>`_ (RedHat-based 7.2 Tools RPM, including IDLE) - `python2-docs-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-docs-2.2.1-1.i386.rpm>`_ (Documentation in HTML and info formats)
- Red Hat 6.2 Binaries:  - **Note:** These RPMs are built from the 2.2.1-1 release.  Use the src.rpm above to create 2.2.1-2 RPMs. - `python2-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-2.2.1-1.i386.rpm>`_ (RedHat-based 6.2 base RPM) - `python2-tkinter-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-tkinter-2.2.1-1.i386.rpm>`_ (RedHat-based 6.2 tkinter RPM) - `python2-devel-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-devel-2.2.1-1.i386.rpm>`_ (RedHat-based 6.2 development RPM) - `python2-tools-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-tools-2.2.1-1.i386.rpm>`_ (RedHat-based 6.2 Tools RPM, including IDLE) - `python2-docs-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-docs-2.2.1-1.i386.rpm>`_ (Documentation in HTML and info formats)

Files, `MD5 <../md5sum.py>`_ checksums and sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    **Source**
        d14a188a9d4ccfae2ad53920d2d4b4af `python2-2.2.1-2.src.rpm </ftp/python/2.2.1/rpms/python2-2.2.1-2.src.rpm>`_ (7477437 bytes)

      **Redhat 7.3**
        414340f193bf0c0d20bd9846bdd075d4 `python2-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-2.2.1-1.i386.rpm>`_ (5670565 bytes)
        5eeffb528beb2e3e668e46fbd5665598 `python2-devel-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-devel-2.2.1-1.i386.rpm>`_ (1926741 bytes)
        35d220cf9fa530d93092cb1848dfb574 `python2-docs-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-docs-2.2.1-1.i386.rpm>`_ (1438713 bytes)
        3b392145289a33c88383e9d66ad9fcc2 `python2-tkinter-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-tkinter-2.2.1-1.i386.rpm>`_ (320522 bytes)
        f336b3193c3eac67b939c063a7872b18 `python2-tools-2.2.1-2.i386.rpm </ftp/python/2.2.1/rpms/rh7.3/python2-tools-2.2.1-1.i386.rpm>`_ (343483 bytes)

      **Redhat 7.2**
        fe04c9397155a952174150c81452327c `python2-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-2.2.1-1.i386.rpm>`_ (5694849 bytes)
        4ada9feaf97521140909c843f7d97ef1 `python2-devel-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-devel-2.2.1-1.i386.rpm>`_ (1951519 bytes)
        9ae59f01ef3c7741faa4abf5feaad221 `python2-docs-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-docs-2.2.1-1.i386.rpm>`_ (1438488 bytes)
        22f11a28dfe540f3e4fa69e335629d94 `python2-tkinter-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-tkinter-2.2.1-1.i386.rpm>`_ (320522 bytes)
        c0909fd8880059acf17c1a92402244bc `python2-tools-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh7.2/python2-tools-2.2.1-1.i386.rpm>`_ (343471 bytes)

      **Redhat 6.2**
        b0f333d0676580d872454d5b56d06db6 `python2-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-2.2.1-1.i386.rpm>`_ (5975575 bytes)
        41b8aa98b31e8b7a7182bb0c0d67a8b5 `python2-devel-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-devel-2.2.1-1.i386.rpm>`_ (1808627 bytes)
        ba5f6b36bb8df9d9ca249448a1d07b25 `python2-docs-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-docs-2.2.1-1.i386.rpm>`_ (1460393 bytes)
        067d782d8d1416ad7082ab9b6673d5d1 `python2-tkinter-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-tkinter-2.2.1-1.i386.rpm>`_ (295078 bytes)
        caa4e92783fbab5bb548f6c1b480950d `python2-tools-2.2.1-1.i386.rpm </ftp/python/2.2.1/rpms/rh6.2/python2-tools-2.2.1-1.i386.rpm>`_ (349253 bytes)

The following SRPMs are available for the "SME Server" distribution
of Linux (what was formerly known as "e-smith" before its acquisition
by Mitel Networks).  They are maintained by 
`Dan York <mailto:dan_york@mitel.com>`_.
The RPMs themselves are in:

`ftp://ftp.e-smith.org/pub/e-smith/contrib/DanYork/RPMS/i386/ 
<ftp://ftp.e-smith.org/pub/e-smith/contrib/DanYork/RPMS/i386/>`_ 

and a simple HOWTO for installing them is at: 

`http://www.lodestar2.com/software/howto/python2-sme-howto.html <http://www.lodestar2.com/software/howto/python2-sme-howto.html>`_

RPM Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Q) **What are the benefits of building my own binary RPM?  I want to          just download binary RPMs and install them.**
- A) If the provided binary RPMs work on your system, fantastic.          You may experience problems if you are running an older or newer          version of the operating system or any of the libraries, or an          RPM-based system which doesn't have binary RPMs available above.            Source RPMs (SRPMs) are the solution to this problem.  A benefit          of an SRPM is that it includes *ALL* of the instructions required to          build the binary from the source.  Building an SRPM is extremely          easy, everything happens automatically...    See the related question on how to build binary          RPMs.
- Q) **How do I build binary RPMs on my system?**
- A) To build a binary tailored to your system, download the source          RPM and run:             .. code-block::      rpm --rebuild <;packagename>.src.rpm             or download the original tar file and run:             .. code-block::      rpm -ta <;packagename>.tgz             Note: this does not actually install <;packagename>.          The resulting binary RPMs are written to a system-dependent          location, but can be found by looking toward the end of          the output of the above commands for lines starting with          "**Wrote:**".  For example:   .. code-block::      [...]        Finding  Provides: (using /usr/lib/rpm/find-provides)...        Finding  Requires: (using /usr/lib/rpm/find-requires)...        PreReq: rpmlib(PayloadFilesHavePrefix) <;= 4.0-1           rpmlib(CompressedFileNames) <;= 3.0.4-1        Requires(rpmlib): rpmlib(PayloadFilesHavePrefix) <;= 4.0-1           rpmlib(CompressedFileNames) <;= 3.0.4-1        **Wrote: /home/jafo/rpm/SRPMS/python2-2.2.1-2.src.rpm**        **Wrote: /home/jafo/rpm/RPMS/i386/python2-2.2.1-2.i386.rpm**        **Wrote: /home/jafo/rpm/RPMS/i386/python2-devel-2.2.1-2.i386.rpm**        **Wrote: /home/jafo/rpm/RPMS/i386/python2-tkinter-2.2.1-2.i386.rpm**        **Wrote: /home/jafo/rpm/RPMS/i386/python2-tools-2.2.1-2.i386.rpm**        **Wrote: /home/jafo/rpm/RPMS/i386/python2-docs-2.2.1-2.i386.rpm**        Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.73606        [...]     These RPMs must then be installed with 'rpm -U' or the equivalent.
- Q) **Why do I get "--rebuild: unknown option" or          "-ta: unknown option" when building from source?**
- A) Some distributions (notably, Red Hat 8.x) running the latest  	 versions of rpm have removed the building functionality from 	 the 'rpm' command.  If you see complaints such as the above, 	 simply use the 'rpmbuild' command instead.
- Q) **Why do I get "failed dependency" errors such as:**   .. code-block::      error: failed dependencies:              libcrypto.so.2   is needed by python2-2.2.1-1              libdb-3.2.so   is needed by python2-2.2.1-1              libreadline.so.4   is needed by python2-2.2.1-1              libssl.so.2   is needed by python2-2.2.1-1
- A) The short answer is that you are running a system which is          sufficiently different from the machine that the RPMs were built          on.  For example, if you are running Red Hat 7.1 and download the          packages built on Red Hat 7.3, your system has different sets of          libraries.            Don't panic!  Unlike some systems which blindly continue          along, hoping that the libraries are "close enough" to work          (or worse yet, install their own copies of those libraries), the          RPM system will track this and warn you of a possible problem.    The best solution to this is to build a set of binary RPMs which          are custom tailored to your system...  It's easy.  See the          related question on how to build binary          RPMs.