# Database using MySQL
The database holds important information about the users and the executables the users have uploaded and want to run.

## Installing MySQL server 8.0 Community
MySQL server is a process that allows the connection and communication with the databases on the server
MySQL 8.0 community server can be downloaded from https://dev.mysql.com/downloads/mysql/ and installed. Once you install MySQL server it will run everytime you start the computer and stay on the entire time unless you change settings or turn it off. This is not a problem just somehing to keep in mind. 

## Installing MySQL Workbench 8.0 CE
The next thing to install is MySQL Workbench which is a tool to help configure MySQL server and the database(s) on the server.
MySQL workbench can be installed from https://dev.mysql.com/downloads/workbench/

## Installing Python packages
The first package is the mysql.connector library this can be done by just running "python -m pip install mysql-connector" in cmd. If you are attempting this on a unix based system it may be necessary to run "python3 -m pip install mysql-connector".
The second package which is only needed if it was not downloaded with the MySQL server. If you are encountering a "connector.connect" not defined you may need to intall this which can be done at https://dev.mysql.com/downloads/connector/python/ the applicable python 3.6 version should be installed.

## Creating a database on the MySQL server
This can be done simply by running CreateDatabase.py which will create a database on the localhost with user root and password "PASSWORD" and name distcompschema. If this runs without any errors you have successfuly created a blank database on the MySQL server.
To view the database in MySQL workbench you can open the workbench and click the + button next to MySQL connections. Then just enter the required information which should be correct by default and just click ok and then put the password that was in createdatabase.py.

## Adding the model to the database
In MySQL workbench on the homescreen on the left menu there is a model tab which is where you can add in the model from a sql file. Next to Models click the > button which allows you to import a model from file. Then click create EER model from script and then click the distcompschema.sql file which contains a description of the database model. Then click execute and just click next through the next windows. Now the model needs to be put into the created database which is done by clicking the database tab and the top and click foward engineer tehn just click next and go through the next couple windows. If this works successfully the model should be in the database.

## Accessing and using the database
For accessing the database I have implemented the file MyDB.py which both connects to the database and then allows for access to functions for adding and deleting data from the database.
Before being used the MyDB.py file needs to be edited and some of the values in the init function need to be changed to fit. The IP needs to be changed to localhost or 127.0.0.1 and the port needs to be changed to 3306.
Now the MyDb class can be imported and used in any other python file in our case we are importing it into the Python server and using these defined functions to access the database.

## Testing the database
A simple test program called Database_Test.py runs some of the basic operations of the database and prints out values relating to the values returned by the database. This can be expanded and altered for additional testing.
