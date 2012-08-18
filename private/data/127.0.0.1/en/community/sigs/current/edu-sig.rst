EDU-SIG: Python in Education
----------------------------

More and more, Python is `making inroads <http://wiki.python.org/moin/SchoolsUsingPython>`_ at all levels in education.
Python offers an interactive environment in
which to explore procedural, functional and object oriented approaches to
problem solving.  Its high level data structures and clear syntax make it
an ideal first language, while the large number of existing libraries
make it suitable to tackle almost any programming tasks.

Edu-sig, through its `mailing list <http://www.python.org/mailman/listinfo/edu-sig>`_, provides an
informal venue for comparing notes and discussing future
possibilities for Python in education.  Its origins trace to Guido van
Rossum's pioneering `Computer Programming for Everybody (CP4E) </doc/essays/cp4e/>`_, a grant
proposal accepted by DARPA, and which provided a modicum of funding in 1999.

Membership includes, but is not limited to, educators using Python in their
courses, independent developers, and authors of educational materials.
Discussion focuses on Python use at all levels, from beginning to advanced
applications.

Python 2 or Python 3 ?
----------------------

Recently, a new version of Python (3) was introduced.  This new version
has some small but significant changes from the previous one.  The most
visible change for beginners is that **print** which used to be a Python
keyword

.. code-block::

    >>> print &quot;Hello World!&quot;   # for Python 2

is now a function: 

.. code-block::

    >>> print(&quot;Hello World!&quot;)   # for Python 3

As a result of the changes, programs written for Python 2 are likely to
be incompatible with Python 3 (and vice-versa).  Some of you may have
not control over which Python version is made available to the students.
If that is the case, you should not despair too much if you and your students
do not have access to the best/latest version of Python: Python is a fantastic
choice as a first language and
the relatively minor changes between versions do not change this fact.

**If** you have some control over which version of Python is made available
to the students, then you have a choice to make.  In this case, and
as a **very subjective opinion**, we would like to offer the following:

- Use Python 3, and more specifically version 3.1, if you only plan to teach Python as an introductory language (say in a CS-1 course), making use **only** of modules included in the standard distribution. Alternatively, if you teach Python in languages other than English, where non-ascii characters could be put to good use in writing identifiers, then Python 3 should definitely be your choice.

- Use Python 2, and more specifically version 2.6, if you think you might be using third-party modules not included in the standard Python distribution, or if you are not familiar with Python (in which case you may not yet realise that you might need some third-party modules.)

- Consider the possibility of teaching both Python 2 and 3. If you are teaching beginners, the only significant differences are the print statement/function, the integer division and possibly the input()/raw_input() changes... which you can point out as you go along. Of course, you will have to decide on a common version to install for everyone to use.

Resources
---------

- `Mailing lists <#mailing-lists>`_

- `Free books <#free-books>`_

- `Textbooks <#textbooks>`_

- `Learning environments <#learning-environments>`_

- `Videos <#videos>`_

- `Specialized packages <#specialized-packages>`_

- `Academic papers <#academic-papers>`_

- `Game time! <#game-time>`_

- `Miscellaneous <#miscellaneous>`_

- `SIG administrivia <#sig-administrivia>`_

Mailing lists, etc.
-------------------

As mentioned above, the Edu-Sig community has its own `mailing list <http://www.python.org/mailman/listinfo/edu-sig>`_.
Two other mailing lists are of potential interest to educators: the
`python tutor <http://mail.python.org/mailman/listinfo/tutor>`_ and the general `python-list <http://mail.python.org/mailman/listinfo/python-list>`_.  All three are available
in a `searchable archive <http://aspn.activestate.com/ASPN/Python/Mail/>`_ on
the `ActiveState site <http://aspn.activestate.com>`_
which is also hosting the
famous `Python Cookbook <http://aspn.activestate.com/ASPN/Cookbook/Python/>`_.
The `python tutor <http://mail.python.org/mailman/listinfo/tutor>`_ mailing list is useful to beginners learning the language
and looking for answers to their programming problems; educators are welcome
to join as volunteers; the `edu-sig mailing list <http://www.python.org/mailman/listinfo/edu-sig>`_ is more for discussions
about uses of Python in educational settings.

Free books and tutorials for educators
--------------------------------------

There are a number of freely available tutorials for Python.  For example,
there is a collection of `Beginner's Guide to Python <http://wiki.python.org/moin/BeginnersGuide/NonProgrammers>`_ available on the
Python wiki.  In addition, the following may be of particular interest
to educators:

