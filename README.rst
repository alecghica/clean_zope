=====================================
Zope buildout for a clean zope server
=====================================

.. contents ::

This buildout will create an isolated environment for running a clean zope
server.
There is one configuration available for running this buildout::
 1. development (devel)

<h1>Prerequests</h1>
$ sudo apt-get install python-dev
$ sudo apt-get install curl
$ sudo apt-get install subversion

<h1>Steps to install a clean zope with buildout </h1>
$ virtualenv devel-venv<br>
$ source devel-venv/bin/activate<br>
$ curl -O http://downloads.buildout.org/2/bootstrap.py<br>
$ python bootstrap.py<br>
$ bin/buildout -c devel.cfg<br>
$ bin/instance<br>
