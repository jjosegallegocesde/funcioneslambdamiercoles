
#DECLARAR UNA FUNCION
def validarUsuario (usserName,usuarPassword):
    usserDB="use123"
    passwordDB="adm123"
    if  usuarPassword == passwordDB and usserName == usserDB:
        return True
    else: 
        return False
    
#LLAMADO LA FUNCION
resultado =validarUsuario("Juan","adm123")
print(resultado)