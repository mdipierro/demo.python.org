Alternative Implementations
---------------------------

This site hosts the &quot;traditional&quot; implementation of Python (nicknamed CPython).
A number of alternative implementations are available as well, namely

- `IronPython <http://ironpython.codeplex.com/>`_ (Python running on .NET)

- `Jython <http://www.jython.org/>`_ (Python running on the Java Virtual Machine)

- `PyPy <http://pypy.org/>`_ (A `fast <http://speed.pypy.org>`_ python implementation with a JIT compiler)

- `Stackless Python <http://www.stackless.com/>`_ (Branch of CPython supporting microthreads)

Download Python
---------------

The current production versions are `Python 2.7.3 <releases/2.7.3/>`_ and
`Python 3.2.3 <releases/3.2.3/>`_.

Start with one of these versions for learning Python or if you want the most
stability; they're both considered stable production releases.

If you don't know which version to use, start with Python 2.7; more existing
third party software is compatible with Python 2 than Python 3 right now.

For the MD5 checksums and OpenPGP signatures, look at the `detailed Python 
2.7.3 <releases/2.7.3/>`_ page: 

- `Python 2.7.3 Windows Installer </ftp/python/2.7.3/python-2.7.3.msi>`_ (Windows binary -- does not include source)

- `Python 2.7.3 Windows X86-64 Installer </ftp/python/2.7.3/python-2.7.3.amd64.msi>`_ (Windows AMD64 / Intel 64 / X86-64 binary `[1] <#id10>`_ -- does not include source)

- `Python 2.7.3 Mac OS X 64-bit/32-bit x86-64/i386 Installer </ftp/python/2.7.3/python-2.7.3-macosx10.6.dmg>`_ (for Mac OS X 10.6 and 10.7 `[2] <#id11>`_)

- `Python 2.7.3 Mac OS X 32-bit i386/PPC Installer </ftp/python/2.7.3/python-2.7.3-macosx10.3.dmg>`_ (for Mac OS X 10.3 through 10.6 `[2] <#id11>`_)

- `Python 2.7.3 compressed source tarball </ftp/python/2.7.3/Python-2.7.3.tgz>`_ (for Linux, Unix or Mac OS X)

- `Python 2.7.3 bzipped source tarball </ftp/python/2.7.3/Python-2.7.3.tar.bz2>`_ (for Linux, Unix or Mac OS X, more compressed)

Also look at the `detailed Python 3.2.3 <releases/3.2.3/>`_ page: 

- `Python 3.2.3 Windows x86 MSI Installer </ftp/python/3.2.3/python-3.2.3.msi>`_ (Windows binary -- does not include source)

- `Python 3.2.3 Windows X86-64 MSI Installer </ftp/python/3.2.3/python-3.2.3.amd64.msi>`_ (Windows AMD64 / Intel 64 / X86-64 binary `[1] <#id10>`_ -- does not include source)

- `Python 3.2.3 Mac OS X 64-bit/32-bit x86-64/i386 Installer </ftp/python/3.2.3/python-3.2.3-macosx10.6.dmg>`_ (for Mac OS X 10.6 and 10.7 `[2] <#id11>`_)

- `Python 3.2.3 Mac OS X 32-bit i386/PPC Installer </ftp/python/3.2.3/python-3.2.3-macosx10.3.dmg>`_ (for Mac OS X 10.3 through 10.6 `[2] <#id11>`_)

- `Python 3.2.3 compressed source tarball </ftp/python/3.2.3/Python-3.2.3.tgz>`_ (for Linux, Unix or Mac OS X)

- `Python 3.2.3 bzipped source tarball </ftp/python/3.2.3/Python-3.2.3.tar.bz2>`_ (for Linux, Unix or Mac OS X, more compressed)

A `comprehensive list of all released versions <releases/>`_
is available if you need source code for an older version of Python.

Other parties have re-packaged Python.  These re-packagings often
include more libraries or are specialized for a particular application:

- `ActiveState ActivePython <http://www.activestate.com/activepython/>`_ (commercial and community versions, including scientific computing modules)

- `pythonxy <http://www.pythonxy.com/>`_ (Scientific-oriented Python Distribution based on Qt and Spyder)

- `Conceptive Python SDK <http://www.conceptive.be/python-sdk.html>`_ (targets business, desktop and database applications)

- `Enthought Python Distribution <http://enthought.com/products/epd.php>`_ (a commercial distribution for scientific computing)

