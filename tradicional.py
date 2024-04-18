def validarUsuario(userName,userPasword):
    userDB="user1234"
    paswordBD="admin123"
    if userPasword==paswordBD and userName==userDB:
        return True
    else:
        return False

nombre="Jose"
print(validarUsuario("Juan","admin123"))