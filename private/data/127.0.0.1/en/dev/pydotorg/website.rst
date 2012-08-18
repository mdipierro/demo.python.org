Python.org Website Maintenance
==============================

This is a guide to setting up and using the software necessary to
maintain the Python.org website.  This document is under construction;
more information may be found at `http://wiki.python.org/moin/PythonWebsite <http://wiki.python.org/moin/PythonWebsite>`_

If you wish to volunteer to help maintain the Python.org website,
please sign up to the `pydotorg-www <http://mail.python.org/mailman/listinfo/pydotorg-www>`_ mailing list.

- `Obtain Python.org Data <#obtain-python-org-data>`_

- `Building a Local Copy <#building-a-local-copy>`_

- `Diagnosing Problems <#diagnosing-problems>`_

`Obtain Python.org Data <#id1>`_
--------------------------------

The command to check out a working copy of the Python.org site data
from the Python Subversion repository is:

.. code-block::

    svn co https://svn.python.org/www/trunk/beta.python.org

Please note that this repository contains several hundred megabytes. 

To be able to directly make changes to these files, you will need
write access to the repository.  Please send a note to
`pydotorg-www@python.org <http://mail.python.org/mailman/listinfo/pydotorg-www>`_ if you'd
like to volunteer to work on the site.

If you have write access, use the following command instead: 

.. code-block::

    svn co svn+ssh://pydotorg@svn.python.org/trunk/beta.python.org

`Building a Local Copy <#id2>`_
-------------------------------

Refer to build/README for a list of dependencies and details on
building a local copy of the website.  In summary:  You will
need Python 2.5 or 2.6, mako, pyyaml, and docutils and about
1 to 3 minutes for the initial build of the website.

`Diagnosing Problems <#id3>`_
-----------------------------

The links on `the status page <http://www.python.org/status/>`_ are
useful, especially the `&quot;Log of all commits and builds&quot; <http://www.python.org/status/updates/>`_ and the &quot;Post commit
logging file&quot; (which may be very large).