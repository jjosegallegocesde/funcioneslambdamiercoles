#DECLARAR UNA FUNSION
def validarusuario(userName,userPassword):
    userDB="user1234"
    passwordDB="admin123"
    if userPassword==passwordDB and userName==userDB:
        return True
    else:
        return False
    
    #LLAMANDO LA FUNCION
    nombre="diana"
    resultado=validarusuario("diana","admin123")
    print(resultado)
    
    


