Python on the Mac   
=======================================================

.. image:: /images/py_mac-sq-64.png

Python on the Mac has the ability to work with
- `Apple Events <http://pythonmac.org/wiki/AppleScript>`_ (you can use Python instead of Applescript),
- Native Mac libraries (you can call all the Objective-C libraries, including Cocoa),
- `Mac application bundles <http://pythonmac.org/wiki/py2app>`_ ("apps", written in Python),

and much much more of the Mac infrastructure!

Python comes pre-installed on Mac OS X, but due to Apple's release
cycle, it's often one or even two years old.  The overwhelming
recommendation of the "MacPython" community is to upgrade your Python
by downloading and installing a newer version from
`the Python standard release page </download/releases/>`_.

If you are using Mac OS X 10.5, see the `Leopard wiki page <http://wiki.python.org/moin/MacPython/Leopard>`_ for detailed
information.

If you're just curious...
#########################

You don't *have* to download anything.  You can run a Python interpreter by 
double-clicking on *Applications / Utilities / Terminal* (`here's a picture 
</images/terminal-in-finder.png>`_), then typing "python" into the window that 
opens up. 

You'll see a prompt that looks like this:

.. code-block::

    Python 2.3.5 (#1, Mar 20 2005, 20:38:20) 
    [GCC 3.3 20030304 (Apple Computer, Inc. build 1809)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

(On Mac OS X 10.3 (Panther), it will say "Python 2.3.0", an older version.)

Try typing "2 + 2" and hit "Enter":

.. code-block::

    >>> 2 + 2
    4
    >>>

You've just evaluated your first Python expression.  It's a simple environment, but good enough to work through `the Python tutorial. <http://docs.python.org/tutorial/>`_

By the way, if you download the recommended upgrade mentioned at the top of 
this page, the "`IDLE </idle/doc/idle2.html>`_" development environment will 
make working through the tutorial a bit easier. 

Alternative Packages for Mac OS X.
==================================

- `ActiveState ActivePython <http://www.activestate.com/activepython>`_   (commercial and community versions, including scientific computing modules).    ActivePython also includes a variety of modules that build on the solid   core.

- `Enthought Python Distribution <http://www.enthought.com/products/epd.php>`_   The Enthought Python Distribution provides scientists with a comprehensive set    of tools to perform rigorous data analysis and visualization.