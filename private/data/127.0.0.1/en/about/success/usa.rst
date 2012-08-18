**MISSING**
**MISSING**

Python Streamlines Space Shuttle Mission Design
===============================================

**MISSING**
**MISSING**
**Category:**  Software Development, Business, Science

**Keywords:**  Rapid Application Development, User Interface, ROI Case Study, Scientifcic Programming

**Title:**  Python Streamlines Space Shuttle Mission Design

**Author:**   Daniel G. Shafer

**Summary:**  The United Space Alliance (USA) uses Python to deliver quality just-in-time engineering solutions at low cost.

**Date:**   2003/01/17 04:44:29

**Logo:**  .. image:: /files/success/usa/usa-logo.gif    :alt: /files/success/usa/usa-logo.gif

This article was previously published on `Builder.com 
<http://www.builder.com/>`_ 

Introduction
------------

Software engineers have long told their bosses and clients that they
can have software &quot;fast, cheap, or right,&quot; as long as they pick any two
of those factors. Getting all three? Forget about it!

But `United Space Alliance (USA) <http://www.unitedspacealliance.com/>`_, NASA's main shuttle support
contractor, had a mandate to provide software that meets all three
criteria. Their experience with Python told them NASA's demands were
within reach. Less than a year later, USA is nearing deployment of a
Workflow Automation System (WAS) that meets or exceeds all of NASA's
specifications.

&quot;Python allows us to tackle the complexity of programs like the WAS
without getting bogged down in the language,&quot; says Robin Friedrich,
USA's Senior Project Engineer. Friedrich conceived of the WAS project
in response to a significant gap in the way shuttle mission planning
was handling data management. &quot;Historically,&quot; Friedrich says, &quot;this
data has been communicated using paper and, more recently, data file
exchange. But both of these approaches are error-prone. Catching and
fixing errors as well as responding to frequent change requests can bog
such a system down.&quot; Complicating the issue was the challenge of
finding money to improve the flight design process in an era of
declining budgets for space activities.

&quot;Just in time&quot; provides a solution--and more problems
---------------------------------------------------------------

USA decided they needed a way to &quot;minimize data changes and the
resulting rework.&quot; The shortest route to that goal would be to shift
the design work to the end of the process so that flight
characteristics would have a good chance of already being finalized. In
other words, as Friedrich says, &quot;We decided we needed to do this data
management work 'just in time'.&quot;

A just-in-time solution, however, generally puts more stress on both
people and systems to get things right the first time because
postponing these activities to the end of the process means a loss of
scheduling elasticity.

&quot;The obvious answer,&quot; according to Friedrich, &quot;was to create a central
database repository to help guarantee consistency and to provide
historical tracking of data changes.&quot; An Oracle database was designed
to store the information, but a graphical front end to manage the
process of workflow automation was clearly an essential component of an
effective solution. &quot;We knew from experience--we do a good bit of Java
coding in our group--that using C++ or Java would have added to the
problem, not the solution,&quot; Friedrich maintains.

Python a mainstay since 1994
----------------------------

Enter Python. &quot;We'd been using Python since 1994,&quot; says Friedrich,
&quot;when I literally stumbled across Python as I was searching the pre-Web
Gopher FTP space for some help with a C++ project we were doing.&quot; Being
an inveterate systems engineer, Friedrich &quot;just had to investigate it.&quot;
He was stunned by what he discovered.

&quot;Twenty minutes after my first encounter with Python, I had downloaded
it, compiled it, and installed it on my SPARCstation. It actually
worked out of the box!&quot;

As if that weren't enough, further investigation revealed that Python
has a number of strengths, not the least of which is the fact that
&quot;things just work the first time. No other language exhibits that trait
like Python,&quot; says Friedrich.

He attributes this characteristic to three primary language features: 

    - Dynamic typing

    - Pseudocode-like syntax

    - The Python interpreter

The result? &quot;We achieve immediate functioning code so much faster in
Python than in any other language that it's staggering,&quot; says
Friedrich. &quot;Java and C++, for example, have much more baggage you have
to understand just to get a functioning piece of software.

&quot;Python also shines when it comes to code maintenance,&quot; according to
Friedrich. &quot;Without a lot of documentation, it is hard to grasp what is
going on in Java and C++ programs and even with a lot of documentation,
Perl is just hard to read and maintain.&quot; Before adopting Python,
Friedrich's team was doing a good bit of Perl scripting and C++ coding.
&quot;Python's ease of maintenance is a huge deal for any company that has
any significant amount of staff turnover at all,&quot; says Friedrich.

The team had already developed a moderately large number of C++
libraries. Because of Python's easy interface to the outside world, USA
was able to retain these libraries. &quot;We wrote a grammar-based tool that
automatically interfaced all of our C++ libraries,&quot; says Friedrich.

Another aspect of Python that Friedrich found eminently significant is
its shallow learning curve. &quot;We are always under the gun on software
projects, like everyone else,&quot; he says. &quot;But for any programmer,
picking up Python is a one-week deal because things just behave as you
expect them to, so there's less chasing your tail and far more
productivity.&quot; He contrasts that with C++ and Java, which he says takes
a good programmer weeks to grasp and months to become proficient.

Friedrich says that even the non-programming engineers at USA learned
to do Python coding quickly. &quot;We wanted to draft the coding energy of
the engineering staff, but we didn't want them to have to learn C++.
Python made the perfect 4GL programming layer for the existing C++
classes.&quot;

One coder and 17,000 lines of code later
----------------------------------------

The WAS project, which has required somewhat less than a man-year of
effort, has been coded by a single Senior Software Engineer, Charlie
Fly, who has cranked out some 17,000 source lines of code (SLOC).
Python plays the central role, managing data interactions and the task
network, as shown in Figure A.

.. image:: /files/success/usa/fig_a.gif
   :alt: Figure A: Python plays a central role in data interaction

*Figure A: Python plays a central role in data interaction.* 

In the system, user tasks communicate with a Python data server, which
in turn connects to an Oracle server via DCOracle. Using Oracle's
built-in trigger mechanism to send a message to WAS as data records are
updated, the WAS calculates which tasks are now data-ready and notifies
the appropriate user.

At the core of the design is the Task object, which stores all
information relevant to a single task in the workflow network. The end
user can view the network in a PERT-style chart layout (Figure B),
where color coding reveals at a glance which tasks are finished, which
are in process, and which have not yet been started.

.. image:: /files/success/usa/fig_b.gif
   :alt: Figure B: PERT-style layout

*Figure B: PERT-style layout* 

Two other graphical interface windows allow the user to manage the
dependencies among data items in the network (Figure C) and to view and
edit individual task details (Figure D).

.. image:: /files/success/usa/fig_c.gif
   :alt: Figure C: Interface 1

*Figure C: Interface 1* 

.. image:: /files/success/usa/fig_d.gif
   :alt: Figure D: Interface 2

*Figure D: Interface 2* 

All of the code for the UIs was also done in Python, using the popular
Tkinter library along with an open source package of supporting
modules. Tkinter is included in all standard Python installations.

&quot;USA is pleasantly surprised by how much quality software we can
deliver,&quot; Friedrich says. &quot;And each time we demonstrate success with
Python, we add a few more believers to my growing list!&quot;

About the Author
----------------

*Dan Shafer is a freelance author and sometime Python coder who hangs
out on California's central coast. He is a member of the PythonCard
Open Source development team creating a GUI-building framework for
Python applications. He makes his living as a writer and a product
development consultant. A founder and former editorial director of
Builder.com, Shafer has been part of the Web development community
almost from its inception.*