from Persona import Persona


class Empleado(Persona):
    def __init__(self, nombre, apellido, ine, telefono, salario):
        super().__init__(nombre, apellido, ine, telefono)
        self.salario = salario