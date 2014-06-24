=====================================
Zope buildout for a clean zope server
=====================================

.. contents ::

This buildout will create an isolated environment for running a clean zope
server.
There is one configuration available for running this buildout::
 1. development (devel)

Project name
------------
The project name is Clean Zope


Prerequisites - System packages
-------------------------------
These should be installed by the sysadmin (needs root)::

 $ sudo apt-get install python-dev curl subversion
 
Build devel
-------------
::

 $ virtualenv devel-venv
 $ source devel-venv/bin/activate
 $ curl -O http://downloads.buildout.org/2/bootstrap.py
 $ python bootstrap.py
 $ bin/buildout -c devel.cfg
 $ bin/instance
