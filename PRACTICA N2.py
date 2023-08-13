'''
#PROBLEMA N1
def  num_div_mul(lim_inf, lim_sup):
    if lim_sup > lim_inf:
        resul = []
        for n in range(lim_inf, lim_sup + 1):
            if n % 7 == 0 and n % 5 == 0:
                resul.append(n)
        return resul
    raise ValueError('El limite inferior debe ser menor al limite superior.')
numeros = num_div_mul(1500, 2700)
print(numeros)            

#PROBLEMA N2
n = int(input("Ingrese Numeros de Lineas en Asteriscos:"))
for i in range(n + 1):
    print('*'*i)
for i in range(n-1,0,-1):
    print('*'*i)

#PROBLEMA N3
n = 1
par = impar = 0
while n != 0:
    n = int(input("¿Deseas Ingresar Numero? Si Escribe caso Contrario Coloca 0:  "))
    if n > 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("El Total de Numeros Pares es: ", par)
print("El Total de Numeros Impares es: ", impar)

#PROBLEMA N4
from pprint import pprint
cant_alum = int(input('  Ingrese la Cantidad de Alumno a Registrar  : '))
lis_alum = []
for i in range(cant_alum):
    print(f'----Registrando al Alumno  {i+1}-----')
    alum={}
    alum ["nombre"] = input('Ingrese Nombre del Alumno : ')
    notas = []
    for j in range(3):
        nota = int(input(f'Ingrese Nota {j+1}:  '))
        notas.append(nota)
    alum["nota"] = notas
    lis_alum.append(alum)
pprint("Imprimiendo Listado de Alumnos...")
pprint(lis_alum)

#PROBLEMA N5
 n = int(input("Ingrese el Numero: "))
d = int(input("Ingrese el Digito: "))
c = 0
while n > 0:
    if d == n % 10:
        c = c + 1
    n = n // 10
print(f"El Digito se Repite {c} veces ")

#PROBLEMA N6
def fibo(n):
    a = 0
    b = 1   
    for k in range(n):
        c=a+b
        a=b
        b=c
    return b
for x in range(0,50):
    print(fibo(x))

#PROBLEMA N7
numero=int(input('Ingrese un NUMERO  '))
if numero > 1:
    cont=0
    for i in range(2,numero):
        resto=numero%i
        if resto == 0:
            cont +=1
    if cont == 0:
      print ("El {} es un Numero Primo".format(numero)) 
    else:
        print ("El {} no es un Numero Primo".format(numero)) 
else:
    print ("El {} no es un Numero Primo".format(numero)) 

#PROBLEMA N8
num=int(input('Ingrese un NUMERO  '))
fact=1
for i in range(1,num +1):          
          fact*=i
print ("El Factorial del Numero" "es: ",fact)

#PROBLEMA N9
psinvocal=""
userWord=str(input("Ingrese una Palabra: "))
userWord=userWord.title()
for letra in userWord:
    if letra=='a':
        continue 
    elif letra=='e':
        continue
    elif letra=='i':
        continue
    elif letra=='o':
        continue
    elif letra=='u':
        continue
    psinvocal+=letra
print("La Palabra Sin Vocales Seria :  ")    
print(psinvocal)

#PROBLEMA N10
lista = ['enero','febrero']
dias = {1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09',10:'10', 11:'11', 12:'12', 13:'13', 14:'14', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20', 21:'21', 22:'22', 23:'23', 24:'24', 25:'25', 26:'26', 27:'27', 28:'28', 29:'29', 30:'30', 31:'31'}
meses = {1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09', 10:'10', 11:'11', 12:'12'}
fecha = input('Introduce una fecha en formato mm/dd/aaaa: ')
fecha = str=(fecha.split('/'))
print("La Fecha Introducida en el Nuevo Formato es:  ")
print(fecha[2],'-',meses[int(fecha[0])],'-',dias[int(fecha[1])])
 '''