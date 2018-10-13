import mysql.connector

class MyDB():
    
    
    def __init__(self):
        self.my_db = mysql.connector.connect(
                host = "IP",
                port = "PORT",
                user = "root",
                passwd = "PASSWORD",
                database = "distcompschema"
        )
        
        self.my_cursor = self.my_db.cursor()
        
        
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
    
    
    #Adds new user and returns userID
    def add_new_user(self, username, password):
        self.my_cursor.execute("""
            INSERT INTO user (username, password, credits)
            VALUES (%s, %s, %s)
        """, (username, password, 0))
        self.my_db.commit()
        self.my_cursor.execute("""
            SELECT userID
            FROM user 
            WHERE username = '%s'
        """ %(username))
        return self.my_cursor.fetchone()[0]
        
    
    #Returns true if given username is not present in DB
    def check_original_username(self, username):
        self.my_cursor.execute("""
            SELECT 1
            FROM user
            WHERE username = '%s'
        """ %(username))
        if self.my_cursor.fetchone() == None:
            result = True
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
    
    
                
    