- `pyBiblio <http://www.ibiblio.org/obp/pyBiblio>`_ is a site for teachers using Python to teach computer science and/or programming skills. It includes links to the free book *How to Think Like a Computer Scientist Learning with Python* as well as links to `Gasp lessons <http://www.openbookproject.net/pybiblio/gasp/>`_ adapted from `LiveWires <http://www.livewires.org.uk/python/>`_.   An Introduction to Programming by Eric Rollins is an example of how this open source resource may serve as a basis for a specific course.

- `Think Python <http://www.greenteapress.com/thinkpython/thinkpython.html>`_, by Allen B. Downey, is a substantially revised version of *How to Think Like a Computer Scientist Learning with Python*.  It is available for free in various formats; printed copies can be purchased as well.

- `Python for Informatics: Exploring Information <http://www.py4inf.com/>`_, by Charles Severance, is another book derived from the freely available *How to Think Like a Computer Scientist Learning with Python* mentioned above. As of January 2010, this book is only partially completed, with chapters available freely as pdf files.

- `Snake Wrangling for Kids <http://www.briggs.net.nz/log/writing/snake-wrangling-for-kids/>`_ is a free book written by Jason R. Briggs.

- `Dave Kuhlman's free book <http://www.rexx.com/~dkuhlman/#a-python-book>`_ and other collection of tutorials is also a very good resource for educators.

- `Andrew Harrington's hands-on tutorial <http://webpages.cs.luc.edu/~anh/python/hands-on>`_ is suitable for high school and university-level CS-0 students. `Dr. Harrington <http://webpages.cs.luc.edu/~anh/>`_ teaches at Loyola University Chicago.

Textbooks and other non-free books
----------------------------------

While there are a number of **free** books and tutorials available, some
people prefer to have an actual copy on paper.
If you are among this group, you might be surprised to learn that there are
close to one hundred books that have been written about Python programming.
Here, we will focus only on a subset that are of potential interest for educators
who teach introductory courses in programming.  More books can
be found `here <http://wiki.python.org/moin/PythonBooks>`_
and `here <http://wiki.python.org/moin/IntroductoryBooks>`_, or by
doing an internet search.

For children, young and old: 

- `Python Programming for the Absolute Beginner <http://www.amazon.com/Python-Programming-Absolute-Beginner-Second/dp/1598631128>`_ by Michael Dawson was one of the first books written for this audience and remains one of the most popular.

- `Hello World! Computer Programming for Kids and Other Beginners <http://cp4k.blogspot.com/>`_ by Warren Sande is just like the title says.

- `Computer Programming is Fun! <http://www.handysoftware.com/cpif/>`_ by David Handy has been written with young children in mind.

University-level textbooks are also available: 

- `Python Programming: An Introduction to Computer Science <http://www.fbeedle.com/99-6.html>`_ by John Zelle is a book designed for a CS-1 course. `Dr. Zelle <http://mcsp.wartburg.edu/zelle/>`_ teaches at Wartburg College.

- `Data Structures and Algorithms Using Python and C++ <http://www.fbeedle.com/2335.html>`_ by David M. Reed and John Zelle is a book designed for a CS-2 course. `Dr. Reed <http://capital2.capital.edu/faculty/dreed/Sites/Capital/Home.html>`_ teaches at Capital University and `Dr. Zelle <http://mcsp.wartburg.edu/zelle/>`_ teaches at Wartburg College.

- `Object-Oriented Programming in Python <http://prenhall.com/goldwasser/>`_ by Michael H. Goldwasser and David Letscher is a book designed for a CS-1 course. Drs. Goldwasser and Letscher teach at Saint Louis University. They have written a free `Object-Oriented Graphics Package <http://www.cs1graphics.org/>`_ as supporting material for their textbook.

- `Practical Programming: An Introduction to Computer Science Using Python <http://pragprog.com/titles/gwpy/practical-programming>`_ by Jennifer Campbell, Paul Gries, Jason Montojo and Greg Wilson is a textbook designed for a CS-1 course.  All four authors are associated with the University of Toronto.

- `Python Programming in Context <http://www.jbpub.com/catalog/9780763746025/>`_ by Bradley N. Miller and David L. Ranum is a book designed for a CS-1 course. Drs. Miller and Ranum teach at Luther College.

- `Python First: Introduction to Computing with Python <http://studypack.com/comp/course/view.php?id=232>`_ by Atanas Radenski is not a traditional textbook but rather a digital pack (textbook, lab manual, quizzes) designed for a CS-1 course. `Dr. Radenski <http://www1.chapman.edu/~radenski/>`_ teaches at Chapman University.

