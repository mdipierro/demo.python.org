Web SIG
=======

The Python Web SIG is dedicated to improving Python's support for
interacting with World Wide Web services and clients.

Charter
-------

The first task should be to create a plan (in the form of a PEP) for
bringing the Web support in the standard Python library up to modern
standards.  This would address capabilities such as (but not limited
to) CSS parsing, XHTML parsing and generation support, client-side and
server-side SSL support, simple server frameworks,
multi-part/form-data POST support, and CGI support.  I suggest that we
set a time limit of six months for coming up with a plan.

Some concrete suggestions on how to draw up a work list follow.
The task can be divided into two parts, client and server.

On the client side, a great deal of mechanism is available, but it's
been developed in a patchwork fashion over the last 10 years.  I'd
suggest that we build a checklist based on looking at some client-side
tool like curl, then add the ability to do everything in that
checklist to Python's &quot;httplib&quot; module.  Additional API sugar could
also be added, probably in a new module.  HTML and XML parsing are
pretty solid, but a critical lack on the client side is the lack of a
CSS parser.

On the server side, things are a bit more dire.  The stdlib contains
three web server modules, BaseHTTPServer, SimpleHTTPServer, and
CGIHTTPServer, none of which are up to today's web tasks.  I'd suggest
a similar strategy here: pick a Web framework that already exists,
make a functionality checklist from it, and add that functionality to
a new webserver module.  I'd start with Medusa, since I'm familiar
with it and pretty happy with it, but something else might be
better. The other major problem on the server side is the lack of
server-side SSL support, critical in today's hostile networking
environment. Finally, something like PyPHP would be a good thing to
support in the webserver module.

Related Links
-------------

- `Mailing list <http://mail.python.org/mailman/listinfo/web-sig>`_

- `Mailing list archives <http://www.python.org/pipermail/web-sig/>`_

- `Web programming Wiki page <http://www.python.org/cgi-bin/moinmoin/WebProgramming>`_