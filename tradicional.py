def validar_usuario(user_name, user_password):
    user_DB="user1234"
    password_DB="admin123"
    if user_password==password_DB and user_name==user_DB:
        return True
    else:
        return False
    

print(validar_usuario("user1234","admin123"))
