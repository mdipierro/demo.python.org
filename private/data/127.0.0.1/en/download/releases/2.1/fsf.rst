FSF response to the Python 2.1 license
======================================

Today, I received the following email from Eben Moglen, the Free
Software Foundation's attorney.  (See also a `postscript <#postscript>`_.)

.. code-block::

    Subject: Re: Python 1.6.1 and GPL compatibility
    From: Eben Moglen <;moglen@columbia.edu>
    To: Guido van Rossum <;guido@digicool.com>
    Cc: "Bradley M. Kuhn" <;bkuhn@gnu.org>, rms@gnu.org
    Date: Thu, 19 Apr 2001 07:44:11 -0400 (EDT)

    On Wednesday, 18 April 2001, Guido van Rossum wrote:

      Please get me an answer before Thursday's over.  I can't hold up my
      response to the Slashdot questions much longer.

    What follows is our official response to the 2.1 license.

    The removal of the acceptance ceremony takes care of the primary
    dissonance between GPL and the Python 1.6.1 license (but see below).
    The other issue over which we spent much time in negotiation with CNRI
    is the applicable law provision in paragraph 7.

    The GPL doesn't use an applicable law provision.  We are concerned
    about a number of problems that can arise.  You see the simplest of
    them already in your license stack: one license applying the law of
    California and another the law of Virginia.  That could happen many
    times over with free software projects, with each module and some
    patches within the modules treated under different rules of law, which
    would create almost intolerable confusion.  It does not happen with
    proprietary software because there is a single owner, who does not
    permit derivative works.

    In addition, we need to be worried about Unfreedonia, the jurisdiction
    that treats the GPL as a nullity, or even worse interprets it to make
    code unfree.  Then anyone can receive a GPL'd program, modify it, and
    rerelease under a GPL with an Unfeedonian-law-applies clause.  We're
    screwed.

    So we have never allowed a license with a choice-of-law clause to be
    treated as fully compatible with GPL.  Virginia is the worst of all
    choices, because that state has passed the UCITA law, which adds a
    whole new range of risks and burdens in the distribution of free
    software.

    We explained all this to CNRI, but it was the other subject on which
    they were immovable.  So we settled for a clause that specifically
    exempted any GPL'd code in Python from that clause, except as it
    applied to the warranty disclaimers.  This was a kludgy solution, but
    we wanted to make a deal, and we expected to have the code ultimately
    released under a different license.

    But this situation shows why we hate doing that: you've taken over
    their language.  If we now agree that this is GPL-compatible, we'll
    have to live with it forever, because other people will copy it from
    your license.  And it still contains more risks for the future than we
    think it is wise to incur.

    So let's take paragraph 7 and reduce it to the no-joint-venture
    clause, which we also think is unnecessary, but which is harmless.  It
    would then read: 

       7. Nothing in this License Agreement shall be deemed to create any
       relationship of agency, partnership, or joint venture between PSF and
       Licensee.  This License Agreement does not grant permission to use PSF
       trademarks or trade name in a trademark sense to endorse or promote
       products or services of Licensee, or any third party.

    Now about paragraph 8.  By removing the ceremony of acceptance you
    eliminate the incompatibility with GPL, but you are still telling your
    user that installation and use of Python constitutes acceptance of
    your license.  This may or may not hold up in court, in the event that
    you ever need to enforce, but we wonder why you would want to sue
    someone who had installed and used Python with his fingers crossed
    about your license, but who never modified or redistributed it.  The
    GPL says that you don't need to accept the license, but you can't
    modify or redistribute unless you do, because nothing gives you the
    right to do those things except the license.  We strongly recommend
    that approach: it loses you nothing except the hypothetical right to
    enforce against someone you wouldn't care about anyway, and it doesn't
    commit you to claiming this sort of "implicit acceptance by use" that
    the lawyers don't believe will work, which is why they use acceptance
    ceremonies, .....

    You will notice that we're about simplifying here.  Most lawyers
    operate from caution: anything that might ever possibly help they
    throw into the license.  Every place they do business they have a
    local license adapted to the conditions there, with every little
    detail thrown in.

    We're about elegance.  We try to use the absolute minimum, because
    we're offering one license for use everywhere, giving the maximum
    amount of freedom to every user.  So the simpler things are the more
    compatible they are with our needs.

    Conclusion: in order to be "compatible" in the strict sense, we need
    paragraph 7 to remove the choice of law clause.  We would also
    recommend that paragraph 8 be changed to say that copying,
    modification or distribution constitutes acceptance of the license,
    but we don't have to have that change to agree that the license is
    fully "GPL compatible."

    I hope this helps.  If you have any further questions I can try to
    respond during the course of Thursday, but my schedule is extremely
    full.

    Best regards.

    -- 
     Eben Moglen                       voice: 212-854-8382 
     Professor of Law & Legal History    fax: 212-854-7946       moglen@
     Columbia Law School, 435 West 116th Street, NYC 10027     columbia.edu
     General Counsel, Free Software Foundation   http://moglen.law.columbia.edu

Postscript
----------

In accordance with the requirement above, the `PSF </psf/>`_ board has decided to change the license, by
replacing the original paragraph 7 with the paragraph 7 suggested in
Eben Moglen's letter above.  The first release with such a
GPL-compatible license is `Python 2.0.1 <../../2.0.1/>`_; Python
2.1.1 will soon follow.  *(Added 14-June-2001)*