from Empleado import Empleado
from Cliente import Cliente


def cargar():
    respuesta = input('¿va a ingresar un empleado?')
    nombre = input('Ingrese el nombre')
    apellido = input('Ingrese el apellido')
    ine = input('Ingrese el ine')
    telefono = input('Ingrese el telefono')

    if (respuesta == 'si'):
     salario  = input('ingrese el salario')
     emp = Empleado(nombre, apellido, ine, telefono, int(salario))
     personas.append(emp)
    else:
     tipo = input('ingrese el tipo de cliente')
    cli = Cliente(nombre, apellido, ine, telefono, tipo)
    personas.append(cli)

    personas = []
    cargar()
    cargar()

    for persona in personas:
      print(persona)