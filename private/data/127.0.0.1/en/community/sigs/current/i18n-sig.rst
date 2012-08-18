Internationalization-SIG ("i18n")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This SIG provides a forum for discussing issues relating to 
the internationalization of Python.

At the time of writing (March 2000), internationalization (henceforth 
spelled as "i18n" to save typing) features are being added
to Python.  This sig is the primary forum for discussing
those features.  Topics covered include but are not limited to:

- Unicode support and building a library of codecs
- Support for locale information, date, number and time formatting
- Frameworks for translating and localizing GUI and Web applications

Deliverables
~~~~~~~~~~~~

The immediate deliverables relate to Unicode and encoding support; the other
topics above are too general and application-specific.

- Test the new Unicode features and supplied single-byte codecs 	as soon as the Unicode patch moves into public CVS (Q2 2000)
- Assist with documentation of the new features (Q2/Q3 2000)
- Do some prototype implementations of double-byte codecs.  On the basis 	of this, determine what changes and additions, if any, are needed to the 	Unicode API at the C level support professional i18n work, 	and help get these into the core in time for 1.6. (Q2 2000)
- Thereafter, begin implementing a full set of codecs supporting  	most of the world's languages. (Q3-4 2000 and ongoing)

Background
~~~~~~~~~~

In mid-1999, Python consortium members made some strong requests
for i18n features to be added to Python.  Following discussions on the
python-dev list, CNRI contracted Marc-Andre Lemburg to add Unicode
strings and the associated changes to the Python core (based on a
running Unicode string implementation from Fredrik Lundh), and Fredrik
Lundh to develop a Unicode- based regex engine.  These tasks are
nearing completion and will shortly be released into public CVS.

The specification on which these are based can be found at `http://starship.python.net/crew/lemburg/unicode-proposal.txt <http://starship.python.net/crew/lemburg/unicode-proposal.txt >`_.
(Now also in the Python 2.0 distribution as Misc/unicode.txt.)

The proposal defines a 'codec' interface, but implementing codecs
for multi-byte languages is out of Marc-Andre's scope and will be left
to members of the SIG.

There was an i18n forum at the Eighth International Python
Conference, at which the above deliverables were agreed, and the SIG
was formed as a result of this.

Key People and Organisations Involved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you can help out n a specific way and feel you should be listed
in here, please contact Andy
Robinson with a brief bio.  This list is a first draft and omits
many key people on the sig, but you'll have to tell me about yourself
to get listed!

**MISSING**

Resources and Links
~~~~~~~~~~~~~~~~~~~

Thanks to Peter Funk for kicking off this list:

- `Martin von Loewis' "Internationalizing Python" paper <http://www.python.org/workshops/1997-10/proceedings/loewis.html>`_, given at the 6th International Python Conference, 1997, is a great place to get an overviw of the issues onvolved.
- `The Python Unicode Proposal <http://starship.python.net/crew/lemburg/unicode-proposal.txt>`_ itself.
- `Python Unicode Tutorial <http://www.reportlab.com/i18n/python_unicode_tutorial.html>`_, by Andy Robinson.
- `The Unicode Consortium <http://www.unicode.org/>`_ home page.
- `The Linux i18n project home page <http://www.li18nux.org/>`_.
- `Lessons learned from internationalizing JavaScript <http://www-4.ibm.com/software/developer/library/internationalization-support.html>`_ from an IBM researcher.
- UTF-8 and Unicode FAQ for Unix/Linux by Markus Kuhn.
- `Jim Breen's Japanese Page <http://www.dgs.monash.edu.au/~jwb/japanese.html>`_. Most things relating to the Japanese language and computing are one or two clicks away from here.
- `Basis Technologies <http://www.basistech.com>`_ make a commercial Unicode library called Rosette; their site has some good docs on the issues involved in designing these.  (There is a free DOS program called uniconv which uses this to convert files between encodings; if we could write a uniconv.py and do a mass regression test against its output, we'd have finished our job!)
- `Unilib <http://www.sybase.com/products/global/products/unilib.html>`_  from Sybase is another commercial offering which is widely used.
- `gettext <http://www.gnu.org/software/gettext/gettext.html>`_ is a GNU library for dealing with string lookups which forms the core part of their  Translation Project.
- `fintl.py <http://sourceforge.net/snippet/detail.php?type=snippet&id=100059>`_ - A pure python module for reading .mo files created by msgfmt.
- `intl.so <http://www.informatik.hu-berlin.de/~loewis/python/intl-960117.tgz>`_  - An interface to the (GNU) gettext C library.  Only useful for                intenational applications, if they are covered by GPL and will                run under Unix-Linux.
- `pygettext <http://www.python.org/~bwarsaw/software/pyware.html>`_ - Barry Warsaw's reimplementation of gettext in pure Python.  (Now also part of Python 2.0 in Tools/i18n/.)
- `Japanese codecs for Python <http://pseudo.grad.sccs.chukyo-u.ac.jp/~kajiyama/python/>`_ - made available by Tamito Kajiyama.
- Tom Emerson presented a paper at the 2002 Unicode conference in Washington, DC on a unified architecture for Asian codecs: Design and Implementation of a Suite of Chinese Transcoders for Python 2.

More contributions to the list are welcome!