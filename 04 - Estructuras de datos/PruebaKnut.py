
## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
import re


ciudades= ['Caracas','Buenos Aires', 'Lujan de Cuyo', 'Lima']
# print(ciudades)
# 2) Imprimir por pantalla el segundo elemento de la lista
# print(ciudades[1]);
# 3) Imprimir por pantalla del segundo al cuarto elemento
# print(ciudades[1:4])
# 4) Visualizar el tipo de dato de la lista
# print(type(ciudades[1:4]))
# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
# print(ciudades[2:])
# 6) Visualizar los primeros 4 elementos de la lista
# print(ciudades[:4])
# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
# ciudades.extend(['Caracas', 'Bogota'])
# print(ciudades)
# 8) Agregar otra ciudad, pero en la cuarta posición
# print(ciudades)
# ciudades.insert(3,'NuevoElemento')
# print(ciudades)
# 9) Concatenar otra lista a la ya creada
# nombres = ['Luis', 'Pedro', 'Jose']
# print(ciudades)
# ciudades.extend(nombres)
# print(ciudades)
# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
# ciudades.append('Caracas')
# print(ciudades)
# ciudades.index('Caracas')
# print(ciudades)
# print(ciudades.index('Caracas'))
# 11) ¿Qué pasa si se busca un elemento que no existe?
# print(ciudades)
# print(ciudades.index('Caracasr'))
# 12) Eliminar un elemento de la lista
# print(ciudades)
# ciudades.pop()
# print(ciudades)
# 13) ¿Qué pasa si el elemento a eliminar no existe?
# print(ciudades)
# ciudades.remove('Caracasd')
# print(ciudades)
# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
# print(ciudades)
# elemento=ciudades.pop()
# print(elemento)
# print(ciudades)
# 15) Mostrar la lista multiplicada por 4
# print(ciudades * 4)
# 16) Crear una tupla que contenga los números enteros del 1 al 20
enteroCeroVeint = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# 17) Imprimir desde el índice 10 al 15 de la tupla
# print(enteroCeroVeint[9:15])
# 18) Evaluar si los números 20 y 30 están dentro de la tupla
# print(enteroCeroVeint)
# print(enteroCeroVeint.index(20))
# print(enteroCeroVeint.index(30))
# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
# print(ciudades)
# 'Caracas' in ciudades
# print('Caracas' in ciudades)

# val=ciudades.index('Paris')
# print('Linea')
# print(val)
# def existParis(lista, dato):
#     existe = False
#     for i in lista:
#         if(i == dato):
#             existe = True
#     if(existe):
#         return print(dato, 'existe')
#     else:
#         lista.append(dato)
#     print(dato, 'no existe')
# existParis(ciudades, 'Cdaracas')
# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
# cont = 0
# for i in ciudades:
#     if(i == 'Caracas'):
#         cont += 1
# print(cont)
# cont = 0
# for i in enteroCeroVeint:
#     if(i == 15):
#         cont += 1
# print(cont)
# 21) Convertir la tupla en una lista
# nuevaLista = [enteroCeroVeint]
# print(nuevaLista)
# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
# print(enteroCeroVeint)
# elemetA, elemetB, elemetC = enteroCeroVeint
# print(elemetA, elemetB, elemetC)
# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad".
# Agregar tambien otras claves, como puede ser "Pais" y "Continente".
# diccionarioA = {
#     'ciudad':ciudades[2],
#     'pais':'Japon',
#     'Continente':'Oceania'
# }

# 24) Imprimir las claves del diccionario
# print(diccionarioA['ciudad'], diccionarioA['pais'],diccionarioA['Continente'])
# 25) Imprimir las ciudades a través de su clave
# print(
#     'Longitud lista:',len(ciudades),
#     'Valor del indice 0:',ciudades[0],
#     'Valor del indice 1:',ciudades[1],
#     'Valor del indice 2:',ciudades[2],
#     'Valor del indice 3:',ciudades[3]
# )