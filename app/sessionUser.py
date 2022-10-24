from db import *
def searchUserKey(var):
     db = criarBanco(1)
     usersAll = db.child("users").get()
     if var != "":
          for i in usersAll.each():
               user = i.val()
               if user['Email'] == var:
                    user_key_sess = i.key()
     else:
          user_key_sess = ""
     return user_key_sess
