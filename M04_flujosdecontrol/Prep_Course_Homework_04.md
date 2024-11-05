## Flujos de Control

1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

a = 56
if (a < 0):
    print('Este número es menor a 0')
elif (a > 0):
    print('Este número es mayor que 0')
else:
    print('El número es igual a 0')


2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

x = 'Danna'
y = 35
if (type(x) == type(y)):
    print ('Las variables son tipos de datos iguales')
else:
    print('Las variables son tipos de datos diferentes')

3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar


for i in range (1, 20):
    if i % 2 ==0:
        print(f'El número es, {i} par')
    else:
        print(f'El número es, {i} impar')

4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3


for i in range (0, 5):
    print(f'Número', {i}, 'Elevado a la 3', {i**3})

5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

a = 56
for i in range (0, a):
    pass
print(a) 

6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

x = 45
if x > 0:
    factorial = 1
    contador = x
    while contador > 0:
        factorial *= contador
        contador -= 1
        print(f"El factorial de {x} es {factorial}")
else:
    print("La variable debe ser un número entero mayor a 0.")

7) Crear un ciclo for dentro de un ciclo while

contador = 0 
while contador < 3:
    print(f'Ciclo while: {contador + 1}')
    for i in range(1, 4):
        print(f'  Iteración del ciclo for: {i}')
    contador += 1

8) Crear un ciclo while dentro de un ciclo for

for i in range(1, 4):
    print(f'Ciclo for: {i}')
    contador = 1
    while contador <= 2:
        print(f'Ciclo while: {contador}')
        contador += 1

9) Imprimir los números primos existentes entre 0 y 30

tope_rango=30
n = 2
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(f'Este número es primo: {n}')
    else:
        primo = True
    n += 1

10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

tope_rango = 30
n = 2
while (n < tope_rango):
    primo = True
    for div in range(2, n):
        if n % div == 0:
            primo = False
            break
    if primo:
        print(f'Este número es primo: {n}')
    n += 1

11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

x = 100
while (x <= 300):
    if x % 12:
        x += 1
        continue
    print (x)
    x += 1 

13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

z = 100
while z <= 300:
    if z % 6 == 0:
        print (f'El número en el rango de 100 a 300 es divisible por 3 y multiplo de 6: {z}')
        break
    z += 1 