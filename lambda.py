add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a * b
print(multiply(80,5))

#cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("cuadrados: ", squared_numbers)

#pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("pares", even_numbers)