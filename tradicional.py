#Declarar una funcion
def validarUsuario(nombreUsuario,passwordUsuario):
    userDB="user1234"
    passwordDB="admin123"
    if passwordUsuario==passwordDB and nombreUsuario==userDB:
        return True
    else:
        return False
    
    #Llamando la funcion
print(validarUsuario("user1234","admin123"))
    