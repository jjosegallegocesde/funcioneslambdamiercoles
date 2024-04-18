def validarUsuario(userName,userPassword):
    userDB ="user1234"
    passworkDb = "admin123"
    if userPassword == passworkDb and userName == userDB:
        return True
    else:
        return False
    
#llamando la funcion
print(validarUsuario("user1234","admin123"))    
