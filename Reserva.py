class Reserva:
    __numero_reserva_nueva = 1
    def __init__(self, email: str, nombre_crucero: str) -> None:
        self.numero_reserva = self.__numero_reserva_nueva
        self.__numero_reserva_nueva += 1
        self.email = email
        self.nombre_crucero = nombre_crucero
    
    def __str__(self):
        return f"Reserva {self.numero_reserva}: {self.email} - {self.nombre_crucero}"