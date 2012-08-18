Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. 
It is a thin object-oriented layer on top of `Tcl/Tk 
<http://tcl.sourceforge.net/>`_. 

Tkinter is not the only `GuiProgramming </moin/GuiProgramming>`_ toolkit for 
Python. It is however the most commonly used one. `CameronLaird 
</moin/CameronLaird>`_ calls the yearly decision to keep TkInter "one of the 
minor traditions of the Python world." 

The Tkinter wiki: `http://tkinter.unpythonic.net/wiki/ 
<http://tkinter.unpythonic.net/wiki/>`_ 

Tkinter Documentation
---------------------

- `An Introduction To Tkinter  <http://www.pythonware.com/library/tkinter/introduction/>`_ (online) by  `FredrikLundh </moin/FredrikLundh>`_
- `Tkinter reference: a GUI for Python  <http://infohost.nmt.edu/tcc/help/pubs/tkinter/>`_ (online or `pdf  <http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf>`_) by John W.  Shipman, New Mexico Tech Computer Center
- `Python and Tkinter Programming  <http://www.amazon.com/exec/obidos/ISBN=1884777813>`_ by John Grayson (see also  `GuiBooks </moin/GuiBooks>`_). This book just recently came back into print on  demand, see the publisher's website `http://www.manning.com/grayson  <http://www.manning.com/grayson>`_
- `Tips for Python/Tk <http://modcopy.sourceforge.net/tips.html>`_ by Andreas  Balogh (about useful documentation, GUI builders and tips using Grid and HList  widgets)
- `Tkinter Summary  <http://www.astro.washington.edu/users/rowen/TkinterSummary.html>`_
- `Tkinter Folklore  <http://www.astro.washington.edu/users/rowen/ROTKFolklore.html>`_

David `McNab </moin/McNab>`_ recommended the latter two as particularly "pythonic" in not insisting that readers think in Tcl. - `Thinking in Tkinter <http://www.ferg.org/thinking_in_tkinter/index.html>`_ is  an introduction to some basic Tkinter programming concepts.
- `Graphical User Interfaces with Tk <http://docs.python.org/lib/tkinter.html>`_,  a chapter from the `Python Library Reference  <http://docs.python.org/lib/lib.html>`_..
- `Online Tcl/Tk Manual Pages <http://www.tcl.tk/man/>`_ - the official man pages  at the Tcl Developer Xchange.
- The New Mexico Institute of Mining and Technology created its own Tkinter  manual. It is available in `HTML <http://www.nmt.edu/tcc/help/pubs/tkinter/>`_  and `PDF <http://www.nmt.edu/tcc/help/pubs/tkinter.pdf>`_.
- `TkDocs Tutorial <http://www.tkdocs.com/tutorial/index.html>`_, covers Python  3+ and Tk8.5, with easy to follow examples.
- The *Tkinter Life Preserver*, by Matt Conway is still useful, though way out of  date. It's the only document that explains how to read the Tcl/Tk manuals and  translate the information there to Tkinter calls. `HTML version  <http://www6.uniovi.es/python/doc/life-preserver/index.html>`_, converted by  Ken Manheimer.
- The source: when all else fails: Read The Source, Luke! - *Demo/tkinter/* in the Python source distribution. - This contains many helpful  examples, including updated versions of Matt Conway's examples. - *Lib/lib-tk/Tkinter.py* in any Python distribution.
- Other prominent Tcl/Tk sites: - `Tcl Developer Xchange <http://www.tcl.tk>`_ - `Tcl project at SourceForge <http://sourceforge.net/projects/tcl>`_ - `Tcl foundry at SourceForge  <http://sourceforge.net/foundry/tcl-foundry>`_(2008/09/07 lost link?)
- Other Tcl/Tk related links: - `Simple toolsuite to create Tkinter GUIs on the fly from JSON files  <http://pypi.python.org/pypi/pytkgen>`_

Tkinter Extensions
------------------

- `Pmw </moin/Pmw>`_ (`http://pmw.sourceforge.net <http://pmw.sourceforge.net>`_)
- `Tix </moin/Tix>`_ (`http://www.python.org/doc/current/lib/module-Tix.html  <http://www.python.org/doc/current/lib/module-Tix.html>`_)
- `TkZinc </moin/TkZinc>`_ (`http://www.tkzinc.org <http://www.tkzinc.org>`_)
- `Tkinter3000 </moin/Tkinter3000>`_ (`http://tkinter.effbot.org  <http://tkinter.effbot.org>`_)
- `How Tkinter can exploit Tcl/Tk extensions  </moin/How%20Tkinter%20can%20exploit%20Tcl/Tk%20extensions>`_

Comments
--------

`MythDebunking </moin/MythDebunking>`_: *TkInter is ugly on Windows* 
(`http://wiki.tcl.tk/8646 <http://wiki.tcl.tk/8646>`_) 

Checking your Tkinter support
-----------------------------

A good way to systematically check whether your Tkinter support is working is 
the following. 

Enter an interactive Python interpreter in a shell on an X console. 

Step 1 - can _tkinter be imported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try the following command at the Python prompt: 

``>>> import _tkinter # with underscore, and lowercase 't'`` - If it works, go to step 2.
- If it fails with "No module named _tkinter", your Python configuration needs to be modified to include this module (which is an extension module implemented in C). Do **not** edit Modules/Setup (it is out of date). You may have to install Tcl and Tk (when using RPM, install the -devel RPMs as well) and/or edit the setup.py script to point to the right locations where Tcl/Tk is installed. If you install Tcl/Tk in the default locations, simply rerunning "make" should build the _tkinter extension.
- If it fails with an error from the dynamic linker, see above (for Unix, check for a header/library file mismatch; for Windows, check that the TCL/TK DLLs can be found).

Step 2 - can Tkinter be imported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try the correct command for your version at the Python prompt: 

``>>> import Tkinter # no underscore, uppercase 'T' for versions prior 
to V3.0`` 

``>>> import tkinter # no underscore, lowercase 't' for V3.0 and later`` - If it works, go to step 3.
- If it fails with "No module named Tkinter", your Python configuration need to be changed to include the directory that contains Tkinter.py in its default module search path. You have probably forgotten to define TKPATH in the Modules/Setup file. A temporary workaround would be to find that directory and add it to your PYTHONPATH environment variable. It is the subdirectory named "lib-tk" of the Python library directory (when using Python 1.4 or before, it is named "tkinter").

Step 3 - does Tkinter work?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try the correct command for your Python version at the Python prompt: 

``>>> Tkinter._test() # note underscore in _test and uppercase 'T' for 
versions prior to V3.0`` 

``>>> tkinter._test() # note underscore in _test and lowercase 'T' for V3.0 and later`` - This should pop up a small window with two buttons. Clicking the "Quit" button makes it go away and the command return. If this works, you're all set. (When running this test on Windows, from Python run in a MS-DOS console, the new window somehow often pops up *under* the console window. Move it aside or locate the Tk window in the Taskbar.)
- If this doesn't work, study the error message you get; if you can't see how to  fix the problem, `ask for help <news:comp.lang.python>`_.