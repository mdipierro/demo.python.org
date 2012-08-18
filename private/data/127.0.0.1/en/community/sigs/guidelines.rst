Python SIG Creation Guidelines
------------------------------

The guidelines for creation of new SIGs are rather informal, but a
few key things are necessary.  First we outline the general framework
of the SIGs and then we describe what you have to do if you want us to
create a new SIG.

The SIG mailing lists are managed by
`GNU Mailman <http://www.list.org>`_, a web-based interface
for mailing lists written in Python.
Un/subscription requests, archiving of messages, etc. all happen
automatically, without human intervention.  This is A Good Thing (TM)
because such responses should be processed very quickly.  (While the
normal way to interact with a mailing list is via the SIG's &quot;listinfo&quot;
web page, it is also possible to send commands to a special
administrative address, see below.)

Every SIG must have a clear mission, with a well defined conclusion
and end date, and a coordinator - a specific person responsible for
reporting on the SIG activity and for shepherding the SIG's activity
and wrap-up.  The end date can be extended if activity warrants, but
we need some reasonable wrap-up objective to avoid maintenance of
unproductive SIGs.

To create a SIG once you can satisfy these criteria, propose it for
discussion on the `meta-sig </community/sigs/current/meta-sig/>`_ mailing list.  If
you get agreement that the SIG is worth creating - and in particular,
no other SIG nor the general Python newsgroup is already more suitable
- and your coordinator is ready, the SIG will be created.

Mailing List Framework
----------------------

Each mailing list has a short name, for example &quot;gui&quot;.  For each
SIG, there are three special addresses:

- <;name>-`sig@python.org <mailto:sig%40python.org>`_: The address for posting messages to the SIG mailing list.  Anything posted to this address gets forwarded to all list members, and also gets archived automatically.  Be careful what you send to this address!

- <;name>-`sig-request@python.org <mailto:sig-request%40python.org>`_: This is an email robot address which can process subscription and removal requests, help requests and other Mailman email commands.  Ordinarily, these messages will not be seen or processed by a human.  For more help send a message to this address with the word *help* in the ``Subject:`` header.

- <;name>-`sig-owner@python.org <mailto:sig-owner%40python.org>`_: This is an alias that reaches the administrators of the SIGs mailing list.  This will be the person who manages specifics of the mailing list, such as subscribe/unsubscribe approvals (if necessary), approving held posts, etc.  There is always a real person on the other end of this address, so if you need to contact a human being, this is the address to use.

Mailing List Policy
-------------------

Each mailing list has a policy for such things as who can join the
list, or post messages, etc.  In general all SIG lists have the
following (fairly lax) policy.  SIG owners are given their own web
interface to Mailman, so they can change the policy without our help.

- Subscriptions are open to everyone.  Approval will only be required if the subscribing address does not match the mail headers of the subscription message.

- Anyone can post messages to the list, even if they are not members of the list.  The list is not be moderated.

Creation Guidelines
-------------------

So you want to create a new SIG mailing list?  Well here's what you
have to do.  Most importantly, you have to take responsibility for
your list.  This means we get to alias
<;name>-`sig-owner@python.org <mailto:sig-owner%40python.org>`_ to your personal mailbox
``:-)``.  You won't get bugged too often (hopefully), but you may
occasionally have to process subscription approvals, and you will get
ignorable notification messages whenever someone subscribes or
unsubscribes.  Your most important job will likely be discarding the
spam messages that get sent to your list, but which Mailman rightfully
puts a hold on.

You should decide what your topic is going to be and what it's
scope is.  Try to keep it focused, and make sure you verify that no
other SIG covers your topic.  You need to write two things.  First,
you should write a short informational blurb about your SIG; just
something that can be put in a short list of SIGs, e.g. &quot;Development
of a C++ Binding.&quot;

You'll also need to write a somewhat longer blurb, which will
eventually be used on the SIG's web page.  Here, for example, is the
info page for the `meta SIG </community/sigs/current/meta-sig/>`_.  Include as much
information as you feel is necessary, but try to keep it fairly brief
and concise.

You should discuss your proposed sig on the `meta SIG </community/sigs/current/meta-sig/>`_
mailing list.  Introduce your proposal, and include a draft of both
blurbs, so we can all discuss the merits of the new SIG.  If the
consensus is to create it, we'll set up the necessary infrastructure
and communicate with you about the details.