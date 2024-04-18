def validarUsuario(userName,userPassword):
    userDB = "user123"
    passwordDB = "admin123"

    if userPassword == passwordDB and userName == userDB:
        return True
    else:
        return False

nombre = "Mateo"
print(validarUsuario("user123","admin123"))