- `The Practice of Computing Using Python <http://www.pearsonhighered.com/educator/product/Practice-of-Computing-using-Python-The/9780136110675.page>`_ by Bill Punch and Rich Enbody is a book that teaches the concepts of CS1 using the Python language. Educational material includes a full set of powerpoint slides, lab exercises, python projects and solutions to the more than 600 exercises in the book. Punch and Enbody are both faculty in the computer science and engineering at Michigan State University.

- A book with a very different approach is `Mathematics for the Digital Age and Programming in Python <http://www.skylit.com/mathandpython.html>`_ by Maria Litvin and Gary Litvin. According to the description on the website *It offers a unique blend of mathematics and programming, designed to give students in introductory computer science courses an appreciation for the rigorous mathematics relevant to computing, as well as practical skills for writing programs.*

- `Python Scripting for Computational Science <http://www.springer.com/mathematics/numerical+and+computational+mathematics/book/978-3-540-73915-9>`_ by Dr. Hans Petter Langtangen teaches tools and programming concepts that are particularly useful for doing science. The `homepage <http://www.ifi.uio.no/~hpl/scripting/all-nosplit/>`_ for the book contains an associated and rather complete set of slides.

- Dr. Hans Petter Langtangen wrote a second book, `A Primer on Scientific Programming with Python <http://www.springer.com/mathematics/numerical+and+computational+mathematics/book/978-3-642-18365-2>`_. In this book, examples from mathematics, statistics, physics, biology, and finance are used. The book teaches &quot;Matlab-style&quot; and procedural programming as well as object-oriented programming. It is also available from `Amazon <http://www.amazon.com/Scientific-Programming-Computational-Science-Engineering/dp/3642024742/ref=sr_1_2?ie=UTF8&s=books&qid=1252223300&sr=8-2>`_.

Learning environments
---------------------

Since Python is an interpreted language, all one needs to start programming
is a terminal window.  However, for your students, this would not be
the friendliest environment; instead,
we recommend that you use something like `IDLE </idle/>`_ (which stands
for Integrated DeveLopment Environment), which is included in the installation
Python files on any platform that supports Tcl, including Windows.

As for yourself, if you prefer programming directly from a terminal window,
a better choice than the default interpreter might
be `IPython <http://ipython.scipy.org/>`_.

In addition to IDLE, there are a number of third party tools which you can find out
by referring to the `Python Editors Wiki <http://wiki.python.org/moin/PythonEditors>`_ and the
`Python Integrated Development Environments Wiki <http://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`_.

There are also a few other non-traditional Python learning environments that
you may wish to consider.  First, some general purpose environments - all three
work from a browser:

- `Crunchy <http://code.google.com/p/crunchy/>`_ is a Python program that can transform an otherwise static html tutorial into an interactive Python session within a browser.  The basic features of an early version of Crunchy are demonstrated in `this screencast. <http://showmedo.com/videos/video?name=1430000&fromSeriesID=143>`_

- A new &quot;Mathematica-like&quot; environment for Python is `Codenode <http://codenode.org/>`_. You may want to `try it yourself <http://live.codenode.org/accounts/login/?next=/bookshelf/>`_.

- `PyKata <http://pykata.org/>`_ is a new online environment designed as a teaching aid for Python.  It includes a small, but growing number of programming exercises that students can try on their own and get immediate feedback.  Educators are invited to contribute their own exercises.

Some other notables, with more restricted goals, are the following: 

- `Pyro <http://emergent.brynmawr.edu/%7Edblank/pyro/>`_ is a Python programming environment for easily exploring advanced topics in artificial intelligence and robotics.

- `GvR <http://gvr.sourceforge.net/>`_, or Guido van Robot, strives to emulate the original *Karel the Robot* created by Richard Pattis. It uses an indentation-based Python-like language and about 20 lessons designed to teach programming concepts. An `online demo is available. <http://gvr-online.appspot.com/>`_

- `RUR-PLE <http://rur-ple.sourceforge.net/>`_ is a Python learning environment that includes an editor, a Python shell and, more prominently, a Karel the Robot clone that is programmable using Python syntax, using either procedural commands [e.g. move()] or an object-oriented approach [e.g. robot.move()]. It includes approximately 40 lessons. RUR-PLE was inspired from `Guido van Robot <http://gvr.sourceforge.net/>`_.

