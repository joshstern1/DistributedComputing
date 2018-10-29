from MyDB import MyDB

myDB = MyDB()

myDB.add_new_user("username", "password")
userID = myDB.login_user("username", "password")
print(userID)
print(myDB.login_user("username", "password2"))

print(myDB.get_credits(userID))
myDB.update_credits(userID, 10)
print(myDB.get_credits(userID))

myDB.delete_user(userID)
print(myDB.login_user("username", "password"))


myDB.close_connection()