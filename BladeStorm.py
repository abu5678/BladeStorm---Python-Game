from tkinter import *
from PIL import ImageTk,Image
from database import *


screen = Tk()
screen.geometry("1500x750")
screen.title("NEA")


#This will load and place the background image of the game menu
background = ImageTk.PhotoImage(Image.open("images/background2.jpg"))
Label(image = background).place(x=0,y=0)

class menu():
    def __init__(self):
        self.teacher = False
        self.student = False
        self.valid_username = False
        self.correct_details = False
        self.valid_answer = False

    #This method is used to create the main menu and will display a start button and exit button
    def main_menu(self):
        self.start_button = Button(text = "Start",font =("Franklin Gothic Demi Cond",30),bg="#3d3d3d",command = lambda:[self.destroy_main_menu(),self.student_or_teacher_menu()])
        self.start_button.pack(pady=(150,50))
        self.exit_button =Button(text = "Exit",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",command = screen.destroy)
        self.exit_button.pack(pady=50)

    #This method is used to delete the main menu so that a new menu can be displayed
    def destroy_main_menu(self):
        self.start_button.destroy()    
        self.exit_button.destroy()

    #This mehod is used to create a start menu which will give the user the option to login,register or go back    
    def start_menu(self):
        self.welcome_text = Label(text = "Welcome",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.welcome_text.pack(pady = (20,0))
        self.login_button = Button(text = "Login",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",command = lambda:[self.destroy_start_menu(),self.login()])
        self.login_button.pack(pady = (100,50))
        self.register_button = Button(text = "Register",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",command = lambda:[self.destroy_start_menu(),self.register()])
        self.register_button.pack(pady = 50)
        self.back_button = Button(text = "Back",command = lambda:[self.destroy_start_menu(),self.main_menu()], font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.back_button.pack(pady = 50)
        
    #This method is used to delete the start menu so that a new menu can be displayed
    def destroy_start_menu(self):
        self.welcome_text.destroy()
        self.login_button.destroy()
        self.register_button.destroy()
        self.back_button.destroy()

    #This method is used to create the login page where the user will be able to enter their username and password and go back
    def login(self):
        self.request_text = Label(text = "Please enter your login details",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.request_text.pack(pady = (20,0))
        self.username_text = Label(text = "Username",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.username_text.pack(pady = (100,0))
        self.username_entry = Entry(textvariable = self.username_text)
        self.username_entry.pack(pady = (10,0))
        self.password_text = Label(text = "Password",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.password_text.pack(pady = (50,0))
        self.password_entry = Entry(textvariable = self.password_text)
        self.password_entry.pack(pady = (10,0))
        self.login_button = Button(text = "Login", font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d", command = self.check_login_details)
        self.login_button.pack(pady = 50)
        self.back_button = Button(text = "Back",command = lambda:[self.destroy_login_menu(),self.start_menu()], font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.back_button.pack()

    #This method is used to delete the login menu so that a new menu can be displayed
    def destroy_login_menu(self):
        self.request_text.destroy()
        self.username_text.destroy()
        self.password_text.destroy()
        self.login_button.destroy()
        self.username_entry.destroy()
        self.password_entry.destroy()
        self.back_button.destroy()

    #This method is used to determine whether the user is a student or teacher
    def student_or_teacher_menu(self):
        self.request_text = Label(text = "Please choose whether you are a student or teacher",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.request_text.pack(pady = (100,0))
        self.student_button = Button(text = "Student",command = lambda:[self.destroy_student_or_teacher_menu(),self.start_menu(),self.student_chosen()], font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.student_button.pack(pady = 50)
        self.teacher_button = Button(text = "Teacher",command = lambda:[self.destroy_student_or_teacher_menu(),self.start_menu(),self.teacher_chosen()], font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.teacher_button.pack(pady = 50)

    #These 2 methods are used to store whether or not the user is a teacher or a student
    def teacher_chosen(self):
        self.teacher = True
        self.student = False

    def student_chosen(self):
        self.student = True
        self.teacher = False

    #This method is used to delete the student or teacher menu so that a new menu can be displayed
    def destroy_student_or_teacher_menu(self):
        self.request_text.destroy()
        self.student_button.destroy()
        self.teacher_button.destroy()

    #This will create the register page where the user will be able to enter a username password and will be asked to confirm their password    
    def register(self):
        
        #These values  will have the default value of an empty string "" so that what the user enters will be stored as a string
        self.username = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()
        
        self.request_text = Label(text = "Please enter your login details",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.request_text.pack(pady = (20,0))
        self.username_text = Label(text = "Username",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.username_text.pack(pady = (100,0))
        self.username_entry = Entry(textvariable = self.username)
        self.username_entry.pack(pady = (10,0))
        self.password_text = Label(text = "Password",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.password_text.pack(pady = (50,0))
        self.password_entry = Entry(textvariable = self.password)
        self.password_entry.pack(pady = (10,0))
        self.confirm_password_text = Label(text = "Confirm Password",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.confirm_password_text.pack(pady = (30,0))
        self.confirm_password_entry = Entry(textvariable = self.confirm_password)
        self.confirm_password_entry.pack(pady = (10,0))
        self.register_button = Button(text = "Register",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",
                                      command = lambda :[self.check_registration_details()])
        self.register_button.pack(pady = 50)
        self.back_button = Button(text = "Back",command = lambda:[self.destroy_register_menu(),self.start_menu()], font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.back_button.pack()

    #This method is used to delete the register menu so that a new menu can be displayed
    def destroy_register_menu(self):
        self.request_text.destroy()
        self.username_text.destroy()
        self.password_text.destroy()
        self.confirm_password_text.destroy()
        self.register_button.destroy()
        self.username_entry.destroy()
        self.password_entry.destroy()
        self.confirm_password_entry.destroy()
        self.back_button.destroy()

    #When the user clicks the register button the code will validate what the user has entered through this method
    #elif statements are used to make sure the details entered pass every validation check
    def check_registration_details(self):
        self.username_info = self.username_entry.get()
        self.password_info = self.password_entry.get()
        self.confirm_password_info = self.confirm_password_entry.get()

        #This will validate the username by selecting all the stored usernames in the user and teacher table that is equal to what the user has written
        if self.student == True:
            self.username_check = cursor.execute("SELECT username FROM users WHERE username = (?)",(self.username_info,)).fetchall()
        if self.teacher == True:
            self.username_check = cursor.execute("SELECT username FROM teachers WHERE username = (?)",(self.username_info,)).fetchall()

        #if it is more than 0 then that means this username already exists and an error is displayed to the user
        if len(self.username_check) > 0:
            self.error_text = Label(text = "Username already exists",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.error_text.place(x=625,y=100)
            self.error_text.after(3000,self.error_text.destroy)
            self.valid_username = False
        #this will check if the username is less than 3 characters or more than 10 characters if so an error is displayed
        elif len(self.username_info)< 3 or len(self.username_info) > 10:
            self.error_text = Label(text = "Username can only be between 3 and 10 characters",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.error_text.place(x=500,y=100)
            self.error_text.after(3000,self.error_text.destroy)
            self.valid_username = False
        elif self.password_info == "":
            self.error_text = Label(text = "You must enter a password",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.error_text.place(x=500,y=100)
            self.error_text.after(3000,self.error_text.destroy)
            self.valid_username = False
            
        #this will check if what the user has written in the password box is the same as what is written in the confirm password box
        elif self.confirm_password_info != self.password_info:
            self.error_text = Label(text = "Password and confirm password must match",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.error_text.place(x=500,y=100)
            self.error_text.after(3000,self.error_text.destroy)
            self.valid_username = False
        else:
            #if the user's details passes all theses checks then that means the user has entered their details correctly
            self.valid_username = True
        if self.valid_username == True:
            #this will store the username and password in the user or teacher table
            if self.student == True:
                cursor.execute("INSERT INTO users(username,password)VALUES(?, ?)",(self.username_info,self.password_info))
                database.commit()
                #when the user registers they are given a user id so that user id is retrieved and the users score and highscore will automatically be set to 0
                self.get_username_id = cursor.execute("SELECT USER_ID FROM users WHERE username = (?)",(self.username_info,)).fetchall()
                database.commit()
                cursor.execute("INSERT INTO score(USER_ID,score,highscore)VALUES(?,0,0)",(self.get_username_id[0][0],))
                database.commit()
            if self.teacher == True:
                cursor.execute("INSERT INTO teachers(username,password)VALUES(?, ?)",(self.username_info,self.password_info))
                database.commit()
                
            self.registered_text = Label(text = "You have successfully registered",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.registered_text.place(x=500,y=100)
            self.registered_text.after(3000,self.registered_text.destroy)

    #this method will validate the user's login details
    #elif statements are used to make sure the details entered pass every validation check
    def check_login_details(self):
        self.username_info = self.username_entry.get()
        self.password_info = self.password_entry.get()
        #this will check if what the user has entered exists in the user or teachers table
        if self.student == True:
            self.username_check = cursor.execute("SELECT username FROM users WHERE username = (?)",(self.username_info,)).fetchall()
            self.password_check = cursor.execute("SELECT password FROM users WHERE username = (?)",(self.username_info,)).fetchall()
        if self.teacher == True:
            self.username_check = cursor.execute("SELECT username FROM teachers WHERE username = (?)",(self.username_info,)).fetchall()
            self.password_check = cursor.execute("SELECT password FROM teachers WHERE username = (?)",(self.username_info,)).fetchall()

        # it is 0 then that means that username has not been registered yet
        if len(self.username_check) == 0:
            self.error_text = Label(text = "Username does not exist",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.error_text.place(x=625,y=100)
            self.error_text.after(3000,self.error_text.destroy)
            self.correct_details = False
        #this will check the password the user has entered matches the password stored in the database that corresponds to the username they have entered
        elif  self.password_check[0][0] != self.password_info:
            self.error_text = Label(text = "Incorrect password",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.error_text.place(x=625,y=100)
            self.error_text.after(3000,self.error_text.destroy)
            self.correct_details = False     
        else:
            self.correct_details = True

        #if the user is a student they will be taken to the play game menu where they will be able to start the game and view the leaderboard
        if self.correct_details == True and self.student == True:
            self.play_game_menu()
            self.destroy_login_menu()
        #if the user is a teacher they will be taken to the teacher menu where they will be able to add questions to different levels
        if self.correct_details == True and self.teacher == True:
            self.teacher_menu()
            self.destroy_login_menu()

    #this will create the teacher menu and will display an add question button and an option to return to the main menu
    def teacher_menu(self):
        if self.teacher == True:
            self.add_question_button = Button(text = "Add Question",font =("Franklin Gothic Demi Cond",30),bg="#3d3d3d",
                                              command = lambda :[self.destroy_teacher_menu(),self.select_level()])
            self.add_question_button.pack(pady=(150,50))
            self.main_menu_button = Button(text = "Return to main menu",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",
                                           command = lambda :[self.destroy_teacher_menu(),self.main_menu()])
            self.main_menu_button.pack(pady=50)

    #This method is used to delete the teacher menu so that a new menu can be displayed
    def destroy_teacher_menu(self):
        self.add_question_button.destroy()
        self.main_menu_button.destroy()
    #this will create the play game menu which will display an option to play the game, view the leader board or return to the main menu
    def play_game_menu(self):
        if self.student == True:
            self.play_game_button = Button(text = "Play Game",font =("Franklin Gothic Demi Cond",30),bg="#3d3d3d",command = run_game)
            self.play_game_button.pack(pady=(150,50))
            self.leader_board_button = Button(text = "Leader board",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",command = lambda:[self.destroy_play_game_menu(),self.leaderboard_menu()])
            self.leader_board_button.pack(pady=50)
            self.main_menu_button = Button(text = "Return to main menu",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",command = lambda :[self.destroy_play_game_menu(),self.main_menu()])
            self.main_menu_button.pack(pady=50)
    #this method is used to delete the play game menu so that a new menu can be displayed
    def destroy_play_game_menu(self):
        self.play_game_button.destroy()
        self.leader_board_button.destroy()
        self.main_menu_button.destroy()
    #this willl create the leader board screen and will show the rank, username and high score of the top 10 players 
    def leaderboard_menu(self):
            self.leaderboard_text = Label(text = "Leaderboard",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.leaderboard_text.pack(pady = (30,0))
            self.back_button = Button(text = "Back",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",command = lambda :[self.destroy_leaderboard_menu(),self.play_game_menu()])
            self.back_button.place(x=50,y=30)
            self.leaderboard_ranking_text = Label(text = "Rank",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.leaderboard_ranking_text.place(x = 175,y = 120)
            self.leaderboard_username_text = Label(text = "Username",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.leaderboard_username_text.place(x = 375,y = 120)
            self.leaderboard_highscore_text = Label(text = "Highscore",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.leaderboard_highscore_text.place(x = 575,y = 120)
            #this SQL statemnt will retrieve all the highscores from the score table
            self.all_highscores = cursor.execute("SELECT highscore FROM score").fetchall()
            database.commit()

            self.highscores_list = []
            #this will take all the high scores and put them into a list
            for i in range(len(self.all_highscores)):
                           self.new_highscores = self.all_highscores[i][0]
                           self.highscores_list.append(self.new_highscores)
            #this will perform a mergesort on the list of all the high scores
            mergesort(self.highscores_list)
            #the mergesort will get the scores from smallest to largest so the list needs to be reversed so that it will now show largest to smallest
            last_10.reverse()
            #this for loop will go through each highscore in the list get the user id that score and get the username and the highscore and display it
            #it will also show the ranks between all the players
            for i in range(len(last_10)):
                self.rank_text = [i+1]
                self.select_last_10_users_score = cursor.execute("SELECT USER_ID FROM score WHERE highscore = (?)",(last_10[i],)).fetchall()
                database.commit()
                self.select_last_10_users_score_username = cursor.execute("SELECT username FROM users WHERE USER_ID = (?)",(self.select_last_10_users_score[0][0],)).fetchall()
                database.commit()
                self.select_last_10_users_highscore = cursor.execute("SELECT highscore FROM score WHERE USER_ID = (?)",(self.select_last_10_users_score[0][0],)).fetchall()
                database.commit()
                self.username_text = Label(text = self.select_last_10_users_score_username,font =("Franklin Gothic Demi Cond",15),bg = "#3d3d3d")
                self.username_text.place(x = 400 , y = [170 + i*50])
                self.ranks_text = Label(text = self.rank_text,font =("Franklin Gothic Demi Cond",15),bg = "#3d3d3d")
                self.ranks_text.place(x = 200 , y = [170 + i*50])
                self.highscores_ranks_text = Label(text = self.select_last_10_users_highscore,font =("Franklin Gothic Demi Cond",15),bg = "#3d3d3d")
                self.highscores_ranks_text.place(x = 600 , y = [170 + i*50])
            
                
    #this method will destroy the leader board screen so that a new screen can be displayed
    def destroy_leaderboard_menu(self):
        self.leaderboard_text.destroy()
        self.back_button.destroy()
        self.leaderboard_ranking_text.destroy()
        self.leaderboard_username_text.destroy()
        self.leaderboard_highscore_text.destroy()
        self.username_text.destroy()
        self.ranks_text.destroy()
        self.highscores_ranks_text.destroy()

    #when the teacher is trying to add a question they are sent here to select the level they want add that question to       
    def select_level(self):
            self.select_level_text = Label(text = "Please select a level",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.select_level_text.pack(pady = (100,0))
            self.level_1_button = Button(text = "Level 1",font =("Franklin Gothic Demi Cond",30),bg="#3d3d3d",
                                         command = lambda:[self.destroy_select_level_menu(),self.level_id_1(),self.add_question_menu()])
            self.level_1_button.pack(pady= (100,0))
            self.level_2_button = Button(text = "Level 2",font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",
                                         command = lambda:[self.destroy_select_level(),self.level_id_2(),self.add_question_menu()])
            self.level_2_button.pack(pady=(100,0))

    def level_id_1(self):
        self.level_id = 1
    def level_id_2(self):
        self.level_id = 2

    def destroy_select_level_menu(self):
        self.level_1_button.destroy()
        self.level_2_button.destroy()
        self.select_level_text.destroy()

    #once the user selects a level they will be taken to this menu and will be asked to enter a question, 3 options and an answer
    #ther will also be a submit button which will call another method to check if the question has been enetered correctly
    #and a back button which will return you to the previous screen.
    def add_question_menu(self):
        self.add_question = StringVar()
        self.option_a = StringVar()
        self.option_b = StringVar()
        self.option_c = StringVar()
        self.answer = StringVar()
        
        self.add_question_text = Label(text = "Add a question",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.add_question_text.pack(pady = (60,0))
        self.add_question_entry = Entry(textvariable = self.add_question,width = 100)
        self.add_question_entry.pack(pady = (10,0))

        self.option_a_text = Label(text = "Option A",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.option_a_text.pack(pady = (50,0))
        self.option_a_entry = Entry(textvariable = self.option_a,width=100)
        self.option_a_entry.pack(pady = (10,0))

        self.option_b_text = Label(text = "Option B",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.option_b_text.pack(pady = (50,0))
        self.option_b_entry = Entry(textvariable = self.option_b,width = 100)
        self.option_b_entry.pack(pady = (10,0))

        self.option_c_text = Label(text = "Option C",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.option_c_text.pack(pady = (50,0))
        self.option_c_entry = Entry(textvariable = self.option_c,width =100)
        self.option_c_entry.pack(pady = (10,0))

        self.answer_text = Label(text = "Answer",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
        self.answer_text.pack(pady = (50,0))
        self.answer_entry = Entry(textvariable = self.answer)
        self.answer_entry.pack(pady = (10,0))

        self.submit_button = Button(text = "Submit", font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d",
                                    command = lambda:[self.check_valid_answer(),self.add_question_database()])
        self.submit_button.place(x=600,y=650)

        self.back_button = Button(text = "Back",command = lambda:[self.destroy_add_question_menu(),self.teacher_menu()], font =("Franklin Gothic Demi Cond",30),bg = "#3d3d3d")
        self.back_button.place(x=800,y=650)

    #this method is used to check if the teacher has created a question incorrectly     
    def check_valid_answer(self):
        self.add_question_info = self.add_question_entry.get()
        self.option_a_info = self.option_a_entry.get()
        self.option_b_info = self.option_b_entry.get()
        self.option_c_info = self.option_c_entry.get()
        self.answer_info = self.answer_entry.get()
        #this if statement will check if what is in the answer box is one of the 3 options, if it is not an error will be displayed
        if self.answer_info not in ["a","b","c"]:
            self.valid_answer = False
            self.error_text = Label(text = "answer must be lowercase a or b or c",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.error_text.place(x=600,y=10)
            self.error_text.after(3000,self.error_text.destroy)
        #this elif statement will check if question or the 3 options are left blank if so then an error will be displayed
        elif self.option_a_info == "" or self.option_b_info == "" or self.option_c_info == "" or self.add_question_info == "":
            self.valid_answer = False
            self.error_text = Label(text = "add question and option a or b or c cannot be left blank",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.error_text.place(x=600,y=10)
            self.error_text.after(3000,self.error_text.destroy)
                
        else:
            #if it passes all the above checks that means that the question has been created correctly
            self.valid_answer = True
    #this method is used to store the question and its details into the database
    def add_question_database(self):
        if self.valid_answer == True:
            #this will insert into the databse the question and the level id of the question inot the question table
            cursor.execute("INSERT INTO question(LEVEL_ID,Question_text)VALUES(?, ?)",(self.level_id,self.add_question_info))
            database.commit()
            #the question id of the question eneter is then retrieved with this SQL statement  
            self.get_question_id = cursor.execute("SELECT QUESTION_ID FROM question ORDER BY rowid DESC LIMIT 1").fetchall()
            database.commit()
            #then the options for the question is stored in the question choice table with the correct question id 
            cursor.execute("INSERT INTO question_choice(QUESTION_ID,option_A,option_B,option_C)VALUES(?, ?, ?, ?)",
                           (self.get_question_id[0][0],self.option_a_info,self.option_b_info,self.option_c_info))
            database.commit()
            #then the answer to the question is stored in the answer table
            cursor.execute("INSERT INTO answer(QUESTION_ID,answer)VALUES(?, ?)",(self.get_question_id[0][0],self.answer_info))
            database.commit()

            self.validation_text = Label(text = "You have successfully added a question",font =("Franklin Gothic Demi Cond",20),bg = "#3d3d3d")
            self.validation_text.place(x=600,y=100)
            self.validation_text.after(3000,self.validation_text.destroy)

            self.destroy_add_question_menu()
            self.teacher_menu()

    #this will destroy the add question screen so that a new screen can be displayed
    def destroy_add_question_menu(self):
        self.add_question_text.destroy()
        self.add_question_entry.destroy()
        self.option_a_text.destroy()
        self.option_a_entry.destroy()
        self.option_b_text.destroy()
        self.option_b_entry.destroy()
        self.option_c_text.destroy()
        self.option_c_entry.destroy()
        self.answer_text.destroy()
        self.answer_entry.destroy()
        self.submit_button.destroy()
        self.back_button.destroy()
#when the leader board is being checked a mergesort of all the high scores will be performed
def mergesort(highscores_list):
                global last_10
                #this will divide the list into 2 halves so that each item in each halves can be compared
                if len(highscores_list) > 1:
                    left_half = highscores_list[:len(highscores_list)//2]
                    right_half = highscores_list[len(highscores_list)//2:]

                    mergesort(left_half)
                    mergesort(right_half)

                    x = 0
                    y = 0
                    z = 0
                    #if x is less than the how many is in the left half of the list or if y is less than how many is in the right half of the list
                    #this while loop will keeep being called
                    while x < len(left_half) and y < len(right_half):
                        if left_half[x] < right_half[y]:
                            #if x is less than y then the first item in the new list will be x as it is sorting it from smallest to largets
                            highscores_list[z] = left_half[x]
                            x += 1
                        else:
                            #if x is not less than y that means y is less x and z will need to be y
                            highscores_list[z] = right_half[y]
                            y += 1
                        z += 1
                    while x < len(left_half):
                        highscores_list[z] = left_half[x]
                        x += 1
                        z += 1
                    while y < len(right_half):
                        highscores_list[z] = right_half[y]
                        y += 1
                        z += 1
                #each time a the smallest value for the next item in the list is found they are all incremented by one so that the next value can be checked
                last_10 = highscores_list[-10:]
                #this will keep the last 10 highscores in the sorted list of high scores
           
menu = menu()
menu.main_menu()


from animations import *
import pygame
import random


def run_game():
        #this will create the game window and set its height and width and the background image of the game
        pygame.init()
        screen_width = 1500
        screen_height = 750
        screen = pygame.display.set_mode((screen_width ,screen_height))
        pygame.display.set_caption("NEA")
        Background = (pygame.image.load("images/level/dungeon_background2.xcf"))
        font = pygame.font.SysFont('comicsansms', 40, True)
        paused = False
        game_over1 = False

        #this class will be the character that the user will control and will respond to user inputs
        class player():
                def __init__(self,x,y,health):
                        self.x = x
                        self.y = y
                        self.health = health
                        self.old_health = 0
                        self.energy  = 0
                        self.speed = 0
                        self.score = 0
                        self.last_updated = 0
                        self.animation_speed = 175
                        self.scale = 2
                        #self.damage = 0
                        self.jump_height = 0
                        #self.y_speed = 0
                        self.facing_right = False
                        self.player_in_air = False
                        self.moving_right = False
                        self.moving_left = False
                        self.jump = False
                        self.normal_attacking = False
                        self.special_attacking = False
                        self.ultimate_attacking = False
                        self.player_dying = False
                        self.collision = False
                        self.pickup = False
                        self.idle_animation_frame = 0
                        self.run_animation_frame = 0
                        self.attack_animation_frame = 0
                        self.ultimate_attack_animation_frame = 0
                        self.player_dead_animation_frame = 0

                #this method will be creating all the rectangles that will be around the player that will act as a hitbox and be used to detect collisions
                #each action that the player can perform have their own rectangle and hitbox
                def rectangle(self):
                    self.rect = pygame.Rect(self.x,self.y,90,130)
                    self.rect.center = (self.x,self.y)
                    self.player_rect = self.rect

                    self.special_attacking_rect = self.attack_image.get_rect()
                    self.special_attacking_rect.center = (self.x-25,self.y-40)
                    

                    self.special_attacking_right_rect = self.attack_right_image.get_rect()
                    self.special_attacking_right_rect.center = (self.x+25,self.y-40)

                    self.ultimate_attacking_rect = self.special_attack_image.get_rect()
                    self.ultimate_attacking_rect.center = (self.x-105,self.y-70)

                    self.ultimate_attacking_right_rect = self.special_right_attack_image.get_rect()
                    self.ultimate_attacking_right_rect.center = (self.x+128,self.y-70)

                #this method will display the player's healthbar on the top right of the screen
                def healthbar(self):
                    self.health_rect = pygame.Rect(1050,20,self.health*2,50)
                    pygame.draw.rect(screen,(100,0,0),(1050,20,400,50))
                    pygame.draw.rect(screen,(0,75,0),self.health_rect)
                    health_text = font.render(str(self.health),1,(0,75,0))
                    screen.blit(health_text,(960,15))

                #this method will display the player's score on the top left of the screen
                def display_score(self):
                    self.score_text = font.render("score:",1,(255,255,255))
                    screen.blit(self.score_text,(0,15))
                    self.show_score = font.render(str(self.score),1,(255,255,255))
                    screen.blit(self.show_score,(150,15))

                #this method will display the player's energy bar underneath the health bar
                def energy_bar(self):
                    #this if statement will make sure that the max amount of energy the player can have will not exceed 200
                    if self.energy > 200:
                        self.energy = 200
                    self.energy_rect = pygame.Rect(1050,80,self.energy*2,50)
                    pygame.draw.rect(screen,(0,0,0),(1050,80,400,50))
                    pygame.draw.rect(screen,(0,41,98),self.energy_rect)
                    energy_text = font.render(str(self.energy),1,(0,41,98))
                    screen.blit(energy_text,(960,80))

                #this method will get the image of the player moving and scale the image to be bigger                       
                def move(self):
                    self.moving_left_image = pygame.image.load("images/player/moving/move.xcf")
                    self.moving_left_image = pygame.transform.scale(self.moving_left_image,(int(self.moving_left_image.get_width() * self.scale),
                                                                                            int(self.moving_left_image.get_height() * self.scale)))
                    #this will flip the image to be in the oppostie direction
                    self.moving_right_image = pygame.transform.flip(self.moving_left_image,True,False)

                #this method is used to keep track of the idle animation and is responsible of holding each frame 
                def idle_animation(self):
                        #this if statemnt is used to check if the idle animation has reached its last frame of the animtaion if it has the animation frame will
                        #reset to 0 which restarts the animation
                        if self.idle_animation_frame > 3:
                            self.idle_animation_frame = 0
                        self.idle_image = idle[self.idle_animation_frame]
                        self.idle_image = pygame.transform.scale(self.idle_image,(int(self.idle_image.get_width() * self.scale), int(self.idle_image.get_height() * self.scale)))
                        #this will flip the image to be in the oppostie direction
                        self.idle_right_image = pygame.transform.flip(self.idle_image,True,False)

                #when the player wants to do a special attack this method will be called
                #it will reset the animtaion frames of the attack and assign the player damage to become the damage of the special attack
                #it will also make it so that no other attack can be performed as every other attack is False
                def special_attack(self):
                    self.attack_animation_frame = 0
                    self.damage = 75
                    if self.player_in_air == False:
                            self.ultimate_attack_animation_frame = 0
                            self.special_attacking = True
                            self.ultimate_attacking = False
                            self.normal_attacking = False

                #this method will deal with the normal and special attack animations it will load each frame of the animation
                def attack_animation(self):                      
                        if self.special_attacking == True:
                                #this if statemnt is used to check if the special attack animation has reached its last frame of the animtaion if it has the animation frame will
                                #reset to 0 which restarts the animation
                                if self.attack_animation_frame > 25:
                                    self.attack_animation_frame = 0
                                    #it makes special attacking animation false so that once the animation is finsihed the player will not automatically attack again
                                    self.special_attacking = False
                                    #this will take away the player's energy
                                    self.energy -= 75
                                    #since the attack is going to stop that means the enemy's are no longer being attacked and will be able to move again
                                    #if the enemy has been attacked he wont move back to the player again until he has finished attacking
                                    enemy1.attacked = False
                                    enemy2.attacked = False
                                    enemy3.attacked = False
                                    enemy4.attacked = False
                                    enemy5.attacked = False
                                    enemy6.attacked = False
                        if self.normal_attacking == True:
                                 #this if statemnt is used to check if the normal attack animation has reached its last frame of the animtaion if it has the animation frame will
                                 #reset to 0 which restarts the animation
                                 if self.attack_animation_frame > 7:
                                    self.attack_animation_frame = 0
                                    #it makes special attacking animation false so that once the animation is finsihed the player will not automatically attack again
                                    #since the attack is going to stop that means the enemy's are no longer being attacked and will be able to move again
                                    #if the enemy has been attacked he wont move back to the player again until he has finished attacking
                                    self.normal_attacking = False
                                    enemy1.attacked = False
                                    enemy2.attacked = False
                                    enemy3.attacked = False
                                    enemy4.attacked = False
                                    enemy5.attacked = False
                                    enemy6.attacked = False
                        #this variable will be responsible for loading the specific frame from the animation list
                        self.attack_image = attack[self.attack_animation_frame]
                        #this will scale the image
                        self.attack_image = pygame.transform.scale(self.attack_image,(int(self.attack_image.get_width() * self.scale), int(self.attack_image.get_height() * self.scale)))
                        #this will flip the image to be in the oppostie direction
                        self.attack_right_image = pygame.transform.flip(self.attack_image,True,False)

                #when the player wants to do a special attack this method will be called
                #it will reset the animtaion frames of the attack and assign the player damage to become the damage of the normal attack
                #it will also make it so that no other attack can be performed as every other attack is False
                def normal_attack(self):
                    self.attack_animation_frame = 0
                    self.damage = 25
                    if self.player_in_air == False:
                            self.ultimate_attack_animation_frame = 0
                            self.normal_attacking = True
                            self.ultimate_attacking = False
                            self.special_attacking = False

                #when the player wants to do a special attack this method will be called
                #it will reset the animtaion frames of the attack and assign the player damage to become the damage of the ultimate attack
                #it will also make it so that no other attack can be performed as every other attack is False                                    
                def ultimate_attack(self):
                    self.ultimate_attack_animation_frame = 0
                    self.damage = 200
                    if self.player_in_air == False:
                            self.attack_animation_frame = 0
                            self.ultimate_attacking = True
                            self.special_attacking = False
                            self.normal_attacking = False

                def ultimate_attack_animation(self):
                        #this if statemnt is used to check if the special attack animation has reached its last frame of the animtaion if it has the animation frame will
                        #reset to 0 which restarts the animation
                        if self.ultimate_attack_animation_frame > 42:
                            self.ultimate_attack_animation_frame= 0
                            #it makes special attacking animation false so that once the animation is finsihed the player will not automatically attack again
                            #since the attack is going to stop that means the enemy's are no longer being attacked and will be able to move again
                            #if the enemy has been attacked he wont move back to the player again until he has finished attacking
                            #it also takes the players energy
                            self.ultimate_attacking = False
                            self.energy -= 150
                            enemy1.attacked = False
                            enemy2.attacked = False
                            enemy3.attacked = False
                            enemy4.attacked = False
                            enemy5.attacked = False
                            enemy6.attacked = False
                        self.special_attack_image = special_attack[self.ultimate_attack_animation_frame]
                        self.special_attack_image = pygame.transform.scale(self.special_attack_image,(int(self.special_attack_image.get_width() * self.scale),
                                                                                                      int(self.special_attack_image.get_height() * self.scale)))
                        #this will flip the image to be in the oppostie direction
                        self.special_right_attack_image = pygame.transform.flip(self.special_attack_image,True,False)
                #this will be taking each frame from the player dead animation list and scaling the image
                def player_dead_animation(self):                
                        self.player_dead_image = dead[self.player_dead_animation_frame]
                        self.player_dead_image = pygame.transform.scale(self.player_dead_image,(int(self.player_dead_image.get_width() * self.scale),
                                                                                                int(self.player_dead_image.get_height() * self.scale)))
                        #this will flip the image to be in the oppostie direction
                        self.player_dead_right_image = pygame.transform.flip(self.player_dead_image,True,False)

                def player_death(self):
                        if self.player_in_air == False:
                                self.player_dying = True
                                self.animation_speed = 800

                #this method is used to increment the frames of the animation that is being played
                def animation(self):
                    #if the player is not bbeing hit then an animation will be played
                    if self.collision == False:
                            #this will get the current time since the game has been opened
                            current_time = pygame.time.get_ticks()
                            #last updated would be the last time the frame in the animation had changed and the animation speed will control how long
                            #each frame is shown on the screen
                            if current_time - self.last_updated > self.animation_speed:
                                self.last_updated = current_time
                                self.idle_animation_frame +=1
                                if self.special_attacking == True or self.normal_attacking == True:
                                    self.attack_animation_frame +=1
                                if self.ultimate_attacking == True:
                                    self.ultimate_attack_animation_frame +=1
                                if self.player_dying == True:
                                        if self.player_dead_animation_frame == 0:
                                              self.player_dead_animation_frame += 1
                #this method is called when the player presses space bar
                def player_jump(self):
                        if self.player_in_air == False:
                                self.jump = True
                        
                def movement(self):
                        #it will check if the player is not dead and is not attacking then it will check if the player wants to jump or move
                        if self.normal_attacking == False and self.special_attacking == False and self.ultimate_attacking == False and self.player_dying == False:
                                if self.moving_right == True and self.collision == False:
                                        #this will make the player constantly increase the x coordinates for as long as they press the D key
                                        self.speed = 2.5
                                        self.x += self.speed
                                        self.facing_right = True
                                if self.moving_left == True and self.collision == False:
                                    #this will make the player constantly decrease the x coordinate for as long as they press the A key
                                        self.speed = -2.5
                                        self.x += self.speed
                                        self.facing_right = False
                                if self.jump == True:
                                        #this will make it so that when the player jumps he will increase his y coordinate until it is no longer true
                                        self.y_speed = 3
                                        self.y -= self.y_speed
                                        self.jump_height += 1
                                        #once the player has travelled a certain height it will need to be tracked and the player will then need to fall back down 
                                        if self.jump_height == 100:
                                                #jump is now false as the player cannot go any height anymore
                                                self.jump = False
                                                self.jump_height = 0
                                                self.player_in_air = True
                                #this will make the player fall down and the y coordinates will decrease until is no longer true
                                if self.player_in_air == True:
                                        self.y_speed = -3
                                        self.y -= self.y_speed
                                       
                #this method is responsible for keeping tracking of what actions the player is performing and diaplaying them to the user at the player's coordinates
                #this method will also be responsible for changing the hitbox of the player to whatever action the player is performing on the screen
                def draw_image(self):
                    if self.moving_right == True and self.special_attacking == False and self.normal_attacking == False and self.ultimate_attacking == False and self.player_dying == False and self.collision == False:
                        self.player_rect = self.rect
                        screen.blit(self.moving_right_image,(self.x-170,self.y-47))
                    if self.moving_left == True and self.special_attacking == False and self.normal_attacking == False and self.ultimate_attacking == False and self.player_dying == False and self.collision == False:
                        self.player_rect = self.rect
                        screen.blit(self.moving_left_image,(self.x-50,self.y-47))
                    if self.special_attacking == True and self.player_dying == False and self.collision == False or self.normal_attacking == True and self.player_dying == False and self.collision == False:
                        if self.facing_right == False:
                                screen.blit(self.attack_image,(self.x-250,self.y-183))
                                self.player_rect = self.special_attacking_rect
                        if self.facing_right == True:
                                self.player_rect = self.special_attacking_right_rect 
                                screen.blit(self.attack_right_image,(self.x-200,self.y-183))     
                    if self.ultimate_attacking == True and self.player_dying == False and self.collision == False:
                        if self.facing_right == False:
                                screen.blit(self.special_attack_image,(self.x-550,self.y-225))
                                self.player_rect = self.ultimate_attacking_rect
                        if self.facing_right == True:
                                screen.blit(self.special_right_attack_image,(self.x-317,self.y-225))
                                self.player_rect = self.ultimate_attacking_right_rect
                    if self.player_dying == True or self.collision == True:
                        self.player_rect = self.rect
                        if self.facing_right == False:
                                screen.blit(self.player_dead_image,(self.x-125,self.y-25))
                        if self.facing_right == True:
                                screen.blit(self.player_dead_right_image,(self.x-65,self.y-25))
                    if self.moving_left == False and self.moving_right == False and self.normal_attacking == False and self.special_attacking == False and self.ultimate_attacking == False and self.player_dying == False and self.collision == False:
                        if self.facing_right == False:
                                self.player_rect = self.rect
                                screen.blit(self.idle_image,self.player_rect)
                        if self.facing_right == True:
                                screen.blit(self.idle_right_image,(self.x-150,self.y-65))
                                self.player_rect = self.rect
                    
                #this will call all the player methods that need to be called for player object to peform actions
                def call_player_methods(self):
                        self.ultimate_attack_animation()
                        self.attack_animation()
                        self.player_dead_animation()
                        self.idle_animation()
                        self.move()
                        self.rectangle()
                        self.movement()
                        self.healthbar()
                        self.energy_bar()
                        self.display_score()
                        self.animation()
                        self.draw_image()


        #this class will be creating the enemy that will try and kill the player the enemy will automatically move on its own and attack the player                    
        class enemy():
                def __init__(self,x,y,health):
                        self.x = x
                        self.y = y
                        self.health = health
                        self.old_health = 0
                        self.last_updated = 0
                        self.speed = 0
                        self.scale = 2
                        self.enemy_animation_speed = 175
                        self.damage = 0
                        self.collision = False
                        self.attacked = False
                        self.enemy_dying = False
                        self.enemy_idle_animation_frame = 0
                        self.enemy_special_attack_animation_frame = 0
                        self.enemy_attack_animation_frame = 0
                        self.enemy_dead_animation_frame = 0
                        self.enemy_run_animation_frame = 0
                        self.moving_right = False
                        self.moving_left = False
                        self.facing_right = False
                        self.facing_left = False
                        self.enemy_special_attacking = False
                        self.enemy_attacking = False
                        self.enemy_dying = False

                #this method will create all the hitboxes of the enemies using rectangles as well as the attack range of the enemy
                def enemy_rectangle(self):
                    self.rect = self.enemy_idle_image.get_rect()
                    self.rect.center = (self.x,self.y+10)

                    self.enemy_attacking_rect = self.enemy_attack_image.get_rect()
                    self.enemy_attacking_rect.center = (self.x-70,self.y)

                    self.enemy_attack_right_rect  = self.enemy_attack_right_image.get_rect()
                    self.enemy_attack_right_rect.center = (self.x+80,self.y)

                    self.enemy_special_attacking_rect = self.enemy_special_attack_image.get_rect()
                    self.enemy_special_attacking_rect.center = (self.x,self.y)

                    self.enemy_attack_range_rect = pygame.Rect(self.x-125,self.y,250,10)
                #this method will create a healthbar above the enemy
                def healthbar(self):
                    self.health_rect = pygame.Rect(self.x - 50,self.y - 70,self.health / 2,10)
                    pygame.draw.rect(screen,(100,0,0),(self.x -50,self.y-70,100,10))
                    pygame.draw.rect(screen,(0,75,0),self.health_rect)
                #this method is used how the hitbox of the enemy works and it will control how far back the enemy is knocked back from the player's attacks
                def hitbox(self):
                        if player.collision == False:
                                #during these frames of the attack animation the player will perform a slash attack
                                if player.attack_animation_frame >= 4 or player.ultimate_attack_animation_frame >= 20:
                                    if self.rect.colliderect(player.player_rect):
                                                self.collision = True
                                                self.attacked = True
                                    #if the player and enemy hitbox collide and the player is attacking the enemy will be knocked back
                                    if self.collision == True:
                                        if self.enemy_rect.centerx < player.rect.centerx:
                                                    self.x -= 1.7
                                        if self.enemy_rect.centerx > player.rect.centerx:
                                                    self.x += 1.7
                                        #this will control how far back the enemy is knocked back from a special attack
                                        if player.special_attacking == True:
                                                    if self.enemy_rect.centerx > player.player_rect.centerx + 400 or self.enemy_rect.centerx< player.player_rect.centerx - 400:
                                                                self.collision = False
                                                                self.old_health = self.health
                                        #this will control how far back the enemy is knocked back from a notmal attack
                                        if player.normal_attacking == True:
                                                    if self.enemy_rect.centerx > player.player_rect.centerx + 300 or self.enemy_rect.centerx< player.player_rect.centerx - 300:
                                                                self.collision = False
                                                                self.old_health = self.health
                                                    else:
                                                                if self.enemy_rect.centerx < player.rect.centerx:
                                                                            self.x -= 2
                                                                if self.enemy_rect.centerx > player.rect.centerx:
                                                                            self.x += 2
                                         #this will control how far back the enemy is knocked back from an ultimate attack
                                        if player.ultimate_attacking == True:
                                            if self.enemy_rect.centerx > player.player_rect.centerx + 520 or self.enemy_rect.centerx < player.player_rect.centerx - 520:
                                                            self.collision = False
                                                            self.old_health = self.health
                                    #this will make sure if the hitboxes collide the enemy's hp is reduced only once during the collision 
                                    if self.health == self.old_health:
                                                            self.health = self.health - player.damage
                                    #this will be checking for when the enemy's hp falls below 0
                                    if self.health <= 0:
                                            self.health = 0 
                                            self.enemy_dying = True
                                            self.animation_speed = 800
                #this will control the player's hitbox and how far back he is knocked back by the enemy
                def player_hitbox(self):
                    #it will first check if the 2 hitboxes are colliding
                    if player.normal_attacking == False and player.special_attacking == True and player.ultimate_attacking == True:
                          if player.player_rect.colliderect(self.enemy_rect):
                                   player.collision == True
                    if player.normal_attacking == True and self.enemy_attacking == True and player.special_attacking == False and player.ultimate_attacking == False and player.player_dying == False:
                        if player.player_rect.colliderect(self.enemy_rect):
                                    player.collision = True
                            
                    if player.normal_attacking == False and player.special_attacking == False and player.ultimate_attacking == False and player.player_dying == False:
                        if player.player_rect.colliderect(self.enemy_rect):
                                    player.collision = True
                    #if the hitboxes are colliding and the player is not ultimate or special attacking he will be knocked back
                    if player.collision == True:
                                    if player.player_rect.centerx < self.rect.centerx:
                                               player.x -= 1
                                    if player.player_rect.centerx > self.rect.centerx:
                                                player.x += 1
                                    if player.health == player.old_health:
                                                    player.health = player.health - self.damage
                    #this will control how far the player is knocked back for running into the enemy
                    if self.enemy_special_attacking == False and self.enemy_attacking == False:
                                if player.player_rect.centerx +45 < self.enemy_rect.centerx -151 or player.player_rect.centerx -45 > self.enemy_rect.centerx + 151:
                                       player.collision = False
                                       player.old_health = player.health
                    #this will control how far the player is knocked back by the enemy attack
                    if self.enemy_attacking == True :
                                 if player.player_rect.centerx +45 < self.enemy_rect.centerx -234 or player.player_rect.centerx -45 > self.enemy_rect.centerx + 234:
                                       player.collision = False
                                       player.old_health = player.health
                    #this will control how far the player is knocked back by the enemy special attack
                    if self.enemy_special_attacking == True:
                                if player.player_rect.centerx +45 < self.enemy_rect.centerx -400 or player.player_rect.centerx -45 > self.enemy_rect.centerx + 400:
                                       player.collision = False
                                       player.old_health = player.health
                    #this will be checking to see if the player's health falls below 0 meaning he has died
                    if player.health <= 0:
                                player.health = 0
                                player.player_dying = True
                                player.animation_speed = 800
               #this method will control the animation to make sure it is reset when the final frame is reached
                def enemy_run_animation(self):
                        if self.enemy_run_animation_frame > 5:
                            self.enemy_run_animation_frame = 0
                        self.enemy_run_right_image = enemy_run[self.enemy_run_animation_frame]
                        self.enemy_run_right_image = pygame.transform.scale(self.enemy_run_right_image,(int(self.enemy_run_right_image.get_width() * self.scale),
                                                                                                        int(self.enemy_run_right_image.get_height() * self.scale)))
                        #this will flip the image to be in the oppostie direction
                        self.enemy_run_left_image = pygame.transform.flip(self.enemy_run_right_image,True,False)

                #this method will control if the enemy's x coordinates will increase or decrease depending on which direction the enemy wants to travel               
                def enemy_movement(self):
                        if self.moving_right == True and self.enemy_attacking == False and self.enemy_special_attacking == False:
                                self.facing_right = True
                                self.facing_left = False
                                self.speed = 1.3
                                self.x += self.speed
                        if self.moving_left == True and self.enemy_attacking == False and self.enemy_special_attacking == False:
                                self.facing_left = True
                                self.facing_right = False
                                self.speed = 1.3
                                self.x -= self.speed
                #this method will be checking if the player is on the right side of the enemy or the left side of the enemy
                #if he is on the left side the enemy will move left if he is on the right side the enemy will move to the right
                def AI(self):
                    if resume.paused == False:
                        if player.x + 90 < self.x and player.collision == False and self.attacked == False and self.enemy_dying == False: 
                                self.moving_left = True
                        elif player.x - 90 > self.x and player.collision == False and self.attacked == False and self.enemy_dying == False:
                                self.moving_right = True
                        else:
                                self.moving_right = False
                                self.moving_left = False

                #if the player gets within the enemy attack range the enemy will attack
                def attack_AI(self):
                        if self.enemy_attack_range_rect.colliderect(player.rect) and player.player_in_air == False and self.enemy_dying == False :
                                self.enemy_attacking = True

                #this will control the enemy idle animation making sure the frame of the animation resets when needed
                def enemy_idle_animation(self):
                        if self.enemy_idle_animation_frame > 11:
                                self.enemy_idle_animation_frame = 0
                        self.enemy_idle_image = enemy_idle[self.enemy_idle_animation_frame]
                        self.enemy_idle_image = pygame.transform.scale(self.enemy_idle_image,(int(self.enemy_idle_image.get_width() * self.scale),
                                                                                              int(self.enemy_idle_image.get_height() * self.scale)))
                        #this will flip the image to be in the oppostie direction
                        self.enemy_idle_right_image = pygame.transform.flip(self.enemy_idle_image,True,False)
                def enemy_special_attack(self):
                    self.enemy_special_attacking = True
                    self.enemy_attacking = False

                #this will control the special attack animation and making sure the frame of the animation resets when needed
                def special_attack_animation(self):
                        if self.enemy_special_attack_animation_frame > 20:
                            self.enemy_special_attack_animation_frame = 0
                            self.enemy_special_attacking = False
                        self.enemy_special_attack_image = enemy_special_attack[self.enemy_special_attack_animation_frame]
                        self.enemy_special_attack_image = pygame.transform.scale(self.enemy_special_attack_image,(int(self.enemy_special_attack_image.get_width() * self.scale),
                                                                                                                  int(self.enemy_special_attack_image.get_height() * self.scale)))
                def enemy_attack(self):
                    self.enemy_attacking = True
                    self.enemy_special_attacking = False
                #this mehod is used to control the attack animation of the enemy making sure the frame of the animation resets when needed
                def attack_animation(self):
                        if self.enemy_attack_animation_frame > 4:
                            self.enemy_attack_animation_frame = 0
                            self.enemy_attacking = False
                        self.enemy_attack_image = enemy_attack[self.enemy_attack_animation_frame]
                        self.enemy_attack_image = pygame.transform.scale(self.enemy_attack_image,(int(self.enemy_attack_image.get_width() * self.scale),
                                                                                                  int(self.enemy_attack_image.get_height() * self.scale)))
                        #this will flip the image to be in the oppostie direction
                        self.enemy_attack_right_image = pygame.transform.flip(self.enemy_attack_image,True,False)
                def enemy_dead_animation(self):                
                        self.enemy_dead_image = enemy_dead[self.enemy_dead_animation_frame]
                        self.enemy_dead_image = pygame.transform.scale(self.enemy_dead_image,(int(self.enemy_dead_image.get_width() * self.scale),
                                                                                              int(self.enemy_dead_image.get_height() * self.scale)))
                def enemy_death(self):
                        self.enemy_dying = True
                        self.enemy_animation_speed = 800        
                #this will be responsible for incrementing each animation frame by 1 and making sure that each frame is displayed for a certain amount of time
                def animation(self):
                    current_time = pygame.time.get_ticks()
                    if current_time - self.last_updated > self.enemy_animation_speed:
                        self.last_updated = current_time
                        self.enemy_idle_animation_frame += 1
                        if self.moving_right == True or self.moving_left == True:
                                self.enemy_run_animation_frame +=1
                        if self.enemy_special_attacking == True:
                            self.enemy_special_attack_animation_frame +=1
                        if self.enemy_attacking == True:
                            self.enemy_attack_animation_frame +=1
                        if self.enemy_dying == True:
                                #if the enemy dies the player's score and energy will increase
                                player.score += 500
                                player.energy += 20
                                if self.enemy_dead_animation_frame == 0:
                                       self.enemy_dead_animation_frame += 1

                #this method will be responsible for displaying the images of the enemy and its actions on to the screen
                #it will also change the hitbox of the enemy to whatever action they area performing
                def draw_enemy_image(self):
                    if self.moving_right == True and self.enemy_attacking == False and self.enemy_special_attacking == False and self.enemy_dying == False and self.collision == False:
                        screen.blit(self.enemy_run_right_image,(self.x-60,self.y-55))
                        self.enemy_rect = self.rect
                    if self.moving_left == True and self.enemy_attacking == False and self.enemy_special_attacking == False and self.enemy_dying == False and self.collision == False:
                            screen.blit(self.enemy_run_left_image,(self.x-80,self.y-55))
                            self.enemy_rect = self.rect
                    if self.moving_right == False and self.moving_left == False and self.enemy_special_attacking == False and self.enemy_attacking == False and self.enemy_dying == False and self.collision == False:
                            if self.facing_left == True:
                                    screen.blit(self.enemy_idle_image,(self.rect))
                            if self.facing_right == True:
                                    screen.blit(self.enemy_idle_right_image,(self.rect))
                            self.enemy_rect = self.rect
                            self.damage = 10
                    if self.enemy_special_attacking == True and self.collision == False:
                        screen.blit(self.enemy_special_attack_image,(self.x-300,self.y-75))
                        self.enemy_rect = self.enemy_special_attacking_rect
                        self.damage = 40
                    if self.enemy_attacking == True and self.collision == False:
                        if self.facing_left == True:
                                screen.blit(self.enemy_attack_image,(self.x-205,self.y-50))
                                self.enemy_rect = self.enemy_attacking_rect
                        if self.facing_right == True:
                                screen.blit(self.enemy_attack_right_image,(self.x-50,self.y-50))
                                self.enemy_rect = self.enemy_attack_right_rect
                        self.damage = 25
                    if self.enemy_dying == True or self.collision == True:
                        self.enemy_rect = self.rect
                        screen.blit(self.enemy_dead_image,(self.x-90,self.y-25))

                #this method will call all the other methods needed for the object to perform its needed actions
                #since i will be creating many enemy's as object instead of calling every method every time i only need to call this method which
                #will call all the other needed methods
                def call_enemy_methods(self):
                        self.enemy_idle_animation()
                        self.enemy_run_animation()
                        self.attack_animation()
                        self.enemy_dead_animation()
                        self.special_attack_animation()
                        self.enemy_rectangle()
                        self.healthbar()
                        self.hitbox()
                        self.AI()
                        self.enemy_movement()
                        self.animation()
                        self.draw_enemy_image()

        #this method is used to create the illusion that there is a a camera that is following the player 
        class camera():
            def __init__(self,camera_shift):
                self.camera_shift = camera_shift
                self.world_shift = 0
            #this method will keep track of how much the camera has moved and how much the world has been shifter by so that when the world has shifted
            #a certain amount then platforms will appear
            def scroll_background(self):
                if player.x < 30:
                    player.x -= player.speed
                #if the player is on the left side of the screen every objects x coordinate will increase shifting everything to the right
                #the player will not actually be but the world itself is just shift whist this is happeneing
                if player.x < 500 and player.moving_left == True:
                    player.x += self.camera_shift
                    floor.x += self.camera_shift
                    sender_public_key.x += self.camera_shift
                    sender_private_key.x += self.camera_shift
                    recipient_public_key.x += self.camera_shift
                    recipient_private_key.x += self.camera_shift
                    message.x += self.camera_shift
                    puzzles_text.x += self.camera_shift
                    senders_key_text.x += self.camera_shift
                    recipients_key_text.x += self.camera_shift
                    recipient.x += self.camera_shift
                    self.world_shift += self.camera_shift

                    enemy1.x += self.camera_shift
                    enemy2.x += self.camera_shift
                    enemy3.x += self.camera_shift
                    enemy4.x += self.camera_shift
                    enemy5.x += self.camera_shift
                    enemy6.x += self.camera_shift

                    stone_platform1.x += self.camera_shift
                    stone_platform2.x += self.camera_shift
                    stone_platform3.x += self.camera_shift
                    stone_platform4.x += self.camera_shift
                    stone_platform5.x += self.camera_shift
                    stone_platform6.x += self.camera_shift
                    stone_platform7.x += self.camera_shift
                    stone_platform8.x += self.camera_shift
                    stone_platform9.x += self.camera_shift
                    stone_platform10.x += self.camera_shift
                    stone_platform11.x += self.camera_shift
                    stone_platform12.x += self.camera_shift
                    stone_platform13.x += self.camera_shift
                    stone_platform14.x += self.camera_shift
                    stone_platform15.x += self.camera_shift
                    stone_platform16.x += self.camera_shift
                    stone_platform17.x += self.camera_shift
                    stone_platform18.x += self.camera_shift
                    stone_platform19.x += self.camera_shift
                    stone_platform20.x += self.camera_shift
                    stone_platform21.x += self.camera_shift
                    stone_platform22.x += self.camera_shift
                    stone_platform23.x += self.camera_shift
                    stone_platform24.x += self.camera_shift

                #if the player is on the right side of the screen every objects x coordinate will decrease shifting everything to the left
                #the player will not actually be but the world itself is just shift whist this is happeneing                  

                if player.x > 1000 and player.moving_right == True :
                    floor.x -= self.camera_shift
                    sender_public_key.x -= self.camera_shift
                    sender_private_key.x -= self.camera_shift
                    recipient_public_key.x -= self.camera_shift
                    recipient_private_key.x -= self.camera_shift
                    message.x -= self.camera_shift
                    puzzles_text.x -= self.camera_shift
                    senders_key_text.x -= self.camera_shift
                    recipients_key_text.x -= self.camera_shift
                    recipient.x -= self.camera_shift
                    self.world_shift -= self.camera_shift           
                    player.x -= self.camera_shift

                    enemy1.x -= self.camera_shift
                    enemy2.x -= self.camera_shift
                    enemy3.x -= self.camera_shift
                    enemy4.x -= self.camera_shift
                    enemy5.x -= self.camera_shift
                    enemy6.x -= self.camera_shift

                    stone_platform1.x -= self.camera_shift
                    stone_platform2.x -= self.camera_shift
                    stone_platform3.x -= self.camera_shift
                    stone_platform4.x -= self.camera_shift
                    stone_platform5.x -= self.camera_shift
                    stone_platform6.x -= self.camera_shift
                    stone_platform7.x -= self.camera_shift
                    stone_platform8.x -= self.camera_shift
                    stone_platform9.x -= self.camera_shift
                    stone_platform10.x -= self.camera_shift
                    stone_platform11.x -= self.camera_shift
                    stone_platform12.x -= self.camera_shift
                    stone_platform13.x -= self.camera_shift
                    stone_platform14.x -= self.camera_shift
                    stone_platform15.x -= self.camera_shift
                    stone_platform16.x -= self.camera_shift
                    stone_platform17.x -= self.camera_shift
                    stone_platform18.x -= self.camera_shift
                    stone_platform19.x -= self.camera_shift
                    stone_platform20.x -= self.camera_shift
                    stone_platform21.x -= self.camera_shift
                    stone_platform22.x -= self.camera_shift
                    stone_platform23.x -= self.camera_shift
                    stone_platform24.x -= self.camera_shift

        #this class will be responsible for creating the platforms on the screen and the collisons for each platform                   
        class level():
                def __init__(self,x,y,width,height):
                        self.x = x
                        self.y = y
                        self.width = width
                        self.height = height
                        self.player_collision = False
                        self.stone_platform_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                        self.public_key_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                        self.message_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                        self.recipient_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                        self.starting_floor_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                        self.ceiling_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                        self.delete_key = False
                        self.delete_message = False
                        self.drop = False
                        self.encrypt_message = False
                        self.message_recieved = False
                        self.decrypt_message = False
               #this will create the rectangle around the starting floor
                def rectangle(self):
                        self.starting_floor_rect = pygame.Rect(self.x,self.y+10,self.width,self.height)
                        
                #this will draw a long horizontal platform
                def draw_long_platform(self):
                        stone_platform = pygame.image.load("images/level/dungeon_platform1.xcf")
                        self.stone_platform_rect = pygame.Rect(self.x,self.y+10,self.width,self.height)
                        
                        screen.blit(stone_platform,(self.x,self.y))

                #this will draw a medium sized horizontal platform
                def draw_medium_platform(self):
                        stone_platform = pygame.image.load("images/level/dungeon_platform3.xcf")
                        self.stone_platform_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                        screen.blit(stone_platform,(self.x,self.y))

                def draw_small_platform(self):
                        stone_platform = pygame.image.load("images/level/dungeon_platform2.xcf")
                        self.stone_platform_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                        #pygame.draw.rect(screen,(0,0,0),self.stone_platform_rect)
                        screen.blit(stone_platform,(self.x,self.y))

                def draw_long_vertical_platform_down(self):
                        stone_platform = pygame.image.load("images/level/dungeon_platform4.xcf")
                        self.stone_platform_rect = pygame.Rect(self.x,self.y+10,self.width,self.height)
                        #pygame.draw.rect(screen,(0,0,0),self.stone_platform_rect)
                        screen.blit(stone_platform,(self.x,self.y))

                def draw_long_vertical_platform_up(self):
                        stone_platform = pygame.image.load("images/level/dungeon_platform4.xcf")
                        stone_platform = pygame.transform.flip(stone_platform,False,True)
                        self.stone_platform_rect = pygame.Rect(self.x,self.y+15,self.width,self.height)
                        pygame.draw.rect(screen,(0,0,0),self.stone_platform_rect)
                        screen.blit(stone_platform,(self.x,self.y))
               #this will draw a key onto the screen
               #it will also create a rectangle so that it can be picked up and dropped
                def key(self):
                    public_key = pygame.image.load("images/level/key.xcf")
                    self.public_key_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                    #pygame.draw.rect(screen,(255,255,255),self.public_key_rect)
                    screen.blit(public_key,(self.x,self.y,self.width,self.height))
                #this will help the user identify that this is the area that the encrypted message needs to be delivered to
                def recipient_text(self):
                    self.font = pygame.font.SysFont('franklingothicmedium', 40, True)
                    sender_keys_text = self.font.render("Recipient",1,(255,255,255))
                    screen.blit(sender_keys_text,(self.x+25,self.y-50))
                #this will create a rectangle which will be used to see if the encrypted message is delivered to the recipient                
                def recipient_box(self):
                    self.recipient_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                    #pygame.draw.rect(screen,(255,255,255),(self.recipient_rect))
                    if self.message_recieved  == False:
                        pygame.draw.rect(screen,(255,255,255),(self.recipient_rect), 3)
                    if self.message_recieved == True:
                            pygame.draw.rect(screen,(0,75,0),(self.recipient_rect), 3)
                #this is used to show that the key is a public key                        
                def public_key_text(self):
                    self.font = pygame.font.SysFont('franklingothicmedium', 20, True)
                    public_key_text = self.font.render("public key",1,(255,255,255))
                    screen.blit(public_key_text,(self.x,self.y-15))
                #this is used to show that the key is a private key
                def private_key_text(self):
                    self.font = pygame.font.SysFont('franklingothicmedium', 20, True)
                    private_key_text = self.font.render("private key",1,(255,255,255))
                    screen.blit(private_key_text,(self.x,self.y-15))
                #this is used to display the text before and after it is encrypted
                #it will also create a rectangle so that it can be picked up and dropped
                def message_text(self):
                    self.font = pygame.font.SysFont('franklingothicmedium', 40, True)
                    message_text = self.font.render("hello",1,(255,255,255))
                    self.message_rect = pygame.Rect(self.x,self.y,self.width,self.height)
                    pygame.draw.rect(screen,(0,0,0),self.message_rect)
                    if self.encrypt_message == False:
                        screen.blit(message_text,(self.x,self.y))
                    if self.encrypt_message == True:
                        message_text = self.font.render("zhsyg",1,(255,255,255))
                        screen.blit(message_text,(self.x,self.y))
                #this is used to see if the message needs to be decrypted by the recipient
                #if it is decrypted then the user has completed the puzzle and their score will increase
                def decrypt_text(self):
                    if self.decrypt_message == True:
                        message_text = self.font.render("hello",1,(255,255,255))
                        screen.blit(message_text,(self.x,self.y))
                        player.score += 1000
                        self.encrypt_message = False
                        self.decrypt_message = False
                #this helps the user identify that the keys underneath this text is the sender's keys
                def sender_key_text(self):
                    self.font = pygame.font.SysFont('franklingothicmedium', 30, True)
                    sender_keys_text = self.font.render("Sender's Keys",1,(255,255,255))
                    screen.blit(sender_keys_text,(self.x,self.y))
                #this helps the user identify that the keys underneath this text is the recipient's keys
                def recipient_key_text(self):
                    self.font = pygame.font.SysFont('franklingothicmedium', 30, True)
                    recipient_keys_text = self.font.render("Recipient's Keys",1,(255,255,255))
                    screen.blit(recipient_keys_text,(self.x,self.y))
                #this is used to tell the user how to solve the puzzle
                def puzzle_text(self):
                    self.font = pygame.font.SysFont('franklingothicmedium', 30, True)
                    puzzle_instruction_text = self.font.render("Act out asymmetric encryption",1,(255,255,255))
                    screen.blit(puzzle_instruction_text,(self.x,self.y))
                    puzzle_instruction1_text = self.font.render("Use F to pick up the keys",1,(255,255,255))
                    screen.blit(puzzle_instruction1_text,(self.x+50,self.y+25))
                    puzzle_instruction2_text = self.font.render("Use G to drop the keys",1,(255,255,255))
                    screen.blit(puzzle_instruction2_text,(self.x+50,self.y+50))
                #this is used to see if the player wants to pickup the message
                def pickup_message(self):
                    if self.message_rect.colliderect(player.rect) and player.pickup == True:
                        self.delete_message = True
                #this is used to see if the player wants to drop the message
                def drop_message(self):
                    player.pickup = False
                    self.drop == True
                    if self.drop == True:
                            self.delete_message = False
                            self.x = player.x
                            self.y = player.y
                            self.drop = False


                    

                #this will handle picking up the key 
                def pickup_key(self):
                    if self.public_key_rect.colliderect(player.rect) and player.pickup == True:
                        self.delete_key = True
                #this will handle dropping the key
                def drop_key(self):
                    player.pickup = False
                    self.drop == True
                    if self.drop == True:
                            self.delete_key = False
                            self.x = player.x
                            self.y = player.y
                            self.drop = False

                

                #this will handle the horizontal collision of the platform
                #if the player hits the left or right side of the platform
                def horizontal_collision(self):
                        if self.stone_platform_rect.colliderect(player.rect):
                                if player.speed > 0:
                                        self.stone_platform_rect.left = player.rect.right
                                        player.x -= player.speed
                                if player.speed < 0:
                                        self.stone_platform_rect.right = player.rect.left
                                        player.x -= player.speed
                #this will handle vertical collisions of every platform
                #if the player lands on a platform or hits it with their head
                def vertical_collision(self):
                        if self.stone_platform_rect.colliderect(player.rect):
                                if player.y + 65 <= self.stone_platform_rect.y +10:
                                        if player.y_speed < 0:
                                                self.stone_platform_rect.top = player.rect.bottom
                                                player.player_in_air = False
                                                player.speed = 0
                                if player.y - 65 >= self.stone_platform_rect.y +50:
                                        if player.y_speed > 0:
                                                self.stone_platform_rect.bottom = player.rect.top
                                                player.jump = False
                                                player.jump_height = 0
                                                player.y += 2
                                                player.speed = 0
                #this will handle the collisions with the celing to see if the player hits their head on it they will not go thorugh it and will fall back down
                def ceiling_collision(self):
                        if self.ceiling_rect.colliderect(player.rect):
                                player.player_in_air = True
                                player.jump = False
                                player.jump_height = 0
                                player.y += 2
                #this will make it so that the player will not fall throught the starting floor
                def floor_collision(self):
                        if self.starting_floor_rect.colliderect(player.player_rect):
                                player.player_in_air = False
                        elif player.jump == False:
                                player.player_in_air = True

        class buttons():
            def __init__(self,colour,x,y,width,height,text = ""):
                self.colour = colour
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.button_rect = pygame.draw.rect(screen,self.colour,(self.x,self.y,self.width,self.height))
                self.text = text
                self.clicked = False
                self.paused = False
                self.game_over = False

            #this is used to draw a button onto the screen                
            def draw_button(self):
                pygame.draw.rect(screen,(128,128,128),(self.x-2,self.y-2,self.width+4,self.height+4))
                self.button_rect = pygame.draw.rect(screen,self.colour,(self.x,self.y,self.width,self.height))
                self.font = pygame.font.SysFont('franklingothicmedium', 70, True)
                button_text = self.font.render(str(self.text),1,(0,0,0))
                screen.blit(button_text,(self.x+50,self.y-5))

             #this will keep track of the mouse on the screen and see if it hovers above the button and clikcs it
            def click_button(self):
                pos = pygame.mouse.get_pos()
                if self.button_rect.collidepoint(pos):
                    if self.clicked == True:
                        if self.paused == True:
                            self.paused = False
                        elif exit_button.clicked == True:
                                pygame.quit()
                        else:
                                game_over1 = True

        #this class will display the questions on to the screen for the user to answer and keep randomly pciking different questions
        class questions():
                def __init__(self):
                        self.level_id = 1
                        self.clicked = False
                        self.number_of_correct_answers = 0
                        self.click_time = 0
                        #self.current_time = 0
                        self.pos = pygame.mouse.get_pos()
                        self.answer_correct = False
                        self.new_question = False
                        
                        
                #this will randomly pick a question from the questions stored in the data base
                def select_level_questions(self):
                    self.select_level_question = (cursor.execute("SELECT Question_text FROM question WHERE LEVEL_ID = (?)",(str(self.level_id))).fetchall())
                    database.commit()
                    self.random_question_select = random.choice(range(1,len(self.select_level_question)))
                    self.level_questions = self.select_level_question[self.random_question_select-1][0]

                 #this will get the question id of the selected question
                def get_question_id(self):
                    self.get_question_id1 = cursor.execute("SELECT Question_ID FROM question WHERE Question_text = (?)",(self.level_questions,)).fetchall()
                    database.commit()
                    self.question_id = self.get_question_id1[0][0]
               #this will get the options of the selected question
                def select_options(self):
                    self.select_question_options = cursor.execute("SELECT option_A,option_B,option_C FROM question_choice WHERE QUESTION_ID = (?)",(self.question_id,)).fetchall()
                    database.commit()
                    self.option_a = self.select_question_options[0][0]
                    self.option_b = self.select_question_options[0][1]                                              
                    self.option_c = self.select_question_options[0][2]
                #this will display the question chosen onto the screen                                                              
                def display_questions(self):
                        pygame.draw.rect(screen,(128,128,128),(198,148,1004,79))
                        self.question_rect = pygame.draw.rect(screen,(0,0,0),(200,150,1000,75))
                        self.font = pygame.font.SysFont('franklingothicmedium', 20, True)
                        self.show_question = self.font.render("Question:",1,(255,255,255))
                        screen.blit(self.show_question,(210,155))
                        self.question_text = self.font.render(self.level_questions,1,(255,255,255))
                        screen.blit(self.question_text,(210,185))

                #this will display the first option to the question onto the screen
                def display_option_a(self):
                        pygame.draw.rect(screen,(128,128,128),(198,273,1004,79))
                        self.option_a_rect = pygame.draw.rect(screen,(0,0,0),(200,275,1000,75))
                        self.font = pygame.font.SysFont('franklingothicmedium', 20, True)
                        self.show_question = self.font.render("A)",1,(255,255,255))
                        screen.blit(self.show_question,(210,280))
                        self.option_a_text = self.font.render(self.option_a,1,(255,255,255))
                        screen.blit(self.option_a_text,(235,280))

                #this will display the second option to the question onto the screen
                def display_option_b(self):
                        pygame.draw.rect(screen,(128,128,128),(198,398,1004,79))
                        self.option_b_rect = pygame.draw.rect(screen,(0,0,0),(200,400,1000,75))
                        self.font = pygame.font.SysFont('franklingothicmedium', 20, True)
                        self.show_question = self.font.render("B)",1,(255,255,255))
                        screen.blit(self.show_question,(210,405))
                        self.option_b_text = self.font.render(self.option_b,1,(255,255,255))
                        screen.blit(self.option_b_text,(235,405))

                #this will display the third option to the question onto the screen
                def display_option_c(self):
                        pygame.draw.rect(screen,(128,128,128),(198,523,1004,79))
                        self.option_c_rect = pygame.draw.rect(screen,(0,0,0),(200,525,1000,75))
                        self.font = pygame.font.SysFont('franklingothicmedium', 20, True)
                        self.show_question = self.font.render("C)",1,(255,255,255))
                        screen.blit(self.show_question,(210,530))
                        self.option_c_text = self.font.render(self.option_c,1,(255,255,255))
                        screen.blit(self.option_c_text,(235,530))

                #this will keep track of the the mouse to see which option the user hovers on and clicks
                def click_option(self):
                        if self.clicked == False:
                                self.click_time = pygame.time.get_ticks()
                                self.pos = pygame.mouse.get_pos()
                        if self.option_a_rect.collidepoint(self.pos) or self.option_b_rect.collidepoint(self.pos) or self.option_c_rect.collidepoint(self.pos):
                            if self.clicked == True:
                                self.check_answer_correct()
                 #this method will see which option the user chose and compare it to the answer stored in the database and will tell them if
                  # they are correct or incorrect
                def check_answer_correct(self):
                        self.get_answer = cursor.execute("SELECT answer FROM answer WHERE QUESTION_ID = (?)",(self.question_id,)).fetchall()
                        database.commit()
                        self.answer = self.get_answer[0][0]
                        self.font = pygame.font.SysFont('franklingothicmedium', 50, True)
                        self.correct_answer = self.font.render("Correct",1,(255,255,255))
                        self.incorrect_answer = self.font.render("incorrect",1,(255,255,255))
                        if self.option_a_rect.collidepoint(self.pos):
                                if self.answer == "a":
                                        self.answer_correct = True
                                        screen.blit(self.correct_answer,(210,75))
                                        self.new_question = True
                                        self.generate_new_question()
                                else:
                                        screen.blit(self.incorrect_answer,(210,75))
                                        self.new_question = True
                                        self.generate_new_question()

                        if self.option_b_rect.collidepoint(self.pos):
                                if self.answer == "b":
                                        self.answer_correct = True
                                        screen.blit(self.correct_answer,(210,75))
                                        self.new_question = True
                                        self.generate_new_question()
                                        
                                else:
                                        screen.blit(self.incorrect_answer,(210,75))
                                        self.new_question = True
                                        self.generate_new_question()
                                        

                        if self.option_c_rect.collidepoint(self.pos):
                                if self.answer == "c":
                                        self.answer_correct = True
                                        screen.blit(self.correct_answer,(210,75))
                                        self.new_question = True
                                        self.generate_new_question()
                                        
                                else:
                                        screen.blit(self.incorrect_answer,(210,75))
                                        self.new_question = True
                                        self.generate_new_question()
                                        
                #after the question is answered it will reamin on the screen for about 3 seconds telling the user if they are correct or not and then a new question is
                #picked and the question and its choices are shown
                def generate_new_question(self):
                        self.current_time = pygame.time.get_ticks()
                        if self.current_time - self.click_time > 3000:
                                self.clicked = False
                                if self.new_question == True:
                                        self.select_level_questions()
                                        self.get_question_id()
                                        self.select_options()
                                        self.new_question = False
                                #this will keep track of how many questions the user has gotten corect in the sections and increase their score and energy
                                #for getting the question correct or making them lose score and hp
                                if self.answer_correct == True:
                                        player.score += 300
                                        player.energy += 25
                                        self.number_of_correct_answers +=1
                                        self.answer_correct = False
                                else:
                                        player.score -= 200
                                        player.health -= 10

        #when the game is paused no movement will be allowed
        #this function will restrict all movement and attacks from the player and the enemy
        def pause_game():
                player.moving_left = False
                player.moving_right = False
                player.jump = False
                player.attacking = False
                player.normal_attacking = False
                player.special_attacking = False

                enemy1.moving_right = False
                enemy1.moving_left = False
                enemy1.enemy_attacking = False
                enemy1.enemy_special_attacking = False

                enemy2.moving_right = False
                enemy2.moving_left = False
                enemy2.enemy_attacking = False
                enemy2.enemy_special_attacking = False

                enemy3.moving_right = False
                enemy3.moving_left = False
                enemy3.enemy_attacking = False
                enemy3.enemy_special_attacking = False

                enemy4.moving_right = False
                enemy4.moving_left = False
                enemy4.enemy_attacking = False
                enemy4.enemy_special_attacking = False

                enemy5.moving_right = False
                enemy5.moving_left = False
                enemy5.enemy_attacking = False
                enemy5.enemy_special_attacking = False

                enemy6.moving_right = False
                enemy6.moving_left = False
                enemy6.enemy_attacking = False
                enemy6.enemy_special_attacking = False

        #once the player dies,falls off the map or defeats  all the enemies the game over screen will be shown
        #it will show their score and previous high score and if their new score is higher than the previous high score the new
        #high score will be recorded in the database
        def game_over_screen():
                paused = True
                font = pygame.font.SysFont('franklingothicmedium',100, True)
                game_over_text = font.render("GAME OVER",1,(255,255,255))
                screen.blit(game_over_text,(400,150))
                font = pygame.font.SysFont('franklingothicmedium',50, True)
                score_text = font.render("Score:",1,(255,255,255))
                screen.blit(score_text,(600,300))
                score_number_text = font.render(str(player.score),1,(255,255,255))
                screen.blit(score_number_text,(800,300))
                high_score_text = font.render("High Score:",1,(255,255,255))
                screen.blit(high_score_text,(600,400))

                get_username_id = cursor.execute("SELECT USER_ID FROM users WHERE username = (?)",(menu.username_info,)).fetchall()
                database.commit()
                
                cursor.execute("UPDATE score SET score = (?) WHERE USER_ID = (?)",(player.score,get_username_id[0][0])).fetchall()
                database.commit()
                select_input_score = cursor.execute("SELECT score FROM score WHERE USER_ID = (?)",(get_username_id[0][0],)).fetchall()
                database.commit()
                select_high_score = cursor.execute("SELECT highscore FROM score WHERE USER_ID = (?)",(get_username_id[0][0],)).fetchall()
                database.commit()

                high_score_number_text = font.render(str(select_high_score[0][0]),1,(255,255,255))
                screen.blit(high_score_number_text,(950,400))
                if select_input_score[0][0] > select_high_score[0][0]:
                                new_score = cursor.execute("UPDATE score SET highscore = (?) WHERE USER_ID = (?)",(player.score,get_username_id[0][0])).fetchall()
                                database.commit()
##        this is used to display the game's fps                          
##        def show_fps():
##                fps_counter = str(int((clock.get_fps())))
##                fps_text = font.render(fps_counter, 1,(255,255,255))
##                screen.blit(fps_text,(100,100))




# this is where all the objects for every class is created
#every enemy and platform have their own objects as they will be doing different things at differnt times at different coordinates
        resume = buttons((25,0,50),500,200,400,75,"RESUME")
        exit_button = buttons((25,0,50),500,350,400,75,"EXIT")
        game_over = buttons((25,0,50),500,550,500,75,"CONTINUE")
        camera = camera(2.5)                  
        player = player(250,320,200)

        enemy1 = enemy(1400,600,210)
        enemy2 = enemy(1400,600,200)
        enemy3 = enemy(6600,600,200)
        enemy4 = enemy(5700,370,200)
        enemy5 = enemy(6670,155,200)
        enemy6 = enemy(7800,600,200)

        floor = level(200,650,925,120)
        ceiling = level(0,0,1500,80)
        sender_public_key = level(3300,250,90,50)
        sender_private_key = level(3500,250,90,50)
        recipient_public_key = level(4300,250,90,50)
        recipient_private_key = level(4500,250,90,50)
        message = level(3400,600,100,50)
        senders_key_text = level(3350,175,0,0)
        recipients_key_text = level(4350,175,0,0)
        recipient = level(4250,430,250,200)
        puzzles_text = level(3700,75,0,0)
        

        question = questions()
        question2 = questions()
        question3 = questions()

        FPS = 144
        clock = pygame.time.Clock()

        question.select_level_questions()
        question.get_question_id()
        question.select_options()

        question2.select_level_questions()
        question2.get_question_id()
        question2.select_options()

        question3.select_level_questions()
        question3.get_question_id()
        question3.select_options()

        stone_platform1 = level(200,650,1220,90)#long platform
        stone_platform2 = level(800,400,80,90)#small platform
        stone_platform3 = level(400,300,80,90)#small platform
        stone_platform4 = level(1800,650,80,90)#small platform
        stone_platform5 = level(2300,650,80,90)#small platform
        stone_platform6 = level(2800,650,80,90)#small platform
        stone_platform7 = level(3300,650,1220,90)#long platform
        stone_platform8 = level(3300,300,290,90)#medium platform
        stone_platform9 = level(3800,400,290,90)#medium platform
        stone_platform10 = level(4300,300,290,90)#medium platform
        stone_platform11 = level(4800,400,80,90)#small platform
        stone_platform12 = level(5200,500,80,90)#small platform
        stone_platform24 = level(5400,657,80,90)#small platform
        stone_platform13 = level(5500,85,80,440)#long vertical platform facing down
        stone_platform14 = level(5500,650,1220,90)#long platform
        stone_platform15 = level(5598,425,290,80)#medium platform
        stone_platform16 = level(5890,425,290,80)#medium platform 
        stone_platform17 = level(6182,425,290,80)#medium platform
        stone_platform18 = level(6670,200,80,440)#long vertical platform facing up
        stone_platform19 = level(5800,215,290,80)#medium platform
        stone_platform20 = level(6090,215,290,80)#medium platform
        stone_platform21 = level(6380,215,290,80)#medium platform
        stone_platform22 = level(6760,650,1220,90)#long platform
        stone_platform23 = level(7270,400,290,80)#medium platform



        #this while loop will be happening the whole time the game is running to keep track of the new coordinates of every object and the actions
        #being peformed constantly so they the methods will need to constantly be called thorught the playing time
        running = True
        while running:
            screen.blit(Background,(0,0))
            #show_fps()
            if paused == True:
                    pause_game()

            player.call_player_methods()

         #this will make sure the user has to answer 3 questions correctly to move on
            if question.number_of_correct_answers == 3:
                paused = False
                if enemy1.enemy_dead_animation_frame != 1:
                        enemy1.call_enemy_methods()
                        enemy1.player_hitbox()
                elif enemy1.enemy_dead_animation_frame > 0 and enemy2.enemy_dead_animation_frame != 1:
                        enemy2.call_enemy_methods()
                        enemy2.player_hitbox()
            if camera.world_shift < - 4500 and question2.number_of_correct_answers == 3:
                paused = False
                if enemy3.enemy_dead_animation_frame != 1:
                        enemy3.call_enemy_methods()
                        enemy3.player_hitbox()
                elif enemy4.enemy_dead_animation_frame != 1 and player.y < 440:
                        enemy4.call_enemy_methods()
                        enemy4.player_hitbox()
                elif enemy5.enemy_dead_animation_frame != 1 and player.y < 215:
                        enemy5.call_enemy_methods()
                        enemy5.player_hitbox()
            if camera.world_shift < -6000 and question3.number_of_correct_answers == 3:
                        paused = False
                        if enemy6.enemy_dead_animation_frame != 1:
                                enemy6.call_enemy_methods()
                                enemy6.player_hitbox()
                        if enemy6.enemy_dead_animation_frame > 0:
                                game_over_screen()
                                game_over.draw_button()
                                game_over.click_button()
                        


            floor.rectangle()
            floor.floor_collision()
            ceiling.ceiling_collision()

            #this will be used to spawn the puzzle once the player is nearby
            #it detects if the player is completing the steps properly
            #it is used to detect if the player is encrypting and decrypting the message correctly by using the keys and message's rectangles
            if camera.world_shift > -4600 and camera.world_shift < -1800:
                    senders_key_text.sender_key_text()
                    recipients_key_text.recipient_key_text()
                    puzzles_text.puzzle_text()

                    recipient.recipient_box()
                    recipient.recipient_text()

                    sender_public_key.pickup_key()
                    sender_private_key.pickup_key()

                    recipient_public_key.pickup_key()
                    recipient_private_key.pickup_key()

                    message.pickup_message()

                    sender_public_key.drop_key()
                    sender_private_key.drop_key()

                    recipient_public_key.drop_key()
                    recipient_private_key.drop_key()

                    message.drop_message()
                    
                    if sender_public_key.delete_key == False:
                        sender_public_key.key()
                        sender_public_key.public_key_text()
                    if sender_private_key.delete_key == False:
                        sender_private_key.key()
                        sender_private_key.private_key_text()


                    if recipient_public_key.delete_key == False:
                        recipient_public_key.key()
                        recipient_public_key.public_key_text()
                    if recipient_private_key.delete_key == False:
                        recipient_private_key.key()
                        recipient_private_key.private_key_text()

                    if message.delete_message == False:
                        message.decrypt_text()
                        message.message_text()
                        

                    if recipient_public_key.public_key_rect.colliderect(message.message_rect):
                        message.encrypt_message = True
                        recipient_public_key.x = recipient_private_key.x - 200
                        recipient_public_key.y = recipient_private_key.y

                    if message.encrypt_message == True:
                        if recipient.recipient_rect.colliderect(message.message_rect):
                            recipient.message_recieved = True

                    if recipient.message_recieved == True:
                        if recipient_private_key.public_key_rect.colliderect(message.message_rect):
                            message.decrypt_message = True
                            recipient_private_key.x = recipient_public_key.x + 200
                            recipient_private_key.y = recipient_public_key.y


                    
           #thes if statements are used to spawn the platforms only when the player is near them so that they do not slow down the game for no reason           
            if camera.world_shift > -1500:
                    stone_platform1.draw_long_platform()
                    stone_platform1.vertical_collision()
                    stone_platform1.horizontal_collision()

            if camera.world_shift > -900:
                    stone_platform2.draw_small_platform()
                    stone_platform2.vertical_collision()
                    stone_platform2.horizontal_collision()

            if camera.world_shift > -500:
                    stone_platform3.draw_small_platform()
                    stone_platform3.vertical_collision()
                    stone_platform3.horizontal_collision()

            if camera.world_shift > -2000 and camera.world_shift < -300:
                    stone_platform4.draw_small_platform()
                    stone_platform4.vertical_collision()
                    stone_platform4.horizontal_collision()

            if camera.world_shift > -2500 and camera.world_shift < -800:
                    stone_platform5.draw_small_platform()
                    stone_platform5.vertical_collision()
                    stone_platform5.horizontal_collision()

            if camera.world_shift > -3000 and camera.world_shift < -1300:
                    stone_platform6.draw_small_platform()
                    stone_platform6.vertical_collision()
                    stone_platform6.horizontal_collision()

            if camera.world_shift > -4600 and camera.world_shift < -1800:
                    stone_platform7.draw_long_platform()
                    stone_platform7.vertical_collision()
                    stone_platform7.horizontal_collision()

            if camera.world_shift > -3600 and camera.world_shift < -1800:
                    stone_platform8.draw_medium_platform()
                    stone_platform8.vertical_collision()
                    stone_platform8.horizontal_collision()

            if camera.world_shift > -4300 and camera.world_shift < -2200:
                    stone_platform9.draw_medium_platform()
                    stone_platform9.vertical_collision()
                    stone_platform9.horizontal_collision()

            if camera.world_shift > -4600 and camera.world_shift < -2800:
                    stone_platform10.draw_medium_platform()
                    stone_platform10.vertical_collision()
                    stone_platform10.horizontal_collision()
                    
            if camera.world_shift > -4900 and camera.world_shift < -3300:
                    stone_platform11.draw_small_platform()
                    stone_platform11.vertical_collision()
                    stone_platform11.horizontal_collision()

            if camera.world_shift > -5300 and camera.world_shift < -3700:
                    stone_platform12.draw_small_platform()
                    stone_platform12.vertical_collision()
                    stone_platform12.horizontal_collision()

            if camera.world_shift > -5600 and camera.world_shift < -3800:
                    stone_platform24.draw_small_platform()
                    stone_platform24.vertical_collision()
                    stone_platform24.horizontal_collision()

            if camera.world_shift > -5600 and camera.world_shift < -4000:
                    stone_platform13.draw_long_vertical_platform_down()
                    stone_platform13.vertical_collision()
                    stone_platform13.horizontal_collision()

            if camera.world_shift > -6800 and camera.world_shift < -4000:
                    stone_platform14.draw_long_platform()
                    stone_platform14.vertical_collision()
                    stone_platform14.horizontal_collision()

            if camera.world_shift > -5900 and camera.world_shift < -4090:
                    stone_platform15.draw_medium_platform()
                    stone_platform15.vertical_collision()
                    stone_platform15.horizontal_collision()

            if camera.world_shift > -6200 and camera.world_shift < -4380:
                    stone_platform16.draw_medium_platform()
                    stone_platform16.vertical_collision()
                    stone_platform16.horizontal_collision()

            if camera.world_shift > -6500 and camera.world_shift < -4670:
                    stone_platform17.draw_medium_platform()
                    stone_platform17.vertical_collision()
                    stone_platform17.horizontal_collision()

            if camera.world_shift > -6800 and camera.world_shift < -5140:
                    stone_platform18.draw_long_vertical_platform_up()
                    stone_platform18.vertical_collision()
                    stone_platform18.horizontal_collision()

            if camera.world_shift > -6100 and camera.world_shift < -4300:
                    stone_platform19.draw_medium_platform()
                    stone_platform19.vertical_collision()
                    stone_platform19.horizontal_collision()

            if camera.world_shift > -6400 and camera.world_shift < -4590:
                    stone_platform20.draw_medium_platform()
                    stone_platform20.vertical_collision()
                    stone_platform20.horizontal_collision()

            if camera.world_shift > -6700 and camera.world_shift < -4880:
                    stone_platform21.draw_medium_platform()
                    stone_platform21.vertical_collision()
                    stone_platform21.horizontal_collision()

            if camera.world_shift > -8100 and camera.world_shift < -5200:
                    stone_platform22.draw_long_platform()
                    stone_platform22.vertical_collision()
                    stone_platform22.horizontal_collision()

            if camera.world_shift > -7600 and camera.world_shift < -5600:
                    stone_platform23.draw_medium_platform()
                    stone_platform23.vertical_collision()
                    stone_platform23.horizontal_collision()

            #this will make sure questions are being asked until 3 have been answered correctly                  
            if question.number_of_correct_answers < 3:
                paused = True
                question.display_questions()
                question.display_option_a()
                question.display_option_b()
                question.display_option_c()
                question.click_option()
            #this will be used to ask questions when the player reaches the 3rd section of the level
            if camera.world_shift < - 4700 and question2.number_of_correct_answers < 3:
                paused = True
                question2.display_questions()
                question2.display_option_a()
                question2.display_option_b()
                question2.display_option_c()
                question2.click_option()
            #this will be used to asked questions when the plyaer reaches the 4th section of the level
            if camera.world_shift < -6300 and question3.number_of_correct_answers < 3:
                paused = True
                question3.display_questions()
                question3.display_option_a()
                question3.display_option_b()
                question3.display_option_c()
                question3.click_option()
                
            #this will check if the player has fallen off the map or if the player's hp falls below 0
            #if these conditions are met then the gameover screen is displayed
            if player.y > 750 or player.health <= 0:
                    game_over_screen()
                    game_over.draw_button()
                    game_over.click_button()

            if resume.paused == True:
                paused = True
                pause_game()
                resume.draw_button()
                resume.click_button()
                exit_button.draw_button()
                exit_button.click_button()
            camera.scroll_background()
                    
                    
            #this is uesed to keep track of all the keyborad inputs the user presses and calls the correct methods to peform the correct actions for the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                                player.moving_left = True
                                player.moving_right = False
                        if event.key == pygame.K_d:
                                player.moving_right = True
                                player.moving_left = False
                        if event.key == pygame.K_k:
                            if player.energy >= 75:
                                if player.attack_animation_frame == 0:
                                    player.special_attack()
                        if event.key == pygame.K_l:
                            if player.energy >= 150:
                                if player.ultimate_attack_animation_frame == 0:
                                    player.ultimate_attack()
                        if event.key == pygame.K_j:
                            if player.attack_animation_frame == 0:
                                player.normal_attack()
                        if event.key == pygame.K_SPACE:
                                player.player_jump()
                        if event.key == pygame.K_f:
                                player.pickup = True
                        if event.key == pygame.K_g:
                            if sender_public_key.delete_key == True:
                                sender_public_key.drop = True
                            if sender_private_key.delete_key == True:
                                sender_private_key.drop = True

                            if recipient_public_key.delete_key == True:
                                recipient_public_key.drop = True
                            if recipient_private_key.delete_key == True:
                                recipient_private_key.drop = True

                            if message.delete_message == True:
                                message.drop = True
                        
                                
                        if event.key == pygame.K_ESCAPE:
                            resume.paused = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        question.clicked = True
                        question2.clicked = True
                        question3.clicked = True
                        resume.clicked = True
                        exit_button.clicked = True
                        game_over.clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        resume.clicked = False
                        exit_button.clicked = False
                        game_over.clicked = False
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                                player.moving_left = False
                        if event.key == pygame.K_d:
                                player.moving_right = False
                        if event.key == pygame.K_f:
                                player.pickup = False
            pygame.display.update()
            clock.tick(FPS)
        pygame.quit()



    
