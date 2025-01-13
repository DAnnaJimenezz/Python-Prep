#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def num_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num_primo(3)


# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def lista_primos(lista):
    lista_numeros = []
    for num in lista:
        if num_primo (num):
            lista_numeros.append(num)
    return lista_numeros

lista2_primos =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista_numeros = lista_primos(lista2_primos)
lista_numeros

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:





# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:



# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:




# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def calcular_factorial(numero):
    if type(numero) != int or numero < 0:
        return "El número debe ser un entero no negativo."
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

print(calcular_factorial(5))