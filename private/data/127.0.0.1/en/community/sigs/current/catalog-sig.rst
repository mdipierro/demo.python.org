SIG for Python Resource Cataloguing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This SIG exists in order to discuss and build a catalog of Python resources.  The SIG charter is:

    The Python Catalog SIG aims at producing a master index of Python
    software and other resources.  It will begin by figuring out what the
    requirements are, converging on a design for the data schema, and
    producing an implementation.  ("Implementation" will almost certainly
    include mean a set of CGI scripts for browsing the catalog, and may
    also contain a standard library module for automatically fetching and
    installing modules, if the SIG decides that's a worthwhile feature.)

SIG Links
#########

- `Requirements document <requirements>`_
- `Other packaging systems <others>`_
- `Subscribing to the mailing list <http://mail.python.org/mailman/listinfo/catalog-sig>`_
- `Archives <http://mail.python.org/pipermail/catalog-sig/>`_

Current Status
##############

As of February 2003, the Python Package Index is operational and
available at `http://pypi.python.org/pypi <http://pypi.python.org/pypi/>`_.  The
list of indexed packages is still quite small; please add your
packages!

Some relevant PEPs have been written:

- PEP   241: Metadata for Python Software Packages: Implemented and   included in Python 2.1.
- PEP 243:   Module Repository Upload Mechanism: A draft specifying how to upload   files to a catalog server.
- PEP 262:   Database of Installed Python Packages: A now-withdrawn proposal    for a database of installed Python packages.
- PEP 301:   Package Index and Metadata for Distutils: Specifies a Distutils   register command for registering packages with a   central catalog.