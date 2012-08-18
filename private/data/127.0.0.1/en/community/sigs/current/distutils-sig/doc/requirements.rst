Python Distutils-SIG
====================

Requirements
------------

The proposed Module Distribution Utilities for Python, or
    **distutils** for short, are needed to fill a number of
    long-standing holes in the Python distribution and culture.  In
    roughly decreasing order of priority:

    - There must be an easy, standardized way for users and           administrators to add new modules (including extension           modules) to an existing Python installation on any platform           supported by Python itself.
- There must be an easy, standardized way to characterize           "meta-data" about a module distribution such as its name,           version number, area of applicability, description, and so           forth, for the use of indexing and search tools.
- There must be an easy, standardized way to create "built           distributions" (ready-to-install downloadable resources, with           all compilation and other processing done) for the major           platforms.
- Module distributions must have a standardized way to express           their dependencies on other modules (both simple           presence/absence and required version number) and on Python           itself (version number), and these dependencies must be           checked at setup/build/install time.
- It must be possible (and preferably easy) to instead download           and build from a source distribution.  (Necessary for people           who don't happen to be using one of the major platforms, or           who don't trust built distributions.)
- To aid in installing all modules, and in building extension           modules from C/C++ source, there must be a standardized way to           get Python's configuration data (such as compiler, compiler           flags, platform, default library directory, etc.).
- It must be easy for a module developer to create both source           and built distributions.
- It must be easy for a third party (the "packager") to download            a source distribution, build it on a particular platform, and           create a built distribution for that platform which can then           be trivially used by less sophisticated users of that           platform.

I have also written a summary of the 
    `division of labour and common tasks <../tasks/>`_, 
    which is a more detailed statement of the project requirements
    that comes at the problem from a different angle.