#El siguiente código crea una lista usando la función estándar de Python list().
#a = list("letras")
#print(a)
# ['l', 'e', 't', 'r', 'a', 's']
#########################################

#Pero volviendo a las palabras reservadas,
#Python nos ofrece una forma de acceder a estas palabras programmatically
#import keyword
#print(keyword.kwlist)
##########################################################

#Condicionales: if, elif, else
#lenguaje = "Python"

#if lenguaje == "Python":
    #print("Estoy de acuerdo, Python es el mejor")
#elif lenguaje == "Java":
    #print("No me gusta, Java no mola")
#else:
    #print("Ningún otro lenguaje supera a Python")

# Salida: Estoy de acuerdo, Python es el mejor
##############################################################
x = 0
while True:
    print(x)
    if x == 2:
        break
    x += 1
