import sqlite3

"""
    Class Name:     Customer
    Writen by:      D Cravens
    Date created:   11-19-2022
    Revised date:   12-18-2022
    Description :   User accounts for the Mighty Pizza app are maintained in this class using a relational database.

"""

class Customer:
    #the constructor for the class
    _instance = None
    _userName: str = ""
    _firstName: str = ""
    _lastName: str = ""
    _userGroup: str = ""

    # Connect to the database
    con = sqlite3.connect("Users.db")
    cur = con.cursor()
    
    def __new__(self):
        if self._instance is None:
            self._instance = super(Customer, self).__new__(self)
        try:
            # create a table for users in database
            self.cur.execute("CREATE TABLE users(firstname, lastname, username, password, email, number, type)")
        except:
            pass
        return self._instance

    def sanitize_usr_input(self, usrInput):
        # initializing bad_chars_list
        bad_chars = [';', ':', '!', "*","("]
        
        # using replace() to
        # remove bad_chars
        for i in bad_chars :
            return usrInput.replace(i, '')

    # Register\add new user to the database
    def add_customer(self, firstname: str, lastname: str, username: str, password: str, email: str, phoneNumber: str, usrGroup = "basic"):
        # Check to see if username already in the database
        x = self.cur.execute("SELECT count(*) FROM users WHERE username=%r"%(username))
        if list(x)[0][0]==0:
            # Username is not in database
            # Check to see if username and\or password is empty
            if username=="" or password=="":
                # Username and/or password is empty return message
                return("Register","Empty Entry is not Allowed(except Email)")
            else:
                # Username and password is not empty
                # Add user to the database
                self.cur.execute("insert into users values(%r,%r,%r,%r,%r,%r,%r)"%(firstname,lastname,username,password,email,phoneNumber,usrGroup))
                self.con.commit()
                # Return a message
                return("it worked")
        else:
            # Username is in database return a message
            return("User already exist, try a different username.")

    def login(self, username: str, password: str):
        # Prepare SQL statement
        statement = f"SELECT * from users WHERE username='{username}' AND password = '{password}';"
        # Execute SQL statement
        self.cur.execute(statement)
        if not self.cur.fetchone():  # An empty result evaluates to False.
            return False
        else:
            self.set_session(username)
            return True

    def set_session(self, username: str):
        # Prepare SQL statement
        statement = f"SELECT * from users WHERE username='{username}';"
        # Execute SQL statement
        self.cur.execute(statement)# Prepare SQL statement
        customer = self.cur.fetchall()

        for row in customer:
            #this.Session = SessionClass.Session(row[0], row[2], row[6])
            self._userName = row[0]
            self._firstName = row[2]
            self._userGroup = row[6]

    def delete_user(self, username: str):
        print(self.Session.get_usrGroup())
        if self.Session.get_usrGroup() == "Admin":
            # Prepare SQL statement
            statement = f"SELECT * from users WHERE username='{username}';"
            # Execute SQL statement
            self.cur.execute(statement)# Prepare SQL statement
            if not self.cur.fetchone():  # An empty result evaluates to False.
                print("No such username in database")
            else:
                # Prepare SQL statement
                statement = f"DELETE FROM users WHERE username='{username}';"
                # Execute SQL statement
                self.cur.execute(statement)
        else:
            print("No such username in admin")

    def get_username(this):
        return this._userName
    def get_user_firstname(this):
        return this._firstName
    def get_user_lastname(this):
        return this._lastName
    def get_user_group(this):
        return this._userGroup
    def guest(this):
        this._userName = "guest"
        this._firstName = "Guest"
        this._lastName = ""
        this._userGroup = "basic"
    def logout(this):
        this._userName = ""
        this._firstName = ""
        this._lastName = ""
        this._userGroup = ""



