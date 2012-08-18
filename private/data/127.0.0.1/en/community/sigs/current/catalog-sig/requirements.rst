Catalog Requirements
~~~~~~~~~~~~~~~~~~~~

There are a few steps needed to find and install a package:

- Discovery : which module does what I need?
- Download  : where can I get a copy?
- Security  : is this actually from the package author, and not a                 Trojan horse?
- Installation : how do I compile the package, install it, and set it up?
- Updating : what's the latest version of a package?  do I need to                get an updated version for my system?

The `Distutils SIG </community/sigs/current/distutils-sig/>`_ focuses on the
hardest and most complicated step, #4, so the Catalog SIG doesn't
really have to concern itself with that problem.

Requirements from #1
####################

1.1) Users can browse through a list of available packages, browse
through a hierarchy like Parnassus, or do keyword searches.

1.2) Packages are also indexed by author and date, so you can see all
of Moshe's packages, or the 10 most recently changed packages.

1.3) For each author, their name, e-mail and home page URL are stored. 

1.4) Information about a package is only extracted from the metadata
included in the package's setup.py file.  This ensures that the info
is up-to-date, saves users the effort of entering data, and encourages
people to use the Distutils.

Requirements from #2
####################

2.1) Given a package name, software can retrieve one or more download
URLs for the package.

2.2) The catalog should keep copies of the code, not just point to
remote sites, in order to prevent disasters

2.3) It should be possible to mirror the catalog without too much
trouble, using a conventional FTP or HTTP mirroring script.

Requirements from #3
####################

3.1) Users can check a signature on the downloaded package,
using an external tool such as GnuPG.

3.2) Checking the signature is optional, and can be skipped if the
external tool isn't available.  (We could implement our own signature
scheme with Python code, but that's a bad idea; security is hard, and
few people will bother to generate keys that are only useful only for
distributing Python modules.

Related requirement: the Distutils sdist and bdist_* commands should
have a --sign switch to sign the generated .tgz, .rpm, or whatever
file.

Requirements from #4
####################

None

Requirements from #5
####################

Not covered by this page.  This includes checking for updated
versions, tracking dependencies between Python packages, and between
Python packages and system libraries.  These seem to be difficult
problems that require a database of Python packages installed on a
system.

.. code-block::

    Information about a package
    ===========================
    Name
    Version
    Supported Platforms
    Description
    Keywords
    Homepage URL
    Author IDs
    License
    Download link
    Date of release

    Left out for now:
    Dependency information 

    Information about an author
    ===========================
    Name
    Home page
    GnuPG/PGP key (both the actual key, and just the ID)
    E-mail address (used as ID?)
    E-mail address public: y/n

    Information about a document
    ============================
    Name
    Author
    Description
    URL of HTML version
    URL of printable version
    URL and format of downloadable version
      (Any of these URLs can be omitted if not applicable.)