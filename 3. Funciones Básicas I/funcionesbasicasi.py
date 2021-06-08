#1 Imprime el numero que retorna la funcion.
def a():
    return 5
print(a())

#2 Imprime la suma de la funcion por si misma.
def a():
    return 5
print(a()+a())

#3 Imprimer los dos valores que retorna la funcion.
def a():
    return 5
    return 10
print(a())

#4 Imprime solo la funcion, el print que esta después del return queda fuera.
def a():
    return 5
    print(10)
print(a())

#5 Imprimer 5 y None debido a que x no toma ninún valor, solo hace el llamado a la función, no devuelve un valor la funcion
def a():
    print(5)
x = a()
print(x)

#6 
# Dentro de la función de imprime la suma de los valores ingresados. Se imprime b+c=3, luego se imprime b+c=5.
# Esta función imprime la suma de dos funciones, pero al no retornar nada la función arroja error al hacer el print de la suma de ambas funciones.
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#7 Uno le ingresa dos valores a la funcion y devuelve dos string, uno al lado del otro.
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8 Se ejecuta la función, se le asigna el valor a "b=100", luego se imprime ese valor. Luego como b es mayor que 10 retorna 10 por el else, el return 7 no se ejecuta nunca.
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9 
# Primero se imprime la funcion con los valores b=2 y c=3, al ser b<c retorna 7. 
# Luego se imprime la funcion con los valores b=5 y c=3, al ser b>c retorna 14. 
# Finalmente se imprime la suma de ambas funciones por lo que se imprime 21.
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10 
# Devuelve la suma de los valores ingresados en la función, el retorno de 10 no se ejecuta nunca.
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11
b = 500 #Se le asigna un valor a b=500
print(b) # Se imprime el valor de b =500
def a(): # Se define la función pero no se ejecuta.
    b = 300
    print(b)
print(b) # Se imprime b=500 
a() #Se ejecuta la función, b toma el valor de 300 dentro de la función y se imprime.
print(b) # Finalmente se imprime b=500, ya que al cambiar de valor dentr de la función no afecta el valor afuera.

#12
b = 500 #Se le asigna un valor a b=500
print(b) #Se imprime el valor de b =500
def a(): # Se define la función pero no se ejecuta.
    b = 300
    print(b)
    return b
print(b) #Se imprime el valor de b =500
a() #Se ejecuta la función, b toma el valor de 300 dentro de la función y se imprime. Se retorn b pero este valor no se usa mas adelante.
print(b) #Se imrime el valor de b que sigue siendo 500.

#13
b = 500 #Se le asigna un valor a b=500
print(b) #Se imprime el valor de b =500
def a(): # Se define la función pero no se ejecuta.
    b = 300
    print(b)
    return b
print(b) #Se imprime el valor de b =500
b=a() #Se le asigna a "b" el valor que retorna la función. Al ejecutarse la función se imprime el valor de b=300, valor que toma dentro de la función.
print(b) #Se imprime b=300

#14
# Se ejecuta la función a(), se imprime 1, luego se ejecuta la función b() que imprime 3, finalemnte se imprime 2.
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() 

#15
# Se le asigan a "y" lo que retorna la funcion a(), se imprime 1. 
# Luego a x se le asigna el valor de la función b(), la cual se ejecuta, y se imprime. 
# Se imprime 3, y al devolver 5 se imprime 5. 
# Finalmente la función a(), retorna 10 y se imprime.
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)