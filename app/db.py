import pyrebase
import re
def criarBanco(s):
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

    if s == 1:
        db = firebase.database()
        return db
    else:
        auth = firebase.auth()
        return auth