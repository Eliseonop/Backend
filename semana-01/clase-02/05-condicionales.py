# codicional IF ELSE

edad = 12
edad_minima = 18
print(edad >= edad_minima)
if edad >= edad_minima:
    # si no tenemos una linea de codigo ponemos 'pass'
    pass
    print('Eres mayor de edad, puedes ingresar')
elif edad > 15:
    print('puedes ingresar solo a los quience años')
elif edad > 10 : 
    print('Puedes ingresar al zoo gratis')
else:
    print('eres menor de edad, no puedes ingresar')
print('yo siempre me ejecuto')

#OPERADOR TERNARIO
#Es pra devolver un valor y almacenarlo en una varuable y en una solo linea de codigo
# print('eres mayor de edad') if edad >= edad_minima else print('ERES MENOR DE EDAD')
# tengo el siguiente numero
numero = 11
# como saber si es par o impar

if numero % 2 == 0 :
    print('es par')
else:
    print('es impar')

# print('eres par') if numero % 2 == 0 else print('es impar')

persona = {
    'nombre':'Raul',
    'nacionalidad':'boliviana',
    'sexo':'M'

}
#vlaidad si la persona es raul y periana
if(persona['nombre'] == 'Raul' and persona['nacionalidad'] == 'Peruana'  ):
    print('Si la persona es', persona['nombre'],'y su nacionalidad es peruana')
else:
    print('No la persona es', persona['nombre'],'y su nacionalidad es',persona['nacionalidad'])
#              F               V
    # IF (COND AND COND2) OR COND3
                #  TODO ES V
# for
# sirve para iterar un numero limitado de veces y tiene un inicio o un numero de arranque y un fin
# generalmente el for se usa para iterar colecciones de datos ORDENADAS pero se puede usar como cualquier for
meses= ['Enero', 'Febrero', 'Marzo', 'Abril']

# para ir desde la posicion 1 hasta el final
for mes in meses[1:]:
    print(mes)

# itera todos los meses
for mes in meses:
    if mes == 'Enero':
        print('Vamos a la playa 🏖️')
    print(mes)

# for(let i=0; i< 10; i++){....}
# en el range podemos pasar hasta 3 parametros
# range(n) => el limite <n
# range(n,m) => n el inicio, m el limite (<m)
# range(n,m,o) => n el inicio, m el limite (<m), o cuantos se suma en cada ciclo
for numero in range(5,10, 2):
    print(numero)

# len() => saca la longitud de la variable
# para convertir de un tipo de dato a otro es necesario tener las siguientes consideraciones:
# * tiene que ser un tipo masomenos coherente (no tratar de convertir de una letra a un numero)
# str(121) | int(12.5) | bool(0) | float(5)

# para ir desde la mitad del arreglo al final
print(int(10.5))
for numero in range(int(len(meses)/2),len(meses)):
    print(numero)
    print(meses[numero])

# TAREAAAAAAA
personas = [
    {
    'nombre': 'Adriana',
    'edad': 25
    },
    {
    'nombre': 'Nicolas',
    'edad': 15
    },
    {
    'nombre': 'Maria',
    'edad': 23
    },
    {
    'nombre': 'Guillermo',
    'edad': 10
    }
]
# 1. Cuantas personas tienen mas de 20 años  > 2
# 2. Que personas son las que tienen menos de 20 años > Las personas son Nicolas, Guillermo
# HINT: crear una lista donde se almacenen los nombres de las personas que tienen menos de 20, un contador para contar a las personas de mas de 20

contador = 0
contador2 =0
arreglo1 =[]
arreglo2 = []
for i in personas:
    if i['edad'] > 20:
        contador += 1
        arreglo1.append(i['nombre'])
    else:
        contador2 += 1
        arreglo2.append(i['nombre'])
print(f'{contador} tienen mas de 20 años')
print(f'{contador2} tienen menos de 20 años')
print('personas que tinen mas de 20 años',arreglo1)
print('personas que tinen menos de 20 años',arreglo2)

import random
print(random.choice(['Armando', 'Juan', 'Pedro']))

import csv
def mostrainformacion():
    csvarchivo = open('data.csv', 'r', encoding='utf-8')
    entrada = csv.reader (csvarchivo) #Leer todos los registros
    for reg in entrada:
        print(reg)
    csvarchivo.close()
    del csvarchivo