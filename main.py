# PYTHON APPLICATIONS

#Steps i followed below:

# MySQL= the data
## copy and paste the code from the appdbproj.sql file into MYSQL in vm
## check it worked by input : SELECT * FROM attendee;

# Neo4j = connections/relationships
## rename in neo4j admin to appdbproj and un comment the code
##  go to bin folder ,open cmd
## in cmd line run : C:Users\appDB\Documents\neo4j-community-5.26.19\bin>neo4j.bat console
## go to = localhost:7474\
## select database appdbproj, paste code in from appdbproj.json file into the query box and run it

# Conect to MySQL from python
## in anaconda prompt run conda install pymysql, as not included by default



## to import pymysql in python, run the code below, if it runs without error then it is installed correctly
## will only work if run inside vm as host is localhost (host="localhost"), if run outside vm will get error as it cannot connect to mysql server
## would need to use the ip address of the vm instead of localhost to connect from outside the vm, but we are running this inside vm so below code:



try:
    import pymysql
except ImportError:
    pymysql = None


def connect_to_mysql():
    if pymysql is None:
        raise ImportError(
            "PyMySQL is not installed. Run: pip install pymysql"
        )

    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="appdbproj",
        cursorclass=pymysql.cursors.DictCursor
    )

## to check the connection to MySQL, run the code below, if it prints "Connected successfully!" then it is working correctly

conn = connect_to_mysql()

print("Connected successfully!")

conn.close()

## now we have connected to MySQL, we can run queries to get data from the database and use it in our application. 
## We can also connect to Neo4j and run queries to get relationships between the data.

# App building

## now to set up the application display as outlined in project specification,
## we will use the data from MySQL and the relationships from Neo4j to create an app that displays the data in a user-friendly way.


