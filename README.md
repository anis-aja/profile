This is website project about profile. 
The project is using Python3 with Django supported by bootstrap4. 

To start the website, run the Django server first: 

Python3 manage.py runserver

The Django is conected to mysql using mysqlconnector. If there is error in mysqlconnector
when runserver with message error in mysqldb, first check the mysqlconnector installation. 
Go to Pypi.org to get the mysqlconnnector installation. If the error persist check the 
__init__.py, make sure __init__.py has below content

import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()

if the error persist, ensure python-dev has been installed. For Mac server, 
ensure command line tool package by using

xcode-select --install
