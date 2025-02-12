## Clases y Programación Orientada a Objetos

1) Crear la clase vehículo que contenga los atributos:<br>
Color<br>
Si es moto, auto, camioneta ó camión<br>
Cilindrada del motor

class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje

2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
Acelerar<br>
Frenar<br>
Doblar<br>

class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color 
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.direccion = 0
        
    def Acelerar (self, vel):
        self.velocidad += vel
    
    def Frenar (self, vel):
        self.velocidad -= vel
    
    def Doblar (self, grados):
        self.direccion += grados

3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

a = Vehiculo ('verde', 'moto', 5.7)
b = Vehiculo('azul', 'carro', 35)
c = Vehiculo('violeta', 'cuatrimoto', 7,12)

4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color 
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.direccion = 0

    def Acelerar (self, vel):
        self.velocidad += vel
    
    def Frenar (self, vel):
        self.velocidad -= vel
    
    def Doblar (self, grados):
        self.direccion += grados

    def Estado (self):
        print(f'El vehiculo tiene una velocidad de {self.velocidad} hacia {self.direccion}')

    def Caracteristicas (self):
        print(f'Color: {self.color}')
        print(f'Tipo: {self.tipo}')
        print(f'Cilindrada: {self.cilindraje}')

a = Vehiculo ('verde', 'moto', 5.7)
b = Vehiculo('azul', 'carro', 35)
c = Vehiculo('violeta', 'cuatrimoto', 7.1)

a.Acelerar(57)
a.Doblar(21)

a.Estado()
b.Caracteristicas ()

5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
Verificar Primo<br>
Valor modal<br>
Conversión grados<br>
Factorial<br>


6) Probar las funciones incorporadas en la clase del punto 5

7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
