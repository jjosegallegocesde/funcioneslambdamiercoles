#declarar una funcion
def validarUsuario (userName,userPassword):
    userDB = "user1234"
    passwordDB = "admin123"
    if userPassword == passwordDB and userName == userDB:
        return True
    else:
        return False
    
#llamando la funcion
nombre = "Jose"
resultado = validarUsuario("Juan","admin123")
print (resultado)    