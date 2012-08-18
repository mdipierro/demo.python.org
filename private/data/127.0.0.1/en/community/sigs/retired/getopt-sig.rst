Python Getopt SIG
-----------------

The purpose of this SIG was to come up with a new and improved library
for command-line parsing in Python 2.3.  Everybody seems to agree that
the venerable getopt module just doesn't do enough.  The
trick is to find something that is sufficiently powerful and flexible
without being too complex to use, especially for novice programmers.

The SIG was kicked off shortly after David Goodger and
Greg Ward (your humble narrator
and champion of this SIG) independently proposed adding
`Optik <http://optik.sourceforge.net/>`_
to the standard library.  This kicked off
`a brief thread <http://mail.python.org/pipermail/python-dev/2002-February/019934.html>`_
on python-dev, the outcome of which is that Paul Prescod posted a
`request for comments <http://mail.python.org/pipermail/python-announce-list/2002-February/001236.html>`_
to get input from the wider community.  Several people chimed in
with their opinions, and Guido told us to go off
and figure out a solution, then report back to python-dev.

Comparing some libraries
~~~~~~~~~~~~~~~~~~~~~~~~

I decided the only fair way to compare various libraries is to
implement the same command-line interface with several of them.
Here are `the results <compare>`_ of that experiment.

Optik, renamed to `optparse <http://docs.python.org/library/optparse.html>`_, 
was added to Python 2.3's standard library.