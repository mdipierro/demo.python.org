**MISSING**
**MISSING**

Acqutek Uses Python to Control CD/DVD Packaging Hardware
========================================================

**MISSING**
**MISSING**
**Category:**  Business

**Keywords:**  real time, real-time, manufacturing, embedded, simulation, pygame, swig, cx_freeze

**Title:**  Acqutek Uses Python to Control CD/DVD Packaging Hardware

**Author:**   Jau-Ann Chen

**Date:**   2006/10/23 13:00:00

**Web site:**  `http://www.acqu.com <http://www.acqu.com>`_

**Summary:**  Python keeps up to speed with a real-time hardware control application for counting and packaging CDs and DVDs

**Logo:**  .. image:: /files/success/acqutek/acqutek-logo.gif    :alt: /files/success/acqutek/acqutek-logo.gif

Introduction
------------

This story is about applying Python in the automated CD/DVD disc packaging
industry. In the wholesale market, CD/DVD discs are sold in units of 10, 20 or
50 in one shrink-wrapped bulk package. Counting out stacks of discs for these
packages is labor-intensive and requires several steps to accomplish:

    - picking up an estimated number of discs from a large stack,

    - verifying the correctness of the number of discs using a disc counter,

    - adding or removing discs to meet the required number, and

    - sending the disks to a packaging machine

To make the packaging process cost effective, an automatic CD/DVD disc
partitioner is used to carry out the above steps.

`Acqutek Corporation <http://www.acqu.com>`_ was contracted by `Micro Image Precision Co. Ltd <http://www.micro-image.com.tw>`_ to
develop the control software for this partitioner machine. The project was time
critical, with less than 4 months available to complete the work.  Furthermore,
no hard specification was available at first, and the requirements changed from
time to time with the concurrently evolving mechanical design of the partitioner.

To satisfy the customer's needs and manage the dynamic requirements of the
project, we needed a quick and flexible way to develop the software for the
system. After surveying the available technologies, we settled on Python. The
interactive nature of this object oriented language, its suitability for rapid
prototyping, and its extensive standard libraries made it ideal for a project
with rapidly changing requirements.

Hardware of the CD/DVD Disc Partitioner
---------------------------------------

The CD/DVD disc partitioner, designed by Micro Image Precision Co, is composed
of six disc counting and picking machines. Each of these can pick up a fixed
number of disks from an input spindle, move the disks forward, and release
them on an empty spindle. The six spindles are moved among the disc counters
on a conveyor that brings them to the point where they are fed to the
packaging machine.

.. image:: /files/success/acqutek/system2-web.jpg
   :alt: Overview of CD/DVD partitioner

*The components of the CD/DVD disc partitioner where green disks represent
the air cylinders that are used to hold spindles stationary while the
conveyor moves continuously beneath them* `Zoom in </files/success/acqutek/system2.jpg>`_

.. image:: /files/success/acqutek/PICT0002-web.jpg
   :alt: Front of CD/CVD partitioner

*The front of the CD/DVD disc partitioner* `Zoom in 
</files/success/acqutek/PICT0002.jpg>`_

.. image:: /files/success/acqutek/PICT0006-web.jpg
   :alt: Side of CD/CVD partitioner with touch screen

*The side of the CD/DVD disc partitioner.  The touch screen control panel
is in the upper left corner* `Zoom in </files/success/acqutek/PICT0006.jpg>`_

The main computer communicates with the six CD/DVD disc partitioners through
RS-485 connections and controls the air cylinders on the conveyor through
digital I/O buses.

Control Software Architecture
-----------------------------

The controller software is divided into five major components: The central
control logic, the error handler, the digital I/O interface, the RS-485
serial communicator, and the graphical user interface (GUI).

The control logic component is in charge of controlling, coordinating, and
monitoring the production processes. Depending on events from the GUI and
signals from other parts of machine, it sends a sequence of commands to the
counting and picking machines and the air cylinders on the conveyor.

The digital I/O interface provides various methods for the control logic to
access the status of sensors, and control the up and down movement of the air
cylinders on the conveyor.

The RS-485 serial communicator provides methods for sending commands to and
receiving responses from the disc partitioner.

The GUI component provides user interfaces for operators to set, test, debug,
start, pause, and stop the machine.

.. image:: /files/success/acqutek/ML500-Main-web.jpg
   :alt: Main entry menu

