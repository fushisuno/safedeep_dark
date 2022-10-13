from random import randint, random
from flask import *

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

if __name__ == '__main__':
    app.run(debug=True)