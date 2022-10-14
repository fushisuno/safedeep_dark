from random import randint, random
from flask import *
from jinja2 import Environment

import pyrebase
import re
config = {
  "apiKey": "AIzaSyAfJZyTi1WtVKy62SytAGbQyd2TaPCWn6A",
  "authDomain": "safedeep-9c030.firebaseapp.com",
  "databaseURL": "https://safedeep-9c030-default-rtdb.firebaseio.com",
  "projectId": "safedeep-9c030",
  "storageBucket": "safedeep-9c030.appspot.com",
  "messagingSenderId": "325692084824",
  "appId": "1:325692084824:web:3ce03fcce1a9fd2286f02d"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
auth = firebase.auth()
anonymus = ""
pagin = "index"
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

app = Flask(__name__)
app.secret_key = "APK_SESION_IS"
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route("/")
@app.route("/index")
def home(): 
    pagin = "index"
    return render_template("index.html")

@app.route("/")
@app.route("/safety")
@app.route("/safety/")
def safety():
    pagin = "safety"
    return render_template("safety.html", pagin = pagin)



@app.route("/")
@app.route("/tools")
@app.route("/tools/")
def tools():
    pagin = "tools"
    tools = list()
    lista_tool = list()
    usersAll = db.child("ferramentas").child("antimalware").get()
    for ferramenta in usersAll.each():
        tool = ferramenta.val()
        dict_tools = {"Nome": tool["Nome"], "Tipo": tool["Tipo"], "Title":  tool["Title"], "Descricao":  tool["Descricao"], "Media_img": "card_media_" + str(tool["Id_media"])}
        lista_tool.append(dict_tools)
    dic_tip = {"Tipo_tool": " Anti-Malware", "Valor": lista_tool, "Class_id": "malware"}
    tools.append(dic_tip)

    lista_tool = list()
    usersAll = db.child("ferramentas").child("antivirus").get()
    for ferramenta in usersAll.each():
        tool = ferramenta.val()
        dict_tools = {"Nome": tool["Nome"], "Tipo": tool["Tipo"], "Title":  tool["Title"], "Descricao":  tool["Descricao"], "Media_img": "card_media_" + str(tool["Id_media"])}
        lista_tool.append(dict_tools)
    dic_tip = {"Tipo_tool": " Anti-virus", "Valor": lista_tool, "Class_id": "antivirus"}
    tools.append(dic_tip)

    return render_template("tools.html", tools = tools, pagin=pagin)




@app.route("/fishys")
def fishys():
    users = list()
    denun = list()
    usersFish = db.child("denuncias").get()
    usersAll = db.child("users").get()
    for i in usersAll.each():
        user = i.val()
        user_valid = user['Email']
        try:
            if user_valid == session["user_name"]:
                den = db.child("users").child(i.key()).child("denuncias_curtidas").get()
                qtd_den = den.val()
                if qtd_den != None:
                    for fishy_den in den.each():
                        nun = fishy_den.key()
                        denun.append(nun)
        except:
            denun = list()

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
    
    return render_template("fishys.html", users = users)

@app.route("/fishys/add/<id_den>")
def fishy_liked(id_den):
    id_fishys_liked = {}
    usersAll = db.child("users").get()
    for i in usersAll.each():
        user = i.val()
        user_valid = user['Email']
        if user_valid == session['user_name']:
            id_fishys_liked = {"Id": str(id_den)}
            db.child("users").child(i.key()).child("denuncias_curtidas").child(id_den).set("Liked")
            return redirect("/fishys")
    return redirect("/login")


@app.route("/fishys/del/<id_den>")
def fishy_deleted(id_den):
    usersAll = db.child("users").get()
    for i in usersAll.each():
        user = i.val()
        user_valid = user['Email']
        if user_valid == session['user_name']:
            db.child("users").child(i.key()).child("denuncias_curtidas").child(id_den).remove()
            return redirect("/fishys")
    return redirect("/login")





@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        camps = {"email": "", "pass":""}
        if request.method == 'POST':
            name = request.form["user_email"]
            password = request.form['password']
            try:
                auth.sign_in_with_email_and_password(name, password)
                session["user_name"] = request.form["user_email"]
                return redirect("/")
            except:
                session["user_name"] = None
                camps['email'] = "camp_invalid"
                session["name"] = None
                camps['pass'] = "camp_invalid"
            
                return render_template("login.html", camps=camps)

        return render_template("login.html", camps=camps)
    except:
        return "Error"



@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    try:
        confirmed = 0
        camps = {"name": "", "email": "", "pass":"", "pass_conf" : ""}
        if request.method == 'POST':
            user_name = "" + request.form["user_name"]
            user_email = "" + request.form["user_email"]
            user_password = "" + request.form["user_password"]
            user_confirmed_pass = "" + request.form["confirmed_password"]
            dados = { "Nome": request.form["user_name"], "Email": request.form["user_email"]}
            if len(user_name) < 4:
                camps['name'] = "camp_invalid"
            else:
                camps['name'] = "camp_sucess"
                confirmed += 1

            if user_password != user_confirmed_pass:
                camps['pass'] = "camp_invalid"
                camps['pass_conf'] = "camp_invalid"
            else:
                confirmed += 2
            
            if(re.search(regex, user_email)):  
                camps['email'] = "camp_sucess"
                confirmed += 1
            else:
                camps['email'] = "camp_invalid"

            
            if confirmed >= 4:
                if user_password == user_confirmed_pass:
                    try:
                        auth.create_user_with_email_and_password(user_email, user_password)
                        id_us = db.generate_key()
                        print("criou")
                        db.child("users").child(id_us).set(dados)
                        db.child("users").child(id_us).child("denuncias_curtidas").set("")

                    except:
                        return redirect('/login')
                    return redirect("/login")

        return render_template("cadastro.html", camps = camps)
    except:
        return "Error"


if __name__ == '__main__':
    app.run(debug=True)