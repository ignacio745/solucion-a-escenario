class Crucero:
    def __init__(self, nombre: str, destino: str, precio: float):
        self.nombre = nombre
        self.destino = destino
        self.precio = precio
    
    def __str__(self) -> str:
        return f"Crucero {self.nombre} - {self.destino} - ${self.precio}"