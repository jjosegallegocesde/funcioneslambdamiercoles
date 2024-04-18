

def validarUsuario(userName, userPassword):
    userDB="user1234"
    passwordDB="admin123"
    if userPassword == passwordDB and userName == userDB:
        return True
    else:
        return False
    
print(validarUsuario("user1234","admin123"))