def validarUsuarios (userName,userPasword):
    userDB = "user1234"
    pasworDB = "admin123"
    if userPasword == pasworDB and userName == userDB:
        return True
    else:
        return False

# llamar una fun)
print(validarUsuarios("jan", "admin123"))
