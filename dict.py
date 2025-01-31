# Agregar elementos a una lista
mi_lista = [1, 2, 3,4]

# Método 1: usando append()
mi_lista.append("ultima pocision")
""" print(mi_lista) """  # Resultado: [1, 2, 3, 4]

# Método 2: usando insert()
mi_lista.insert(1, "hola")  # Insertar el número 5 en la posición 1
""" print(mi_lista) """  # Resultado: [1, 5, 2, 3, 4]


# Modificar elementos en una lista:
# Para modificar elementos en una lista, simplemente accede al elemento mediante su índice y asigna un nuevo valor.
mi_lista[0] = 1000
""" print(mi_lista) """  # Resultado: [10, 5, 2, 3, 4]

'''
Eliminar elementos de una lista:
Hay varias formas de eliminar elementos de una lista en Python, como utilizar el método remove() para eliminar un valor específico, el método pop() para eliminar por índice o la palabra clave del.
'''

# Eliminar por valor usando remove()
""" mi_lista.remove(5) """
""" print(mi_lista) """  # Resultado: [10, 2, 3, 4]

# Eliminar por índice usando pop()
mi_lista.pop(1)
""" print(mi_lista) """  # Resultado: [10, 3, 4]

# Eliminar por índice usando del
del mi_lista[1]
""" print(mi_lista) """  # Resultado: [10, 4]




'''
Agregar y modificar elementos en un diccionario:
En Python, los diccionarios tienen pares de clave-valor. Puedes agregar nuevos pares clave-valor o modificar el valor asociado a una clave existente.
'''
# Crear un diccionario 
mi_diccionario = {"Fecha": "12/12/2024"}

# Agregar elementos al diccionario
mi_diccionario['nombre'] = 'Pepe'
mi_diccionario['edad'] = 30
print(mi_diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 30}

# Modificar el valor asociado a una clave existente
mi_diccionario['edad'] = 31
print(mi_diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 31}

""" 
Eliminar elementos de un diccionario:
Para eliminar un elemento de un diccionario, utiliza la palabra clave del y especifica la clave que deseas eliminar. 
"""
del mi_diccionario['edad']
print(mi_diccionario)  # Resultado: {'nombre': 'Juan'}

#Eliminar todos los elementos de un diccionario

mi_diccionario.clear()
print(mi_diccionario)


mision = True
recomendacion = True
se_casara = True

if (not mision or not se_casara) and recomendacion:
    print("se inviste")
else:
    print("no se inviste")