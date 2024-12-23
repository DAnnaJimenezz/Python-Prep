## Iteradores e iterables

1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

lista = []
num=-15
while num < 0:
    lista.append(num)
    num +=1
print(lista)

2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

lista2 = [1,2,3,4,5,6,7,8,9,10]
x = 0
while x < len(lista2):
    if lista2[x] % 2 == 0:
        print(lista2[x])
    x += 1


3) Resolver el punto anterior sin utilizar un ciclo while

lista3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for a in lista3:  
    if a % 2 == 0:  
        print(a)

4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

for a in lista3[:3]:
    print(a)

5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

for elemento in enumerate(lista3):
    print(elemento)

6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

lista4 = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]

for i in range(1, 21):
    if i not in lista4: 
        lista4.append(i)
    print(i)

7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
n<sub>0</sub> = 0<br>
n<sub>1</sub> = 1<br>
n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
Crear una lista con los primeros treinta números de la sucesión.<br>

fibonacci = [0, 1]

for i in range(2, 30):
    next_number = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_number)
print(fibonacci)


8) Realizar la suma de todos elementos de la lista del punto anterior

sum(fibonacci)

9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
Donde i es la cantidad total de elementos<br>
n<sub>i-1</sub> / n<sub>i</sub><br>
n<sub>i-2</sub> / n<sub>i-1</sub><br>
n<sub>i-3</sub> / n<sub>i-2</sub><br>
n<sub>i-4</sub> / n<sub>i-3</sub><br>
n<sub>i-5</sub> / n<sub>i-4</sub><br>
 

primeros = 15  
n = primeros - 5  

while n < primeros:  
    print(fibonacci[n] / fibonacci[n - 1])  
    n += 1 

10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i, cadena in enumerate(cadena):
    if cadena == 'n':
        print(i)


11) Crear un diccionario e imprimir sus claves utilizando un iterador

diccionario= {"animal": "mono", 
              "clasificacion": "vertebrado",
              "alimentacion": "banano",
              "animal": "mariposa",
              "clasificacion": "invertebrado",
              "alimentacion": "nectar de las flores"}

for i in diccionario:
    print(i)

12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
print(type(cadena))

cadena = list(cadena)
print(type(cadena))

13) Crear dos listas y unirlas en una tupla utilizando la función zip

lista5 = ["1","2","3","4","5","6","7","8", "9","10"]
lista6 = ["Danna", "Milena", "Jimenez", "Castro"]
e = zip(lista5, lista6)
print(type(e))
print(list(e))

14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lis7 = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lista8 = [i for i in lis7 if i % 7 == 0]
print(lista8)

15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
total = 0

for elemento in lis:
    if type(elemento) == list:
        total += len(elemento)
    else:
        total += 1
print (total)

16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

for indice, elemento in enumerate(lis):
    if type(elemento) != list:
        lis[indice] = [elemento]
print(lis)