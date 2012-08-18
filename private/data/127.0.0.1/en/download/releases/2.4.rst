Python 2.4
----------

    **Python 2.4 has been replaced by a newer bugfix
    release.** Please see the `releases page <../>`_ to select a more
    recent release.

We are pleased to announce the release of **Python 2.4, final**
on November 30, 2004.  This is a final, stable release, and we
can recommend that Python users upgrade to this version.

    **Important:** This release is vulnerable to the problem described in
    `security advisory PSF-2006-001 </news/security/PSF-2006-001/>`_
    &quot;Buffer overrun in repr() of unicode strings in wide unicode
    builds (UCS-4)&quot;.  This fix is included in `Python 2.4.4 <../2.4.4/>`_

    **Note: there's a** `security fix </news/security/PSF-2005-001/>`_
    **for SimpleXMLRPCServer.py - this fix is included in** `2.4.1 </download/releases/2.4.1/>`_

Python 2.4 is the result of almost 18 month's worth of work on top
of Python 2.3 and represents another stage in the careful evolution
of Python. New language features have been kept to a minimum, many
bugs have been fixed and a `variety of improvements <highlights>`_
have been made.

Notable changes in Python 2.4 include improvements to the importing of
modules, function decorators, generator expressions, a number of new
modules (including subprocess, decimal and cookielib) and a host of
bug fixes and other improvements. See the (subjective)
`highlights <highlights>`_ or the `detailed release notes <notes>`_
for more, or consult Andrew Kuchling's
`What's New In Python </doc/2.4/whatsnew/whatsnew24.html>`_
for a detailed view of some of the new features of Python 2.4.

Please see the separate `bugs page <bugs>`_ for known
issues and the bug reporting procedure.

Download the release
--------------------

Starting with the Python 2.4 releases the **Windows** Python
installer is being distributed as a Microsoft Installer (.msi) file.
To use this, the Windows system must support Microsoft Installer
2.0. Just save the installer file
`python-2.4.msi </ftp/python/2.4/python-2.4.msi>`_
to your local machine, then double-click python-2.4.msi to find
out if your machine supports MSI. If it doesn't, you'll need to
install Microsoft Installer first. Many other packages (such as
Word and Office) also include MSI, so you
may already have it on your system. If not, you can download it freely
from Microsoft for `Windows  95, 98 and Me <http://www.microsoft.com/downloads/details.aspx?FamilyID=cebbacd8-c094-4255-b702-de3bb768148f&displaylang=en>`_ and for `Windows  NT 4.0 and 2000 <http://www.microsoft.com/downloads/details.aspx?FamilyID=4b6140f9-2d36-4977-8fa1-6f8a0f5dca8f&DisplayLang=en>`_. Windows XP and later already have MSI; many
older machines will already have MSI installed.

The new format installer allows for `automated installation <msi#automated>`_ and `many other  shiny new features <msi>`_. There is also a separate installer
`python-2.4.ia64.msi </ftp/python/2.4/python-2.4.ia64.msi>`_
for Win64-Itanium users.

Windows users may also be
interested in Mark Hammond's `win32all <http://starship.python.net/crew/mhammond/win32/>`_ package, available from `Sourceforge <http://sourceforge.net/project/showfiles.php?group_id=78018>`_. win32all adds a number of Windows-specific
extensions to Python, including COM support and the Pythonwin IDE.

Debian users using `Sarge <http://www.debian.org/releases/sarge/>`_: Python
2.4 has already been packaged for you. Simply ``apt-get install python2.4``.
Note that you will also need to install python2.4 versions of any other
modules you use.

**All others** should download either
`Python-2.4.tgz </ftp/python/2.4/Python-2.4.tgz>`_ or
`Python-2.4.tar.bz2 </ftp/python/2.4/Python-2.4.tar.bz2>`_,
the source archive.  The tar.bz2 is considerably smaller, so get that one if
your system has the `appropriate  tools <http://sources.redhat.com/bzip2/>`_ to deal with it. Unpack it with
``tar -zxvf Python-2.4.tgz`` (or
``bzcat Python-2.4.tar.bz2 | tar -xf -``).
Change to the Python-2.4 directory
and run the &quot;./configure&quot;, &quot;make&quot;, &quot;make install&quot; commands to compile
and install Python. The source archive is also suitable for Windows users
who feel the need to build their own version.

**Fedora Core 3** users can download
`RPMs <rpms>`_, or build from source.  An SRPM is also
available for other RPM-based systems, or the source tar-file can be used
(see the &quot;rpm&quot; man page for the &quot;-ta&quot; options).

What's New?
-----------

- See the `highlights <highlights>`_ of this release.

- Andrew Kuchling's `What's New in Python 2.4 </doc/2.4/whatsnew/whatsnew24.html>`_ describes the most visible changes since `Python 2.3 </download/releases/2.3/>`_ in more detail.

- A detailed list of the changes is in the `release notes <notes>`_, or the ``Misc/NEWS`` file in the source distribution.

- For the full list of changes, you can poke around in `CVS <http://sourceforge.net/cvs/?group_id=5470>`_.

Documentation
-------------

The documentation has also been updated: 

- `Browse HTML on-line </doc/2.4/>`_

- Download using `HTTP </ftp/python/doc/2.4/>`_.

Downloadable packages of the documentation will be available shortly.

Files, `MD5 <md5sum.py>`_ checksums, signatures and sizes
---------------------------------------------------------

    ``149ad508f936eccf669d52682cf8e606`` `Python-2.4.tgz </ftp/python/2.4/Python-2.4.tgz>`_
    (9198035 bytes, `signature <Python-2.4.tgz.asc>`_)

    ``44c2226eff0f3fc1f2fedaa1ce596533`` `Python-2.4.tar.bz2 </ftp/python/2.4/Python-2.4.tar.bz2>`_
    (7840762 bytes, `signature <Python-2.4.tar.bz2.asc>`_)

    ``e9fe1fcdce9fa8c5590ab58b1de3246f`` `python-2.4.msi </ftp/python/2.4/python-2.4.msi>`_
    (10887168 bytes, `signature <python-2.4.msi.asc>`_)

    ``5810ed46da712adef93315b08791aea8`` `python-2.4.ia64.msi </ftp/python/2.4/python-2.4.ia64.msi>`_
    (8858624 bytes, `signature <python-2.4.ia64.msi.asc>`_)

The signatures above were generated with
`GnuPG <http://www.gnupg.org>`_ using release manager
Anthony Baxter's
`public key </download#pubkeys>`_
which has a key id of 6A45C816.