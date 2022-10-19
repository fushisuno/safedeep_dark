userRoot = {"Nome": "", "Email":"", "Id_User":"", "Descrição":"", "denuncias_curtidas": list(), "ferramentas_curtidas": list()}

def criandoUserRoot(sys, val):
    if sys == None:
        userRoot = {"Nome": "", "Email":"", "Id_User":"", "Descrição":"", "denuncias_curtidas": list(), "ferramentas_curtidas": list()}
    elif sys == "Nome":
        userRoot["Nome"] = val

    elif sys == "Email":
         userRoot["Email"] = val

    elif sys == "Id_User":
         userRoot["Id_User"] = val

    elif sys == "Descrição":
         userRoot["Descrição"] = val

    elif sys == "denuncias_curtidas":
         userRoot["denuncias_curtidas"] = val

    elif sys == "ferramentas_curtidas":
         userRoot["ferramentas_curtidas"] = val
    
    return userRoot
