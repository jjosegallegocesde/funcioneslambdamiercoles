#DECLARAR UNA FUNCION
def validarUsuario(userName , userPassword ):
    userDB="1234"
    passwordDB="admin123"
    if userPassword==passwordDB and userName==userDB:
        return True
    else:
        return False
    
#LLAMANDO LA FUNCION

nombre="jorge"
resultado=validarUsuario("jorge","admin123")
validarUsuario()
    