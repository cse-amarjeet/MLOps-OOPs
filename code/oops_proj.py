class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook !! how would you like to proceed?
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit\n""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_message()
        else:
            pass
    
    def signup(self):
        email = input("Enter your email here: ")
        pwd = input("Enter the new password: ")
        self.username = email
        self.password = pwd
        print("you have signed up successfully!!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username=="" and self.password=='':
            print("please signup first by presing 1 in the menu")
        else:
            uname= input("enter your email/username: ")
            pwd1 = input("Enter your password: ")
            if self.username == uname and self.password == pwd1:
                print("you have signined successfully!!")
                self.loggedin = True
            else:
                print("please input the correcr credentials!!")
        print("\n")
        self.menu()
    def my_post(self):
        if self.loggedin == True:
            txt = input("Write you post here: ")
            print("Following content has been posted: ",txt)
        else:
            print("you need signin first before posting")
        self.menu()
        
    def send_message(self):
        if self.loggedin == True:
            txt = input("Enter you message here: ")
            frnd = input("whom to send the msg?  -> ")
            print("your message has been send to ",frnd)
        else:
            print("you need signin first before posting")
        self.menu()

obj = chatbook()