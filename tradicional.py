#DECLAR UNA FUNCION
def validarUsuario(userName,userPassword):
    userDB="user1234"
    passwordDB="admin123"
    if userPassword==passwordDB and userName==userDB:
        return True
    else:
        return False

#LLAMANDO LA FUNCION
nombre="Jose"
validarUsuario("Juan","admin123")
