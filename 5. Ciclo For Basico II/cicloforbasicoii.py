# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".

def tamañogrande(lista):
    for x in range (0,len(lista)):
        if (lista[x]>0):
            lista[x]="big"
    return lista
lista=[- 1, 3, 5, -5]
print(tamañogrande(lista))

# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

# Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. 
# (Tenga en cuenta que cero no se considera un número positivo).

def contarpositvos(lista):
    counter=0
    for x in range (0,len(lista)):
        if (lista[x]>0):
            counter=counter+1
    lista[len(lista)-1]=counter    
    return lista
lista=[1,6, -4, -2, -7, -2]
print(contarpositvos(lista))


# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.

def sumatotal(list):
    suma=0
    for value in range(0,len(list)):
        suma=suma+list[value]
    return suma
list=[1,2,3,4]
print(sumatotal(list))

# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7


# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.

def promedio(list):
    suma=0
    promedio=0
    for value in range(0,len(list)):
        suma=suma+list[value]
    promedio=suma/len(list)
    return promedio
list=[1,2,3,4]
print(promedio(list))

# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

# Longitud : crea una función que toma una lista y devuelve la longitud de la lista.

def longitud(list):
    return len(list)        
list=[37,2,1, -9]
print(longitud(list))

# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

# Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.

def minimo(list):
    if(len(list)==0):
        return False
    else:
        minimo=list[0]
        for value in range(0,len(list)): # minimo=min(list), esta funcion resume el for.
            if (list[value]<minimo):
                minimo=list[value]        
    return minimo
list=[37,2,1, -9]
print(minimo(list))

# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False

# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.

def maximo(list):
    if(len(list)==0):
        return False
    else:
        maximo=list[0]
        for value in range(0,len(list)): # minimo=min(list), esta funcion resume el for.
            if (list[value]>maximo):
                maximo=list[value]        
    return maximo
list=[37,2,1, -9]
print(maximo(list))

# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

# Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.

def analisisfinal(list):
    suma=0
    promedio=0
    maximo=0
    minimo=0
    for value in range(0,len(list)): 
        suma=suma+list[value]               # suma=sum(list)
        if (list[value]>maximo):
            maximo=list[value]          # maximo=max(list)
        else:
            minimo=list[value]      # minimo=min(list)
    promedio=suma/len(list)                 
    dic={"suma total":suma, "promedio":promedio, "mínimo":minimo, "máximo":maximo}
    return dic
list=[37,2,1, -9]
print(analisisfinal(list))

# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).

def listainversa(list):
    listaaux=[]
    for value in range (len(list)-1,-1,-1): # return list[::-1]
        listaaux.append(list[value])
    return listaaux
list=[37,2,1, -9]
print(listainversa(list))

# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]