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



# Order to build the app,(as advised byreference in reference folder) we will follow the steps below:


# Main menu
# Option 1
# Option 6
# Option 2
# Option 3
# Option 4
# Option 5


## menu page
## this will be main page of app


def main_menu():
    while True:
        print("\nConference Management")
        print("---------------------")
        print()
        print("MENU")
        print("====")
        print("1 - View Speakers & Sessions")
        print("2 - View Attendees by Company")
        print("3 - Add New Attendee")
        print("4 - View Connected Attendees")
        print("5 - Add Attendee Connection")
        print("6 - View Rooms")
        print("x - Exit application")

        choice = input("Choice: ")

        if choice == "1":
            view_speakers_sessions()

        elif choice == "2":
            view_attendees_by_company()

        elif choice == "3":
            add_new_attendee()

        elif choice == "4":
            print("Option 4 later")

        elif choice == "5":
            print("Option 5 later")

        elif choice == "6":
            view_rooms()

        elif choice.lower() == "x":
            print("Exiting application...")
            break

        else:
            print("Invalid choice")


#layout of menu page, will add functionality to options later
#1,2,3 will use MySQL data, 4 and 5 will use Neo4j data, 6 will use MySQL data


# option 1. view speakers and sessions




def view_speakers_sessions():# this creates the function for option 1.
    speaker_name = input("\nEnter speaker name : ")#asks for input parameter to search for in database

    conn = connect_to_mysql()# opens connection to database
    cursor = conn.cursor()# this sends the query to database,query below:

# query to get required and connects each session to its room, both tables have room id
    sql = """
    SELECT speakerName, sessionTitle, roomName 
    FROM session
    JOIN room ON session.roomID = room.roomID
    WHERE speakerName LIKE %s
    """

    search_value = "%" + speaker_name + "%"
    cursor.execute(sql, (search_value,))# runs the query specified
    results = cursor.fetchall()

    print("Session Details For :", speaker_name)
    print("------------------------------------------------")

    if results:
        for row in results:
            print(row["speakerName"], "|", row["sessionTitle"], "|", row["roomName"])
    else:
        print("No speakers found of that name")

    cursor.close()
    conn.close()
