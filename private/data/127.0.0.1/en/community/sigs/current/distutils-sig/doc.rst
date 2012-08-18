Python Distutils-SIG: Documentation
===================================

User Documents
--------------

Two documents have been written to cover the Distutils, and 
    are part of Python's standard documentation set:
    - **MISSING**   This is for end-users, system administrators, and Python           programmers who need to install third-party modules           to their existing Python installation.  It focusses on           using the Distutils, but also covers older ways of           installing Python modules and extensions.
- **MISSING**   This is for module and extension developers who want to share           their efforts with the world using the Distutils.  It covers           writing the setup script and using it to create a source           distribution and "built" (binary) distributions (thus, it's           also useful for packagers -- people turning other developer's           source distributions into built distributions for a particular           platform).

Planning, Requirements, and Design Documents
--------------------------------------------

The Distutils did not spring magically into existence one day; a
    considerable amount of forethought was required, and some of it was
    even written down.  In roughly chronological order:
    - summary of the Developer's Day           session at IPC7 (the Seventh International Python           Conference, November 1998)
- `requirements overview <requirements/>`_
- `tasks and roles <tasks/>`_ involved in           the Distutils
- `proposed user interface <interface/>`_--mainly           of historical interest now that the code exists and is           documented in **MISSING**,           but I can never throw anything away
- `proposed design <design/>`_--also mainly of           historical interest; superseded by the IPC8 paper (below) and,            of course, the actual code

IPC8 Paper/Presentation
-----------------------

A the Eighth International Python Conference (January 2000), I
    gave a talk on the Distutils and published a paper in the conference
    proceedings.  The paper is available as:
    - `HTML </files/sigs/ipc8_paper.html>`_
- `compressed PDF </files/sigs/ipc8_paper.pdf.gz>`_
- `compressed PostScript </files/sigs/ipc8_paper.ps.gz>`_

    I updated the paper a bit and submitted it to the
    `Software Carpentry <http://software-carpentry.codesourcery.com/>`_
    competition; you might want to read the
    `updated version of the paper </files/sigs/sc_submission.html>`_
    instead.

You can also download the slides from my presentation.  I haven't
    figured out how to get Applixware to generate HTML from the slides
    (grumble), so for now you can download the slides for:
    - `Applix Presents </files/sigs/ipc8_talk.ag.gz>`_ (compressed)
- `Microsoft PowerPoint </files/sigs/ipc8_talk.ppt.gz>`_ (compressed)