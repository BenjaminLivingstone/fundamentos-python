# GRUPO 2: 

# Crea una funcion que dado una palabra diga si es palindroma o no.
def palindroma(palabra):
    if ("hola"[::-1]==palabra):
        print("La palabra",palabra,"es palindroma")
    else:
        print("La palabra",palabra,"NO es palindroma")
palabra="hola";
palindroma(palabra)

palabra="python"
print(palabra[2:])
# palabra[inicio:final:paso]

print("hola"[::-1])
# - Crea una función que tome una lista y devuelva el primer y el último valor de la lista. Si la longitud de la lista es menor que 2, haga que devuelva False.

def devuelvevalor(lista):
    if (len(lista)<2):
        return False
    print(lista[0])
    print(lista[len(lista)-1])
lista=[1,2,3,4,5,7]
devuelvevalor(lista)

# # # - Crea una función que tome una lista y devuelva un diccionario con su mínimo, máximo, promedio y suma.

# def devuelvedic(listadic):
#     minimo=min(listadic)
#     maximo=max(listadic)
#     promedio=sum(listadic)/len(listadic)
#     suma=sum(listadic)
#     dic={"Mínimo":minimo,"Máximo":maximo,"Promedio":promedio,"Suma":suma}
#     print(dic)
# listadic=[1,21,3,44,-15,6]
# devuelvedic(listadic)