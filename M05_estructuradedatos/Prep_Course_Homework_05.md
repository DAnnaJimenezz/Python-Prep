## Estructuras de Datos

1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

lista = ['Colombia','Argentina','Francia','Mexico','Japón','Chile']
print (lista)

2) Imprimir por pantalla el segundo elemento de la lista

print(lista[1])

3) Imprimir por pantalla del segundo al cuarto elemento

print(lista[2:4])

4) Visualizar el tipo de dato de la lista

print(type(lista))

5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(lista[2:])

6) Visualizar los primeros 4 elementos de la lista

print(lista[:4]) # Para poder buscar elementos de la lista utilizamos los rangos empezando desde 0, se puede poner tanto solo el inicio, como solo el final

7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

lista.append('Brazil') # El metodo append permite agregar un nuevo elemento al final de la lista

lista.append('Colombia')

print(lista)

8) Agregar otra ciudad, pero en la cuarta posición

lista.insert(4, 'Perú') #El metodo insert permite insertar en la posición que deseamos 
print(lista)

9) Concatenar otra lista a la ya creada

lista.extend(['Perro', 'Gato']) #Extend sirve para concatenar con un nueva lista a la que ya teniamos creada
print(lista)

10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

lista.index('Colombia')

11) ¿Qué pasa si se busca un elemento que no existe?

lista.index('Estados Unidos')

12) Eliminar un elemento de la lista

lista.remove('Argentina')

print(lista)

13) ¿Qué pasa si el elemento a eliminar no existe?

lista.remove('India')

print(lista)

14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

a=lista.pop() # El metodo POP elimina o extrae el ultimo elemento de la lista

print(lista)

print(a)

15) Mostrar la lista multiplicada por 4

print(lista*4)

lista_dos = [45, 56, 100]
print(lista_dos*4)

16) Crear una tupla que contenga los números enteros del 1 al 20

tupla_uno = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

print(tupla_uno)

17) Imprimir desde el índice 10 al 15 de la tupla

print(tupla_uno[10:15])

18) Evaluar si los números 20 y 30 están dentro de la tupla

20 in tupla_uno # Evalua si estan o no en la tupla

30 in tupla_uno

19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

pais = 'Paris'
if (not(pais in lista)):
    lista.append(pais)
    print('Se insero correctamente a la lista')
else:
    print('No pudo ser insertado')

20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

print(tupla_uno.count(5)) # El metodo count sirve para saber cuantas veces esta un elemento en una lista o tupla
print(lista.count('Colombia'))

21) Convertir la tupla en una lista

lista_cuato = list(lista) #List nombre de una función interna que permite convertir en una lista, tambien se puede utilizar la funcion tupla
print(lista_cuato)

22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

x, y, z = tupla_uno[:3]
print(x)
print(y)
print(z)

23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

diccionario = {'Pais': lista, 
               'Ciudad': ['Bogota', 'Buenos Aires', 'Paris', 'Ciudad de Mexico', 'Tokio', 'Santiago'],
               'Continente': ['America', 'America', 'Europa', 'America', 'Asia', 'America']}

24) Imprimir las claves del diccionario

print(diccionario.keys()) # La funcion keys imprime las claves del diccionario

25) Imprimir las ciudades a través de su clave

print(diccionario['Ciudad'])