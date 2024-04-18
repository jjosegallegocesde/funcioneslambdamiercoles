
#declarar una funcion
def validarUsuario(userName,userPassword):
    userDB="user1234"
    password="admin123"
    if userPassword==password and userPassword==userDB:
        return True
    else:
        return False
    
#llamando la funcion
print(validarUsuario("Juan","admin123"))     
