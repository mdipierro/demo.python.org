Windows Installer Features
--------------------------

Python 2.5 is distributed as a Microsoft Installer (MSI) file
on Windows. Typically, packages are installed by double-clicking
them in the file explorer. However, with the msiexec.exe command
line utility, additional features are available, like non-interactive 
installation and administrative installation.

Non-interactive Installation
----------------------------

With the command line

.. code-block::

    msiexec /i python<;version>.msi

installation can be initiated programmatically. Additional
parameters can be passed at the end of this command line, like

.. code-block::

    msiexec /i python-2.5.msi TARGETDIR=r:\python25

Limited user interface
~~~~~~~~~~~~~~~~~~~~~~

The amount of user interface that installer displays can
be controlled with /q options, in particular:
- /qn - No interface
- /qb - Basic interface - just a small progress dialog
- /qb! - Like /qb, but hide the Cancel button
- /qr - Reduced interface - display all dialogs that     don't require user interaction (skip all modal dialogs)
- /qn+ - Like /qn, but display "Completed" dialog at the end
- /qb+ - Like /qb, but display "Completed" dialog at the end

Target directory
~~~~~~~~~~~~~~~~

The property TARGETDIR determines the root directory of the Python
installation. For example, a different installation drive can
be specified with

.. code-block::

    TARGETDIR=R:\python25

The default TARGETDIR is [WindowsVolume]Python<;version>.

Installation for All Users
~~~~~~~~~~~~~~~~~~~~~~~~~~

Adding

.. code-block::

    ALLUSERS=1

causes an installation for all users. By default, the non-interactive
installation install the package just for the current user, and the
interactive installation offers a dialog which defaults to "all users"
if the user is sufficiently privileged.

Feature Selection
~~~~~~~~~~~~~~~~~

A number of properties allow selection of features to be installed,
reinstalled, or removed. The set of features for the Python installer
is
- DefaultFeature - install the interpreter proper, plus the core libraries
- Extensions - register extensions (.py, .pyc, etc)
- TclTk - install Tkinter, and IDLE
- Documentation - install documentation
- Tools - install the Tools/ directory
- Testsuite - install Lib/test/

In addition, ALL specifies all features. All features depend on
DefaultFeature, so installing any feature automatically installs the
default feature as well.
The following properties control features to be installed or removed
- ADDLOCAL - list of feature to be installed on the local machine
- REMOVE - list of features to be removed
- ADDDEFAULT - list of features added in their default configuration  (which is local for all Python features)
- REINSTALL - list of features to be reinstalled/repaired
- ADVERTISE - list of feature for which to perform an advertise installation

There are a few additional properties available; see the MSDN documentation
for details.

With these options, adding

.. code-block::

    ADDLOCAL=Extensions

installs the interpreter itself and registers the extensions, but does
not install anything else.

Uninstallation
--------------

With

.. code-block::

    msiexec /x python<;version>.msi

python can be uninstalled. It is not necessary to have the
MSI file available for uninstallation; alternatively, the package
or product code can also be specified. You can find the product
code by looking at the properties of the Uninstall shortcut that
Python installs in the start menu.

Administrative installation
---------------------------

With

.. code-block::

    msiexec /a python<;version>.msi

an "administrative" (network) installation can be initiated.
The files get unpacked into the target directory (which should
be a network directory), but no other modification is made to
the local system. In addition, another (smaller) msi file is
generated in the target directory, which clients can then use
to perform a local installation (future versions may also offer
to keep some features on the network drive altogether).

Currently, there is no user interface for administrative installations,
so the target directory must be passed on the command line.

There is no specific uninstall procedure for an administrative
install - just delete the target directory if no client uses
it anymore.

Advertisement
-------------

With

.. code-block::

    msiexec /jm python<;version>.msi

it would be possible, in principle, to "advertise" python to a
machine (with /ju to a user). This would cause the icons to appear
in the start menu, and the extensions to become registered, without
the software actually being installed. The first usage of a feature
would cause that feature to be installed.

*The Python installer currently supports
just advertisement of start menu entries, but no advertisement
of shortcuts.*

Automatic Installation on a Group of Machines
---------------------------------------------

With Windows Group Policy, it is possible to automatically install
Python an a group of machines. To do so, perform the following steps:
- Log on to the domain controller
- Copy the MSI file into a folder that is shared with access  granted to all target machines.
- Open the MMC snapin "Active Directory users and computers"
- Navigate to the group of computers that need Python
- Open Properties
- Open Group Policies
- Add a new polices, and edit it
- In Computer Configuration/Software Installation, chose      New/Package
- Select the MSI file through the network path
- Optionally, select that you want the Python to be deinstalled  if the computer leaves the scope of the policy.

Group policy propagation typically takes some time - to reliably deploy
the package, all machines should be rebooted.