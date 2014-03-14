<h1>Steps to install an clean zope </h1>
$ cd clean_zope<br>
$ virtualenv devel-venv<br>
$ source devel-venv/bin/activate<br>
$ pip install -r requirements-dev.txt<br>
$ curl -O http://downloads.buildout.org/2/bootstrap.py<br>
$ python bootstrap.py<br>
$ ./bin/buildout -c devel.cfg<br>
$ ./bin/instance<br>
