import sqlite3

#used to create a connection between sqlite and my database
database = sqlite3.connect("BladeStorm database.db")
#used to interact with the database through sql commands to create tables etc
cursor = database.cursor()

#creates a table called users that has the fields USER_ID,username and password
#USER ID will be the primary key of this table 
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                  USER_ID integer NOT NULL PRIMARY KEY,
                  username text NOT NULL,
                  password text NOT NULL)""")
database.commit()

#creates a table called teachers that has the fields TEACHER_ID,username and password
#TEACHER_ID will be the primary key of this table
cursor.execute("""CREATE TABLE IF NOT EXISTS teachers(
                  TEACHER_ID integer NOT NULL PRIMARY KEY,
                  username text NOT NULL,
                  password text NOT NULL)""")
database.commit()

#creates a table called score that has the fields USER_ID,score and highscore
#USER_ID will be the foreign key in this table
cursor.execute("""CREATE TABLE IF NOT EXISTS score(
        USER_ID integer NOT NULL,
        score integer NOT NULL,
        highscore integer NOT NULL,
        FOREIGN KEY(USER_ID) REFERENCES users(USER_ID))""")
database.commit()

#creates a table called question which has the fields QUESTION_ID,LEVEL_ID and Question_text
#QUESTION_ID will be the primary key in this table
cursor.execute("""CREATE TABLE IF NOT EXISTS question(
        QUESTION_ID integer PRIMARY KEY,
        LEVEL_ID integer NOT NULL,
        Question_text text NOT NULL)""")
database.commit()

#creates a table called question_choice which has the fields QUESTION_ID,option_A,option_B,option_C
#QUESTION_ID will be the foreign key of this table
cursor.execute("""CREATE TABLE IF NOT EXISTS question_choice(
        QUESTION_ID integer,
        option_A text NOT NULL,
        option_B text NOT NULL,
        option_C text NOT NULL,
        FOREIGN KEY(QUESTION_ID) REFERENCES question(QUESTION_ID))""")
database.commit()

#creates a table called answers which has the fields QUESITON_ID and answer_text
#QUESTION_ID will be the foreign key of this table
cursor.execute("""CREATE TABLE IF NOT EXISTS answer(
        QUESTION_ID integer,
        answer_text NOT NULL,
        FOREIGN KEY(QUESTION_ID) REFERENCES question(QUESTION_ID))""")
database.commit()


