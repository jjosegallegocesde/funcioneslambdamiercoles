

def validarUsuario(userName, userPassword):
    userDB = 'admin'
    password = '1234'
    
    if userName == userDB and userPassword == password:
        return True
    else: 
        return False
    
usuario = input("ingrese un usuario: ")
contraseña = input("ingrese contraseña: ")

validar = validarUsuario(usuario,contraseña)
print(validar)