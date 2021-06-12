# Nota: Evita usar palabras clave de clase como int, str, list y dict como nombres de variables / parámetros.

# Actualiza los valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].

def cambiaelvalor(x):
    for i in range (0, len(x)):
        for j in range (0,len(x[i])):
            # print(i,x[i][j])
            if x[i][j]==10:
                x[i][j]=15
    # x[1][0]=15, se puede hacer así pero preferí agregarle que cualquier 10 dentro de la lista se cambia por 15.
    return x
x = [[5,2,3],[10,8,9]] 
print(cambiaelvalor(x))

# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'

def cambiaelapellido(students):
    for student in students:
        if student['last_name']=="Jordan":
            student['last_name']="Bryant"
    return students
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(cambiaelapellido(students))

# En el directorio sports_directory, cambia 'Messi' a 'Andres'

def cambiamessi(sports_directory):
    for sport in sports_directory:
        for dato in range(0,len(sports_directory[sport])):
            if sports_directory[sport][dato]=="Messi":
                sports_directory[sport][dato]="Andres"
    return (sports_directory)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(cambiamessi(sports_directory))

# Camba el valor 20 en z a 30

def cambiavalor(z):
    # print(z)
    for value in z:
        for num in value:
            if value[num]==20:
                value[num]=30
    return z
z = [ {'x': 10, 'y': 20} ]
print(cambiavalor(z))

# Itera a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:

def iterateDictionary(students):
    for persona in students:
        print (f"first_name - {persona['first_name']}, last_name - {persona['last_name']} ")
        # print(persona.keys(),persona.values())
        # for dato in persona:
        #     print(dato, persona[dato])
        # # print(persona['first_name'], persona['last_name'] )
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)

# # La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# # Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# Obtén valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

def iterateDictionary2(info, students=[]):
    for persona in students:
            print(persona[info])
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary2 ('first_name', students)
iterateDictionary2('first_name', students)

# Michael
# John
# Mark
# KB
# Y iterateDictionary2('last_name', students) debería generar:

# Jordan
# Rosales
# Guillen
# Tonel
# Itera a través de un diccionario con valores de listas

# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
def printInfo(dojo):
    for datos in dojo:
        counter=0
        for info in dojo[datos]:
            counter=counter+1
        print(counter, datos.upper())
        for info in dojo[datos]:
            print(info)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon