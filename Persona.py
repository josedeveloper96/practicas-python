class Persona:
    def __init__(self, nombre, apellido, ine, telefono):
        self.nombre = nombre 
        self.apellido = apellido 
        self.ine = ine
        self.telefono = telefono

    def __str__(self):
        return self.nombre + " " + self.apellido + " - " + self.ine