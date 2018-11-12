from MyDB import MyDB

myDB = MyDB()
try:
    print(myDB.add_new_user("username123", "password"))
    userID = myDB.login_user("username123", "password")
    print(userID)
    print(myDB.login_user("username123", "password2"))
    
    print(myDB.get_credits(userID))
    myDB.update_credits(userID, 10)
    print(myDB.get_credits(userID))
    
    #myDB.delete_user(userID)
    print(myDB.login_user("username", "password"))
except Exception as e:
    print(e)


myDB.close_connection()