def validarusuario(userName,userPassword):
    userDB="user1234"
    passwordDB="admin123"
    if userPassword==passwordDB and userName==userDB:
        return True
    else:
        return False
    #llamando la funcion
    nombre="jose"
    resultado=print(validarusuario("juan","admin123"))
    print(resultado)