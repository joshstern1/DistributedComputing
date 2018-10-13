import mysql.connector

class MyDB():
    
    
    def __init__(self):
        self.my_db = mysql.connector.connect(
                host = "IP",
                port="PORT",
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
        
    
    def login_user(self, username, password):
        pass
    
                
    