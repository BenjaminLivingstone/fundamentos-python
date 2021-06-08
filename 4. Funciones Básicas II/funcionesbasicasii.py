# Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
def cuentaregresiva(entrada):
    lista=[]
    # lista.len()=entrada
    for x in range (entrada, -1,-1):
        lista.append(x)
    print(lista)    
entrada=int(input())
cuentaregresiva(entrada)

# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]


# Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.

def imprimiryvolver(lista):
    print(lista[0])
    return lista[1]
lista=[1,2]
print (imprimiryvolver(lista))

# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

# First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.

def firstpluslength(lista):
    return (lista[0]+len(lista))
lista=[1,2,3,4,5]
print(firstpluslength(lista))

# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

# Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False

def mayoresqueelsegundo(lista):
    lista2=[]
    contador=0
    if (len(lista)<2):
        return False
    else:
        for x in range (0,len(lista)):
            if (lista[x]>lista[1]):
                contador=contador+1
                lista2.append(lista[x])
        print (contador)
        return lista2    
lista=[5,2,3,2,1,4]
print(mayoresqueelsegundo(lista))

# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False


# Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.

def longitudvalor(longitud, valor):
    lista=[]
    for x in range (0,longitud):
        lista.append(valor)
    return lista
valor1=6
valor2=2
print(longitudvalor(valor1,valor2))

# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]