- Python's `turtle module <http://docs.python.org/library/turtle.html>`_ is not a learning environment as such, but it has been completely revamped for Python 2.6 and above and is worth checking out.  Examples are included in the source distribution (along with a demoViewer program, which also serves as an example on how to embed turtle graphics into a Tkinter application.)  For those that have older version of Python installed (2.3, 2.4 or 2.5), a suitable version of the turtle module can be `found here. <http://svn.python.org/view/python/trunk/Lib/lib-tk/>`_, with the `examples here. <http://svn.python.org/view/python/trunk/Lib/lib-tk/>`_ A `video of the Pycon 2009 talk demonstrating the turtle module <http://blip.tv/file/1947495>`_ is available.

Videos
------

There is a growing body of podcasts, screencasts and video presentations
for the Python community, many of which may be of interest to educators.
For more details, please consult the
`Audio/Video Instructional Materials for Python </doc/av/>`_

Specialized packages
--------------------

Given the large number of `modules <http://docs.python.org/modindex.html>`_ included in the Python distribution,
it is often said that Python comes with batteries included.  If the standard
distribution does not include what you need, you may want to consult the
`Python Package Index <http://pypi.python.org/pypi>`_ which is a repository that includes close to 7000
additional packages.

The following represent just a small sample of what is available. 

- `NumPy <http://numpy.scipy.org/>`_ is the fundamental package needed for scientific computing with Python. It contains:- a powerful N-dimensional array object  - sophisticated broadcasting functions  - basic linear algebra functions  - basic Fourier transforms  - sophisticated random number capabilities  - tools for integrating Fortran code.  - tools for integrating C/C++ code.

- `SciPy <http://www.scipy.org/>`_ (pronounced &quot;Sigh Pie&quot;) is open-source software for mathematics, science, and engineering. The SciPy library depends on NumPy, which provides convenient and fast N-dimensional array manipulation. The SciPy library is built to work with NumPy arrays, and provides many user-friendly and efficient numerical routines such as routines for numerical integration and optimization. Together, they run on all popular operating systems, are quick to install, and are free of charge. NumPy and SciPy are easy to use, but powerful enough to be depended upon by some of the world's leading scientists and engineers. If you need to manipulate numbers on a computer and display or publish the results, give SciPy a try!

- `matplotlib <http://matplotlib.sourceforge.net/>`_ is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell (ala matlab or mathematica), web application servers, and six graphical user interface toolkits. matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc, with just a few lines of code.

- `PIL <http://www.pythonware.com/products/pil/>`_, the Python Imaging Library adds image processing capabilities to your Python interpreter. This library supports many file formats, and provides powerful image processing and graphics capabilities.

- `OpenOpt <http://openopt.org/Welcome>`_ is a free optimization framework which builds upon Numpy. In addition to various numerical optimization packages, it includes:- FuncDesigner - a tool to rapidly build functions over variables/arrays and get their derivatives via automatic differentiation. Also, one can perform integration, interpolation, solve systems of linear/nonlinear/ODE equations and numerical optimization problems coded in FuncDesigner by OpenOpt.  - DerApproximator - a tool to get (or check user-supplied) derivatives via finite-difference approximation.  - SpaceFuncs - a tool for 2D, 3D, N-dimensional geometric modeling with possibilities of parametrized calculations, numerical optimization and solving systems of geometrical equations.

- `VPython <http://vpython.org>`_ makes it easy to create navigable 3D displays and animations, even for those with limited programming experience.  It includes a modified version of IDLE.

- `ReportLab <http://www.reportlab.com/>`_ gives Python programs the power to output directly in Adobe's PDF format. The open source version is fully functional in the hands of a Python programmer.  Useful for publishing course materials.

- `SymPy <http://code.google.com/p/sympy/>`_ is a Python library for symbolic mathematics. It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible. SymPy is written entirely in Python and does not require any external libraries.

- `Sage <http://sagemath.org/>`_ is not a Python package but offers an environment showcasing Python as a programming language. It is a free open-source mathematics software system licensed under the GPL. It combines the power of many existing open-source packages into a common Python-based interface. Sage's mission is to create a viable free open source alternative to Magma, Maple, Mathematica and Matlab.

- `Blender <http://www.blender3d.com/>`_ is a cross-platform 3D modeling suite, offering modeling, animation, interactive creation and playback. Blender is not a Python package but it does use Python for scripting support.

- An `Object-Oriented Graphics Package <http://www.cs1graphics.org/>`_ has been written by Michael H. Goldwasser and David Letscher to use in conjuction with their textbook (referenced above).

Academic papers
---------------

A number of academic papers have been written about using Python as
a programming language.  They include the following:

