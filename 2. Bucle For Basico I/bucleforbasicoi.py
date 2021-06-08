# Crea un archivo de Python llamado for_loop_basic1.py que realice las siguientes tareas.

# Básico : imprime todos los enteros del 0 al 150.
for x in range (0,151):
    print(x)

# Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range (1,201):
    print(x*5)

# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for x in range(1,100):
    
    if(x%5==0):
        print("Coding")
    else:
        print(x)       
    if(x%10==0):
        print("Coding Dojo")          

# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
aux=0
for x in range(0,500001):
    aux=aux+x
print(aux)

# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for x in range(2018, 0, -4):
    print(x)

# Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum= 2
highNum= 9
mult=3
for x in range (lowNum,highNum+1):
    if (x%mult==0):
        print (x)




# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?

