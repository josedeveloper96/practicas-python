from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, ine, telefono, categoria):
       super().__init__(nombre, apellido, ine, telefono)
       self.categoria = categoria
