Python.org Maintenance and Administration
-----------------------------------------

This document is incomplete; we're updating it as questions come up. If
you have questions, try the webmaster alias first, then `pydotorg-www <http://mail.python.org/mailman/listinfo/pydotorg-www/>`_
if you don't get a response.

Getting Started
---------------

To learn how to maintain the Python.org website, please read the
`Python.org Website Maintenance <website/>`_ document and
explore the `Admin wiki page <http://wiki.python.org/moin/Admin>`_.

If you would like to volunteer to help maintain the Python.org website,
please send a note to the `pydotorg-www <http://mail.python.org/mailman/listinfo/pydotorg-www/>`_ mailinglist.

Mailing Lists
-------------

There are four mailing lists for python.org maintainers; many
maintainers are on all the lists.

`pydotorg-www <http://mail.python.org/mailman/listinfo/pydotorg-www/>`_ 

    This is a public discussion list for anyone interested in the
    development of the python.org website.

webmaster  (`Autoreply text <http://mail.python.org/replybot/webmaster.txt>`_) 

    Mail that's sent to the webmaster goes to this list.  There is an
    auto-responder that returns a general reply, answering a number of the
    most common questions and providing information about other sources of
    help.  If you think the auto-response mail includes the answer to a
    question sent to webmaster, the question does not need to be answered by a
    human.

    If a response is appropriate, please ``Cc:`` the webmaster address so
    others can see that the question has been answered.  Note that taking
    action (such as updating the web site) always makes a response
    appropriate; people deserve to know that their e-mail was welcome and
    helpful.

    If you're responding to webmaster mail, you may want to set either
    ``From:`` or ``Reply-To:`` to `webmaster@python.org <mailto:webmaster%40python.org>`_; that will keep replies
    from cluttering your personal box.

    If you want to volunteer to help out responding to webmaster email, send a
    note to `webmaster@python.org <mailto:webmaster%40python.org>`_ asking to be added.

`pydotorg <http://mail.python.org/mailman/listinfo/pydotorg/>`_ 

    This is a private internal discussion list used for discussion among the
    python.org server maintainers. If you have SSH login access on the
    python.org servers, you should probably be on this list.

`pydotorg-checkins 
<http://mail.python.org/mailman/listinfo/pydotorg-checkins/>`_ 

    This internal list receives reports of all changes to the SVN
    repositories.

The following additional addresses are used in collecting information
in the process of maintaining python.org; these also are hosted in the
python.org domain.

**MISSING**

IRC
---

Occasionally volunteers will use IRC to communicate: the server used is
``irc.freenode.net``, on the ``#pydotorg`` channel.

Machines
--------

There are several machines which support the operation of python.org, all of
which are currently hosted by `XS4ALL <http://www.xs4all.com/>`_.  The primary machine is
www.python.org (also known as &quot;dinsdale.python.org&quot;).  This machine hosts
the static content of the site and some light CGI scripts (the FAQ Wizard,
in particular).

**MISSING**
**Machine**   **Functions**
ximinez   Wiki, PostgreSQL, pypi

dinsdale   Main www python.org, SVN, planet.python.org.

bag   Mail

The following people are available for emergency root access to
machines. Contact should be attempted through the `pydotorg <http://mail.python.org/mailman/listinfo/pydotorg/>`_ list first.

**MISSING**
**Person**   **Timezone**
Barry Warsaw   US/Eastern

Sean Reifschneider   US/Pacific

Thomas Wouters   Western Europe

Anthony Baxter   Australia

Mail processing occurs on mail.python.org.  Barry Warsaw maintains the
`Mailman <http://www.list.org/>`_ installation on that machine.

Adding Subversion Commit Access
-------------------------------

Here are the instructions for `adding <http://mail.python.org/mailman/private/pydotorg/2005-November/007885.html>`_ Subversion commit access for new
developers, or updating the public keys for existing developers.  Because
this list archive is private, you will need to be a member of the mailing
list to read this article.