- Drs. Fotis Georgatos's MSc thesis, How applicable is Python as first computer language for teaching programming in a pre-university educational environment, from a teacher's point of view?

- `Using Python in a High School Computer Science Program </workshops/2000-01/proceedings/papers/elkner/pyYHS.html>`_ documents experiences with Python in the classroom, reported at the 8th International Python Conference. By Jeff Elkner. (See also an `interview <http://www.oreilly.com/frank/elkner_0300.html>`_ with Jeff by Frank Willison for O'Reilly.)

- Dr. John Zelle of Wartburg College advocates using Python as a first language, and has a few papers on that topic at his `web site <http://mcsp.wartburg.edu/zelle/python/>`_.

- John Miller's PhD dissertation, `Promoting Computer Literacy Through Programming Python </files/miller-dissertation.pdf>`_ (1.37 MB), looks at the issues around teaching with Python, and explores some of the threads taken up on `edu-sig <http://www.python.org/mailman/listinfo/edu-sig>`_.

- Dr. Atanas Radenski has written a paper entitled &quot;Python First&quot;: A Lab-Based Digital Introduction to Computer Science which describes a positive experience when switching from Java to Python as a language for CS1 courses.

- Dr. Michael H. Goldwasser and Dr. David Letscher have written a paper entitled Teaching an Object-Oriented CS1 - with Python which has been published in the *Proceedings of the 13th Annual Conference on Innovation and Technology in Computer Science* (ITiCSE) in June 2008.  They have also written `A Graphics Package for the First Day and Beyond <http://cs.slu.edu/~goldwasser/publications/SIGCSE2009_Abstract.html>`_, published in the *Proceedings of the 40th Annual SIGCSE Technical Symposium on Computer Science Education* in May 2009.  (A link to the freely available graphics package is included above.)

And finally, while it is not an academic paper,
`Why Python is a great language for teaching beginners in introductory programming classes <http://www.stanford.edu/~pgbovine/python-teaching.htm>`_
by Philip Guo is certainly worth reading.

Game time!
----------

If it weren't for games, there likely would have been many fewer people
interested in programming - and much less free software developped as
a result.  Python has two well-known frameworks for making games:

- `pygame <http://pygame.org>`_ is the original and still very much active package for game development using Python. It allows Python to talk to `SDL <http://www.libsdl.org/index.php>`_, a cross-platform, multimedia library. Because it needs to be compiled for each platform and each Python version, there can be a lag when a new Python version comes along.

- `pyglet <http://pyglet.org>`_ is the newcomer, based on OpenGL.  Because it is a pure Python package, it can be used as is even when a new Python version is released (except for the Python 2 to Python 3 transition).

Miscellaneous
-------------

- `Python for secretaries <http://wiki.python.org/moin/PythonForSecretaries>`_: A resource site aimed at showing business users how to use a little bit of Python, focused entirely on helping them with their regular workaday duties.

- `Freely-reusable data <http://wiki.python.org/moin/EduSig/DataResources>`_: Instructors often have need of meanful data for constructing programming exercises.  To support this usage, many in the educational community have contributed `freely-reusable data <http://wiki.python.org/moin/EduSig/DataResources>`_ on which to build.

- `Software Carpentry <http://swc.scipy.org/>`_ by Greg Wilson is a course on software development skills for scientists and engineers.

- Kirby Urner's `CP4E resources <http://www.4dsolutions.net/ocn/cp4e.html>`_ integrate Python programming with topics in mathematics.

- `Computer Programming for Everybody </doc/essays/ppt/acm-cp4e/>`_ by Guido van Rossum, is a presentation summarizing CP4E highlights.

- `An Interview with Guido van Rossum <http://www.linuxjournal.com/articles/conversations/005.html>`_, by Phil Hugues for the *Linux Journal*, is a conversation with the creator of Python about an effort to teach Python to non-computer science students.

- `Hackers and Trackers: CP4E <http://www.oreillynet.com/pub/a/network/2000/01/31/hacktrack/index.html>`_ and `Teaching Math with Python <http://www.onlamp.com/pub/a/python/2000/10/04/pythonnews.html>`_, both by Stephen Figgins, are older articles about the beginning of the Computer Programming for Everybody initiative.

SIG administrivia
-----------------

- Subscribe to the `edu-sig mailing list <http://www.python.org/mailman/listinfo/edu-sig>`_

- Browse the `edu-sig mailing list archives <http://www.python.org/pipermail/edu-sig>`_

- Send suggestions for changes to the edu-sig list or to andre.roberge at gmail.com.