- `Portable Python <http://portablepython.com/>`_ (Python and add-on packages configured to run off a portable device)

- `PyIMSL Studio <http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx>`_ (a commercial distribution for numerical analysis ? free for non-commercial use)

Information about specific ports, and developer info: 

- `Windows (and DOS) <windows>`_

- `Macintosh <mac>`_

- `Other platforms <other>`_

- `Source <source>`_

- `Python Developer's Guide </dev/>`_

- `Python Issue Tracker <http://bugs.python.org/>`_

OpenPGP Public Keys
-------------------

Source and binary executables are signed by the release manager using
their OpenPGP key.  The release managers since Python 2.3 have been:

- Anthony Baxter (key id: `6A45C816 <http://www.python.org/~anthony/anthonypub.asc>`_)

- Georg Brandl (key id: `36580288 <http://www.python.org/~gbrandl/gbrandlpub.asc>`_)

- Martin v. L?wis (key id: `7D9DC8D2 <http://www.dcl.hpi.uni-potsdam.de/people/loewis/mvl.asc>`_)

- Benjamin Peterson (key id: `A4135B38 <http://www.python.org/~peterson/pubkey.asc>`_)

- Barry Warsaw (key id: `EA5BBD71 and ED9D77D5 <http://barry.warsaw.us/barrypub-gpg.asc>`_)

- Ronald Oussoren (key id: E6DF025C)

- Ned Deily (key id: `6F5E1540 <nadpub.asc>`_)

**Note:** Barry's key id EA5BBD71 is used to sign all Python 2.6 and 3.0
releases.  His key id ED9D77D5 is a v3 key and was used to sign older
releases.

You can import the release manager public keys by either downloading
`the public key file from here </files/pubkeys.txt>`_ and then
running

.. code-block::

    % gpg --import pubkeys.txt

or by grabbing the individual keys directly from the keyserver network
by running this command:

.. code-block::

    % gpg --recv-keys EA5BBD71 6A45C816 ED9D77D5 \
        7D9DC8D2 A4135B38 36580288

On the version-specific download pages, you should see a link to both the
downloadable file and a detached signature file.  To verify the authenticity
of the download, grab both files and then run this command:

.. code-block::

    % gpg --verify Python-3.2.3.tgz.asc

Note that you must use the name of the signature file, and you should use the
one that's appropriate to the download you're verifying.

- (These instructions are geared to `GnuPG <http://www.gnupg.org/>`_ and Unix command-line users. Contributions of instructions for other platforms and OpenPGP applications are welcome.)

Other Useful Items
------------------

- Looking for 3rd party **Python modules**?  The `Package Index <http://pypi.python.org/pypi/>`_ has many of them.

- You can `view <http://docs.python.org/>`_ the standard documentation online, or you can `download <http://docs.python.org/download>`_ it in HTML, PostScript, PDF and other formats.  See the main `Documentation </doc/>`_ page.

- Information on `tools for unpacking archive files <unpacking>`_ provided on python.org is available.

- **Tip**: even if you download a ready-made binary for your platform, it makes sense to also download the `source <source>`_. This lets you browse the standard library (the subdirectory **Lib**) and the standard collections of demos (**Demo**) and tools (**Tools**) that come with it.  There's a lot you can learn from the source!

- There is also a `collection of Emacs packages </emacs>`_ that the Emacsing Pythoneer might find useful.  This includes major modes for editing Python, C, C++, Java, etc., Python debugger interfaces and more.  Most packages are compatible with Emacs and XEmacs.

Want to contribute?  See the `Python Developer's Guide </dev/>`_
to learn about how Python development is managed.

Python is `OSI Certified Open Source <http://www.opensource.org/>`_:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/osi-certified-120x100.gif
   :alt: /images/osi-certified-120x100.gif

**MISSING**
[1]  *(`1 <#id1>`_, `2 <#id4>`_)* The binaries for AMD64 will also work on processors that implement the Intel 64 architecture (formerly EM64T), i.e. the architecture that Microsoft calls x64, and AMD called x86-64 before calling it AMD64. They will not work on Intel Itanium Processors (formerly IA-64).
**MISSING**
[2]  *(`1 <#id2>`_, `2 <#id3>`_, `3 <#id5>`_, `4 <#id6>`_)* There is important information about IDLE, Tkinter, and Tcl/Tk on Mac OS X here.