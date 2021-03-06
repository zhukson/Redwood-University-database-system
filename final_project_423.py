# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test1.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor
query_Department = """
    CREATE TABLE Department(
    Department_id varchar(30) NOT NULL PRIMARY KEY,
    Department_name varchar(50) NOT NULL
    Check(Department_name LIKE '%Department%'),
    Chair_name varchar(50),
    Num_faculty int
)
 """

query_major = """
    CREATE TABLE Major(
    Major_code varchar(3) NOT NULL PRIMARY KEY
    CHECK(length(Major_code)=3),
    Major_name varchar(50) NOT NULL,
    Department_id varchar(30) NOT NULL, 
    FOREIGN KEY(Department_id) REFERENCES Department(Department_id)
)
 """

query_student = """
    CREATE TABLE Student(
    Student_id varchar(50) NOT NULL PRIMARY KEY,
    Student_initials varchar(30)
    CHECK (length(Student_initials)>1),
    Student_name varchar(50)
)
"""

query_event = """
    CREATE TABLE Event(
    Event_id varchar(50) NOT NULL PRIMARY KEY,
    Event_name varchar(50) NOT NULL,
    Start_date date
    CHECK(Start_date > date('2021-12-9')),
    End_date date
    CHECK(End_date > date('2021-12-9')),
    CHECK(End_date > Start_date)
)
"""

query_Student_event = """
    CREATE TABLE Student_event(
    Student_id varchar(50) NOT NULL,
    Event_id varchar(30) NOT NULL,
    PRIMARY KEY(Student_id, Event_id),
    Foreign key(Student_id) references Student (Student_id) on delete cascade,
    Foreign key(Event_id) references Event (Event_id) on delete cascade
)
"""

query_Student_major = """
    CREATE TABLE Student_major(
    Student_id varchar(50) NOT NULL,
    Major_code varchar(3) NOT NULL,
    PRIMARY KEY(Student_id, Major_code),
    Foreign key(Student_id) references Student (Student_id) ON DELETE CASCADE,
    Foreign key(Major_code) references Major (Major_code) ON DELETE CASCADE
)
"""

query_Department_Event = """
    CREATE TABLE Department_Event(
    Department_id varchar(30) NOT NULL,
    Event_id varchar(50) NOT NULL,
    PRIMARY KEY(Department_id, Event_id),
    Foreign key (Department_id) references Department(Department_id) ON DELETE CASCADE,
    Foreign key (Event_id) references Event (Event_id) ON DELETE CASCADE
)
"""

# Execute query, the result is stored in cursor
cursor.execute(query_Department)
cursor.execute(query_major)
cursor.execute(query_student)
cursor.execute(query_event)
cursor.execute(query_Student_event)
cursor.execute(query_Student_major)
cursor.execute(query_Department_Event)

"""# insert 5 columns into each table"""