*Main Entry Menu. This is the first menu shown on the screen of the touch panel after
the system boots up.* `Zoom in </files/success/acqutek/ML500-Main.jpg>`_

.. image:: /files/success/acqutek/ML500-SetOperationMode-web.jpg
   :alt: Setup operation mode menu

*Setup Operation Mode Menu. Operators can use this control panel to set up the
number of discs to select for each package.* `Zoom in </files/success/acqutek/ML500-SetOperationMode.jpg>`_

.. image:: /files/success/acqutek/ML500-Operation-web.jpg
   :alt: Operation menu

*Operation Menu. Operators can use this panel to initialize, run, pause,
reset, and clear the conveyor. The panel also display any warnings or error messages
sent from other parts of machine.* `Zoom in </files/success/acqutek/ML500-Operation.jpg>`_

.. image:: /files/success/acqutek/ML500-EngineerMode-web.jpg
   :alt: Engineer mode

*Engineer Mode. Engineers can use this panel to get the status of each
sensor, to control air cylinders and the conveyor motor, and send commands to a
counting and picking machine for maintenance or problem-solving purposes.*
`Zoom in </files/success/acqutek/ML500-EngineerMode.jpg>`_

Implementation
--------------

Python's `threading <http://wingware.com/psupport/python-manual/2.5/lib/module-threading.html>`_ module proved to be a very important tool in handling
concurrent processes in the control logic. Threads are used to simultaneously
monitor the production process, watch events from the GUI, and detect
error messages coming in from other parts of the machine.

The digital I/O interface and RS-485 serial communicator were libraries written
in C.  `SWIG <http://www.swig.org/>`_ was used to quickly make these callable from Python code.

The GUI components of the CD/DVD partitioner were built using `Tkinter <http://wingware.com/psupport/python-manual/2.5/lib/module-Tkinter.html>`_,
which provides a simple but very reliable GUI development toolkit.

`cx_Freeze <http://www.cxtools.net/default.aspx?nav=cxfrlb>`_ was used to package up the Python control software into an
executable.

At the hardware level, a ``JUKI-740E`` (K6 400MHz CPU and 64M RAM) CPU card is
used for the main computer. The OS is ``Linux kernel 2.4.18`` and the system
software includes `BusyBox <http://www.busybox.net/>`_, minimized X11 window server, touch panel
daemon, and network driver.

All of these fit onto a 64MB flash memory stick. While it is possible to reduce
the root file system size further, it was not necessary for this project.

Simulator
---------

A simulator was developed in the early stages of the project, before the
actual machine was available. This provided the developer with a graphical
animation of the movement of the spindles, air cylinders, and the status of
the sensors.

The simulator allowed the software developer to start building the control
software before the hardware design and assembly were complete. It also acts
as a convenient way to debug and stress test the control software.

.. image:: /files/success/acqutek/Simulation-web.png
   :alt: ML500 simulator

*ML500 simulator. A red disk represents a spindle with discs loaded.
A green disk represents an empty spindle waiting to be loaded.
A small blue vertical bar represents an air cylinder and a small red
square represents a sensor used to detect position of the spindles.
The black and green squares represent the signals; black means the signal
is off and green means the signal is on.* `Zoom in </files/success/acqutek/Simulation.png>`_

The graphical animation displayed by the simulator was built with the
`pygame <http://www.pygame.org/news.html>`_ module. The simulator proved to be very realistic; code running on
on it can be uploaded to the main computer with very little modification. Only
the simulated I/O module is replaced by the real I/O module.

Conclusion
----------

The control software of the CD/DVD disc partitioner took one developer about 4
months to complete. The software development process was almost parallel with
the hardware development process. At the end of the project, the control
software passed all field tests and is running smoothly in production.

The project was developed almost 100% in Python.  This shows that Python is
not just a toy.  It is a powerful weapon for solving real problems.

There was one concern raised in the beginning of the project:  Would Python be
fast enough to deal with the real-time demand of the production process? In
the CD/DVD partitioner, Python and Linux work perfectly as long as the fastest
required response time is greater than 1 millisecond. For faster applications,
a real time OS may be required to provide sufficiently fast and precise
response times.

About the Authors
-----------------

*Jau-Ann Chen is a Linux consultant and system analyst for the automation
industry. He specializes in simulation, embedded Linux, and digital image
processing applications.*