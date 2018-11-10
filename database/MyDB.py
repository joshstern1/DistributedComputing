import mysql.connector

class MyDB():
    
    
    def __init__(self):
        self.my_db = mysql.connector.connect(
                host = "IP",
                port = "PORT",
                user = "root",
                passwd = "PASSWORD",
                database = "distcompschema",
        )
        
        self.my_cursor = self.my_db.cursor()
        
        
    #Diconnects from database
    def close_connection(self):
        self.my_db.disconnect()
        
    
    #TODO check for valid email format function to add to this and check original username
    #Attempts to add new user
    #Returns userID and False if username already used
    def add_new_user(self, username, password):
        if not self.check_if_username_present(username):
            self.my_cursor.execute("""
                INSERT INTO user (username, password)
                VALUES (%s, %s)
            """, (username, password))
            self.my_db.commit()
            self.my_cursor.execute("""
                SELECT userID
                FROM user 
                WHERE username = '%s'
            """ %(username))
            result = self.my_cursor.fetchone()[0]
        else:
            result = False
        return result
        
    
    #If login credentials are correct returns userID if not returns False
    def login_user(self, username, password):
        self.my_cursor.execute("""
            SELECT userID
            FROM user
            WHERE(username = '%s' AND password = '%s')
        """ %(username, password))
        value = self.my_cursor.fetchone()
        if value == None:
            result = False
        else:
            result = value[0]
        return result
    
    
    #Updates the users credits   
    def update_credits(self, userID, delta_credits):
        self.my_cursor.execute("""
            SELECT credits
            FROM user 
            WHERE userID = %d
        """ %(userID))
        cur_credits = self.my_cursor.fetchone()[0]
        new_credits = cur_credits + delta_credits
        self.my_cursor.execute("""
            UPDATE user
            SET credits = %d
            WHERE userID = %d
        """ %(new_credits, userID))
        self.my_db.commit()
        
        
    #Returns the number of credits a user has
    def get_credits(self, userID):
        self.my_cursor.execute("""
            SELECT credits
            FROM user
            WHERE userID = %d
        """ %(userID))
        return self.my_cursor.fetchone()[0]
    
    
    #Returns true if the password was successfully updated
    def change_password(self, userID, old_password, new_password):
        self.my_cursor.execute("""
            SELECT userID
            FROM user
            WHERE(userID = %d AND password = '%s')
        """ %(userID, old_password))
        value = self.my_cursor.fetchone()
        if value == None:
            result = False
        else:
            self.my_cursor.execute("""
                UPDATE user
                SET password = '%s'
                WHERE userID = %d
            """ %(new_password, userID))
            self.my_db.commit()
            result = True
        return result
    
    
    #Returns true if username is in the database
    def check_if_username_present(self, username):
        self.my_cursor.execute("""
            SELECT 1
            FROM user
            WHERE username = '%s'
        """ %(username))
        if self.my_cursor.fetchone() == None:
            result = False
        else:
            result = True
        return result
    
    
    #Returns true if the username was successfully updated
    def change_username(self, userID, password, new_username):
        self.my_cursor.execute("""
            SELECT userID
            FROM user
            WHERE(userID = %d AND password = '%s')
        """ %(userID, password))
        value = self.my_cursor.fetchone()
        if value == None:
            result = False
        else:
            self.my_cursor.execute("""
                UPDATE user
                SET username = '%s'
                WHERE userID = %d
            """ %(new_username, userID))
            self.my_db.commit()
            result = True
        return result
    
    
    #Deletes given user
    def delete_user(self, userID):
        self.my_cursor.execute("""
            DELETE FROM user
            WHERE userID = %d
        """ %(userID))
        self.my_db.commit()
        
        
    #TODO
    #Adds new executable to database
    def add_executable(self, userID, executable_name, executable):
        return True
    
    
    #TODO
    #Updates existing executable on database
    def set_executable(self, executableID, executable):
        return True
    
    
    #TODO
    #Updates name of executable
    def set_executable_name(self, executableID, executable_name):
        return True
    
    
    #TODO
    #Returns a list of executables for given user
    #Returns if form (executable_name, executableID)
    def get_users_executables(self, userID):
        return True
    
    
    #TODO
    #Returns the binary executable file
    def get_executable(self, executableID):
        return True
    
    
    #TODO
    #Returns executable name
    def get_executable_name(self, executableID):
        return True
    
    
    #TODO
    #Update result File
    def set_result(self, executableID, result):
        return True
    
    
    #TODO
    #Returns result File or False if one does not exist
    def get_result(self, executableID):
        return True
    
    
    #TODO
    #Update Hardware rating for user
    def set_hardware_rating(self, userID, hardware_rating):
        return True
    
    
    #TODO
    #Returns hardware rating for user or False if one does not exist
    def get_hardware_rating(self, userID):
        return True
    
    
    
    