import mysql.connector
import re
import random


#TODO
#Add thread pool to handle multiple connections to the server


class MyDB():
    
    def __init__(self):
        try:
            self.my_db = mysql.connector.connect(
                    host = "IP",
                    port = "PORT",
                    user = "root",
                    password = "PASSWORD",
                    database = "distcompschema"
            )
            self.my_cursor = self.my_db.cursor()
        except Exception as e:
            print(e)


    #Diconnects from database
    def close_connection(self):
        try:
            self.my_db.disconnect()
        except:
            print("disconnection error")


    #Attempts to add new user
    #Returns userID if successful and False if username already used
    def add_new_user(self, username, password):
        if (not self.check_if_username_present(username)) \
                    and MyDB.check_email_format(username):
            userID = self.get_new_userID()
            self.my_cursor.execute("""
                INSERT INTO user (username, password, userID)
                VALUES (%s, %s, %s)
            """, (username, password, userID))
            self.my_db.commit()
            result = userID
        else:
            result = False
        return result
    
    
    def get_new_userID(self):
        userID = random.randint(0, 100000000)
        while(self.check_userID_present(userID)):
            userID = random.randint(0, 100000000)
        return userID
    
    
    def check_userID_present(self, userID):
        self.my_cursor.execute("""
            SELECT 1
            FROM user
            WHERE userID = %d
        """ %(userID))
        if self.my_cursor.fetchone() == None:
            result = False
        else:
            result = True
        return result
    
    
    def get_new_executableID(self):
        executableID = random.randint(0, 100000000)
        while(self.check_executableID_present(executableID)):
            executableID = random.randint(0, 100000000)
        return executableID
    
    
    def check_executableID_present(self, executableID):
        self.my_cursor.execute("""
            SELECT 1
            FROM executables
            WHERE executableID = %d
        """ %(executableID))
        if self.my_cursor.fetchone() == None:
            result = False
        else:
            result = True
        return result
    
    
    #Returns if given string in in the form of an email
    #Just checks for @ and . present with . after @
    @staticmethod
    def check_email_format(username):
        result = False
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            result = True
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
            UPDATE user
            SET credits = credits + %d
            WHERE userID = %d
        """ %(delta_credits, userID))
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
    
    
    #TODO deleta all attached file and results if not already being done
    #Deletes given user
    def delete_user(self, userID):
        self.my_cursor.execute("""
            DELETE FROM user
            WHERE userID = %d
        """ %(userID))
        
        #self.my_cursor.execute("""
        #    DELETE FROM executables
        #    WHERE userID = %d
        #""" %(userID))
        self.my_db.commit()
        
        
    #TODO test to ensure it works
    #Deletes given executableID row from the table
    def delete_executable(self, executableID):
        self.my_cursor.execute("""
            DELETE FROM executables
            WHERE executableID = %d
        """ %(executableID))
        self.my_db.commit()

    
    #Returns data in provided file
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, 'rb') as f:
                data = f.read()
            return data
        except:
            print("Read File Error")
    
    
    #Writes file from given data
    @staticmethod
    def write_file(data, filepath):
        try:
            with open(filepath, 'wb') as f:
                f.write(data)
        except Exception as e:
            print("write_file error")
    
        
    #Adds new executable to database returns executable ID
    def add_executable(self, userID, executable_name, executable):
        try:
            executableID = self.get_new_executableID()
            self.my_cursor.execute("""
                INSERT INTO executables (userID, executableName, executable, executableID)
                VALUES (%s, %s, %s, %s)
            """, (userID, executable_name, executable, executableID))
            self.my_db.commit()
            return executableID
        except:
            print("add_executable error")
    
    
    #Adds new executable from file path to database returns executable ID
    def add_executable_from_file(self, userID, executable_name, filepath):
        try:
            executableID = self.get_new_executableID()
            data = MyDB.read_file(filepath)
            self.my_cursor.execute("""
                INSERT INTO executables (userID, executableName, executable, executableID)
                VALUES (%s, %s, %s, %s)
            """, (userID, executable_name, data, executableID))
            self.my_db.commit()
            result = executableID
            return result    
        except:
            print("add_executable_from_file error")
            
            
    #Returns the binary executable file
    def get_executable(self, executableID):
        try:
            self.my_cursor.execute("""
                SELECT executable
                FROM executables
                WHERE executableID = %d
            """ %(executableID))
            return self.my_cursor.fetchone()[0].encode()
        except:
            print("get_executable error")
    
    
    #Saves executable to given filepath
    def save_executable_to_path(self, executableID, filepath):
        try:
            self.my_cursor.execute("""
                SELECT executable
                FROM executables
                WHERE executableID = %d
            """ %(executableID))
            data = self.my_cursor.fetchone()[0].encode()
            MyDB.write_file(data, filepath)             
        except:
            print("save_executable_to_path error")
    
    
    #Updates existing executable on database
    def set_executable_from_file(self, executableID, filepath):
        try:
            data = MyDB.read_file(filepath)
            sql = """
                UPDATE executables
                SET executable = %s
                WHERE executableID = %s
            """ 
            val = (data, executableID)
            self.my_cursor.execute(sql, val)
            self.my_db.commit()
        except:
            print("set_executable_from_file error")
    
    
    #Updates existing executable on database
    def set_executable(self, executableID, data):
        try:
            sql = """
                UPDATE executables
                SET executable = %s
                WHERE executableID = %s
            """ 
            val = (data, executableID)
            self.my_cursor.execute(sql, val)
            self.my_db.commit()
        except:
            print("set_executable error")
    
    
    #Updates name of executable
    def set_executable_name(self, executableID, executable_name):
        sql = """
            UPDATE executables
            SET executableName = %s
            WHERE executableID = %s
        """ 
        val = (executable_name, executableID)
        self.my_cursor.execute(sql, val)
        self.my_db.commit()
    
    
    #Returns a list of executables for given user
    #Returns if form (executable_name, executableID)
    def get_users_executables(self, userID):
        self.my_cursor.execute("""
            SELECT executableName, executableID
            FROM executables
            WHERE userID = %d
        """ %(userID))
        return self.my_cursor.fetchall()
      
    
    #Returns executable name
    def get_executable_name(self, executableID):
        self.my_cursor.execute("""
            SELECT executableName
            FROM executables
            WHERE executableID = %d
        """ %(executableID))
        return self.my_cursor.fetchone()[0]
    
    
    #Update result File
    def set_result_from_file(self, executableID, filepath):
        try:
            data = MyDB.read_file(filepath)
            sql = """
                UPDATE executables
                SET result = %s
                WHERE executableID = %s
            """ 
            val = (data, executableID)
            self.my_cursor.execute(sql, val)
            self.my_db.commit()
        except:
            print("set_result_from_file error")
    
    
    #Update result File
    def set_result(self, executableID, data):
        try:
            sql = """
                UPDATE executables
                SET result = %s
                WHERE executableID = %s
            """ 
            val = (data, executableID)
            self.my_cursor.execute(sql, val)
            self.my_db.commit()
        except:
            print("set_result error")
    
    
    #Returns result File or False if one does not exist
    def get_result(self, executableID):
        try:
            self.my_cursor.execute("""
                SELECT result
                FROM executables
                WHERE executableID = %d
            """ %(executableID))
            result = self.my_cursor.fetchone()[0]
            if result == None:
                result = False
            else:
                result = result.encode()
            return result 
        except:
            print("get_result error")
    
    
    #Saves result to given filepath
    #Returns whether or not result file was present
    def save_result_to_file(self, executableID, filepath):
        try:
            self.my_cursor.execute("""
                SELECT result
                FROM executables
                WHERE executableID = %d
            """ %(executableID))
            data = self.my_cursor.fetchone()[0].encode()
            if data == None:
                result = False
            else:
                result = True
                MyDB.write_file(data, filepath)
            return result
        except:
            print("save_result_to_file error")
    
    
    #Update Hardware rating for user
    def set_hardware_rating(self, userID, hardware_rating):
        self.my_cursor.execute("""
            UPDATE user
            SET hardwareRating = %d
            WHERE userID = %d
        """ %(hardware_rating, userID))
        self.my_db.commit()  
    
    
    #Returns hardware rating for user or False if one does not exist
    def get_hardware_rating(self, userID):
        self.my_cursor.execute("""
            SELECT hardwareRating
            FROM user
            WHERE userID = %d
        """ %(userID))
        result = self.my_cursor.fetchone()[0]
        if result == None:
            result = False
        return result
    
    