<h1>Steps to install a clean zope with buildout </h1>
$ virtualenv devel-venv<br>
$ source devel-venv/bin/activate<br>
$ curl -O http://downloads.buildout.org/2/bootstrap.py<br>
$ python bootstrap.py<br>
$ bin/buildout -c devel.cfg<br>
$ bin/instance<br>