# Insert row into table
query_Department = []
query_Department.append("""INSERT INTO Department VALUES('AS','ART and SCIENCE Department', 'JACK', 105)""")
query_Department.append("""INSERT INTO Department VALUES('COMP', 'COMPUTER SCIENCE Department', 'Vic', 76) """)
query_Department.append("""INSERT INTO Department VALUES('ENG', 'Engineering Department', 'Mike', 90) """)
query_Department.append("""INSERT INTO Department VALUES('MSC', 'Music Department', 'Jacob', 98) """)
query_Department.append("""INSERT INTO Department VALUES('ECON', 'ECONOMICS Department', 'Nancy', 120) """)
query_major = []
query_major.append("""INSERT INTO Major VALUES('ART','ARTIFICIAL INTELLIGENCE','COMP') """)
query_major.append("""INSERT INTO Major VALUES('CSC','Computer Science', 'COMP') """)
query_major.append("""INSERT INTO Major VALUES('JAZ','JAZZ','MSC') """)
query_major.append("""INSERT INTO Major VALUES('FRN','FRENCH','AS') """)
query_major.append("""INSERT INTO Major VALUES('ECE','Electricity Engineering', 'ENG') """)
query_student = []
query_student.append("""INSERT INTO Student VALUES('A10001', 'LEO','LEONARDO') """)
query_student.append("""INSERT INTO Student VALUES('A10002','STE','STEFEN') """)
query_student.append("""INSERT INTO Student VALUES('A10003','JAC','JACKADS') """)
query_student.append("""INSERT INTO Student VALUES('A10004','KO','KOKO') """)
query_student.append("""INSERT INTO Student VALUES('A10005','ZIP','ZIPEI')""")
query_event = []
query_event.append("""INSERT INTO Event VALUES('E10001','HAPPY FITTING', date('2021-12-10'), date('2021-12-15')) """)
query_event.append("""INSERT INTO Event VALUES('E10002','CAKES FESTIVAL', date('2021-12-13'),date('2021-12-14')) """)
query_event.append("""INSERT INTO Event VALUES('E10003','BOAT COMPETITION', date('2021-12-20'),date('2021-12-22')) """)
query_event.append("""INSERT INTO Event VALUES('E10004','VIDEO GAMES', date('2021-12-12'),date('2021-12-15')) """)
query_event.append("""INSERT INTO Event VALUES('E10005','FIND A JOB', date('2021-12-10'),date('2021-12-20')) """)
query_Student_event = []
query_Student_event.append("""INSERT INTO Student_event VALUES('A10001','E10001') """)
query_Student_event.append("""INSERT INTO Student_event VALUES('A10002','E10002') """)
query_Student_event.append("""INSERT INTO Student_event VALUES('A10003','E10003') """)
query_Student_event.append("""INSERT INTO Student_event VALUES('A10004','E10004') """)
query_Student_event.append("""INSERT INTO Student_event VALUES('A10005','E10005') """)
query_Student_major = []
query_Student_major.append("""INSERT INTO Student_major VALUES('A10001','CSC') """)
query_Student_major.append("""INSERT INTO Student_major VALUES('A10002','ECE') """)
query_Student_major.append("""INSERT INTO Student_major VALUES('A10003','JAZ') """)
query_Student_major.append("""INSERT INTO Student_major VALUES('A10004','FRN') """)
query_Student_major.append("""INSERT INTO Student_major VALUES('A10005','ART') """)
query_Department_Event = []
query_Department_Event.append("""INSERT INTO Department_Event VALUES('COMP','E10001') """)
query_Department_Event.append("""INSERT INTO Department_Event VALUES('ENG','E10002') """)
query_Department_Event.append("""INSERT INTO Department_Event VALUES('MSC','E10003') """)
query_Department_Event.append("""INSERT INTO Department_Event VALUES('ECON','E10004') """)
query_Department_Event.append("""INSERT INTO Department_Event VALUES('AS','E10005') """)
query_total = [query_Department, query_major, query_student, query_event, query_Student_event, query_Student_major, query_Department_Event]
for i in query_total:
  for j in i:
    cursor.execute(j)

"""# 5 sql quries test"""

# (1) List the number of the Faculty in the engineering department.
query_1 = """
    SELECT NUM_faculty, Department_id, Department_name
    FROM Department
    where Department_id = 'ENG'
    """
# (2) List the department information including the name, id, chair name belong to the computer science major.
query_2 = """    
    SELECT d.Department_name, d.Department_id, d.Chair_name, m.Major_code
    FROM Major m, Department d
    WHERE m.Department_id = d.Department_id and m.Major_code = 'CSC'
    """
# (3) List the Start Date, End_date of event named ???HAPPY FITTING???
query_3 = """
      select Start_date, End_date, Event_name
      FROM Event
      where Event_name = 'HAPPY FITTING'
      """

# (4) List the Student id of those students who has major in ARTIFICIAL INTELLIGENCE.
query_4 = """
      select k.Major_code, m.Major_name, k.Student_id
      FROM Student_major k, Major m
      WHERE k.Major_code = m.Major_code and m.Major_name = 'ARTIFICIAL INTELLIGENCE'
"""

# (5) List the event(s) hold by COMPUTER SCIENCE Department
query_5 = """
      select d.Department_id, d.Department_name, k.Event_id, e.Event_name
      FROM Department_Event k, Department d, Event e
      WHERE d.Department_id = k.Department_id and d.Department_name = 'COMPUTER SCIENCE Department' and e.Event_id = k.Event_id
"""

print("(1) List the number of the Faculty in the engineering department\n")
cursor.execute(query_1)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)
print()
print("(2) List the department information including the name, id, chair name belong to the computer science major.\n")
cursor.execute(query_2)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)
print()
print("(3) List the Start Date, End_date of event named ???HAPPY FITTING???\n")
cursor.execute(query_3)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)
print()
print("(4) List the Student id of those students who has major in ARTIFICIAL INTELLIGENCE.\n")
cursor.execute(query_4)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)
print()
print("(5) List the event(s) hold by COMPUTER SCIENCE Department\n")
cursor.execute(query_5)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)
print()

"""# close the database"""

# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()