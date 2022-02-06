# Listas, tuplas, etc. se pueden cambiar
a = [1, 2, 3]
b = {'Idioma': 98, "matemáticas": 101}

def myfun():
    a.append(4)
    b.update({"Inglés": 103})
    print("En la función a =", a)
    print("En la función b =", b)


myfun()
print("Fuera de la función a =", a)
print("Función externa b =", b)

#Resultado de salida:
#En la función a =  [1, 2, 3, 4]
#En la función b =  {'Idioma': 98, 'matemáticas': 101, 'Inglés': 103}
#Fuera de la función a =  [1, 2, 3, 4]
#Función exterior b =  {'Idioma': 98, 'matemáticas': 101, 'Inglés': 103}
