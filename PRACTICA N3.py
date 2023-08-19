'''''
#PROBLEMA N1
while True:
    try:
        fraccion = input("Ingrese una fracción en el formato X/Y: ")
        numerador, denominador = map(int, fraccion.split('/'))
        
        if numerador < 0 or denominador <= 0 or denominador < numerador:
            raise ValueError
        
        porcentaje = (numerador / denominador) * 100
        
        if porcentaje < 1:
            resultado = 'E'
        elif porcentaje > 99:
            resultado = 'F'
        else:
            resultado = str(round(porcentaje)) + '%'
        
        print("Cantidad de combustible en el tanque:", resultado)
        break
    
    except ValueError:
        print("Error: X e Y deben ser números enteros, Y debe ser mayor o igual a X, y Y debe ser diferente de 0.")
    
    except ZeroDivisionError:
        print("Error: El denominador no puede ser 0.")

#PROBLEMA N2
notas = input("Ingrese una lista de calificaciones separadas por comas: ")
lista_calificaciones = notas.split(",")
calificaciones_enteros = []
for calificacion in lista_calificaciones:
    try:
        calificacion_entero = int(calificacion)
        calificaciones_enteros.append(calificacion_entero)
    except ValueError:
        print(f"Calificación inválida: {notas}")

#PROBLEMA N3
import math
class circulo:
    def __init__(self,radio):
        self.radio = radio

    def calculararea(self):
        a =math.pi*self.radio**2
        print('El Area del Circulo es: ', round(a))

r=int(input('Ingrese el Radio  '))
cir=circulo(r)
cir.calculararea()

#PROBLEMA N4
class rectangulo:
    def __init__(self,anchox,largox):
        self.ancho = anchox
        self.largo =largox
    def calculaarea(self):
        a = self.ancho * self.largo
        print ('El Area del Rectangulo es: ',a)

an=int(input('Ingrese Ancho '))
la=int(input('Ingrese Largo '))
r1=rectangulo(an,la)
r1.calculaarea()

#PROBLEMA N5
class Alumno():
    def __init__(self,nombre,nota):
      self._nombre = nombre
      self._nota = nota

def nombre(self): 
    return self._nombre

def nota(self): 
    return self._nota

def aprobacionNota(self, nota): 
    if self._nota > 9:
        print(f'aprobo su nota es {self._nota}')
    else:
        print(f'no aprobo su nota es {self._nota}')

#PROBLEMA N7

import generador
lista_numeros = generador.generar_numeros()
print("Lista generada:")
generador.mostrar_lista(lista_numeros)
print("Lista ordenada:")
generador.ordenar_lista(lista_numeros)

#PROBLEMA N8
import operaciones
a = 10
b = 20

print(operaciones.suma(a,b))
print(operaciones.resta(a,b))
print(operaciones.producto(a,b))
print(operaciones.division(a,b))
'''