from db import *
usRoot = {"Nome": "", "Email": "", "Id_User": "", "Descrição": "", "denuncias_curtidas": list(), "ferramentas_curtidas": list()}

def addDenun ():
     db = criarBanco(1)
     users = list()
     denun = list()
     liked_denun = list()

     usersFish = db.child("denuncias").get()

     den = db.child("users").child(usRoot["Id_User"]).child("denuncias_curtidas").get()
     qtd_den = den.val()
     if qtd_den != None:
          for fishy_den in den.each():
               nun = fishy_den.key()
               denun.append(nun)

     for i in usersFish.each():
          user = i.val()
          liked_fh = False
          if len(denun) > 0:
               if i.key() in denun:
                    liked_fh = True
          if user['opcao'] == "invasor": 
               dict_user = {"Nome": user['nome'], "Tipo": user['opcao'], "Nome_invasor": user['invasor'], "Descricao": user['descricao'], "ID_Fishy": "" + i.key()}
          else:
               dict_user = {"Nome": user['nome'], "Tipo": user['opcao'], "Url": user['url_site'], "Descricao": user['descricao'], "ID_Fishy": "" + i.key()}
          dict_user["Fishy_liked"] = liked_fh
          users.append(dict_user)

          if liked_fh == True:
               liked_denun.append(dict_user)
     return liked_denun

def addFer():
     db = criarBanco(1)
     tool_lik = list()
     tools = list()
     lista_tool = list()

     liked_fer = list()
     den = db.child("users").child(usRoot["Id_User"]).child("ferramentas_curtidas").get()
     qtd_den = den.val()
     if qtd_den != None:
          for fishy_den in den.each():
               nun = fishy_den.key()
               tool_lik.append(nun)

     liked_fh = False  

     usersAll = db.child("ferramentas").child("antimalware").get()
     for ferramenta in usersAll.each():
          tool = ferramenta.val()
          if len(tool_lik) > 0:
               if ferramenta.key() in tool_lik:
                         liked_fh = True
               else:
                    liked_fh = False 
          dict_tools = {"Nome": tool["Nome"], "Tipo": tool["Tipo"], "Title":  tool["Title"], "Descricao":  tool["Descricao"], "Media_img": "card_media_" + str(tool["Id_media"]), "ID_Tool": "" + ferramenta.key()}
          dict_tools["Tool_liked"] = liked_fh
          lista_tool.append(dict_tools)

          if liked_fh == True:
               liked_fer.append(dict_tools)

     lista_tool = list()
     liked_fh = False   
     usersAll = db.child("ferramentas").child("antivirus").get()
     for ferramenta in usersAll.each():
          tool = ferramenta.val()
          if len(tool_lik) > 0:
               if ferramenta.key() in tool_lik:
                         liked_fh = True
               else:
                    liked_fh = False 
          dict_tools = {"Nome": tool["Nome"], "Tipo": tool["Tipo"], "Title":  tool["Title"], "Descricao":  tool["Descricao"], "Media_img": "card_media_" + str(tool["Id_media"]), "ID_Tool": "" + ferramenta.key()}
          dict_tools["Tool_liked"] = liked_fh
          lista_tool.append(dict_tools)
          
          if liked_fh == True:
               liked_fer.append(dict_tools)

     return liked_fer


def userR(var): 
     db = criarBanco(1)
     usersAll = db.child("users").get()
     for i in usersAll.each():
          user = i.val()
          if user['Email'] == var:
               usRoot["Nome"] = user["Nome"]
               usRoot["Nome"] = user["Nome"]
               usRoot["Email"] = user["Email"]
               usRoot["Id_User"] = i.key()
               usRoot["Descrição"] = user["Descrição"]
               usRoot["denuncias_curtidas"] = addDenun()
               usRoot["ferramentas_curtidas"] = addFer()