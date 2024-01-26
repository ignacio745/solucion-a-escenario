import regex as re

class Cliente:
    def __init__(self, email: str, nombre_apellido: str, contrasena: str):
        # Validar email
        # Expresion regular extraida de https://emaillistvalidation.com/blog/email-verification-with-regular-expressions-in-python-a-comprehensive-guide/
        if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email): 
            raise ValueError("El email no es valido")
        
        self.email = email
        self.nombre_apellido = nombre_apellido
        self.contrasena = contrasena

    def __str__(self):
        return f"Cliente: {self.email} - {self.nombre_apellido}"