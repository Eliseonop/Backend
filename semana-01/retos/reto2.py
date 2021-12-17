
from datetime import datetime

tiempo = datetime.now()
fecha = int(tiempo.strftime(" %Y"))
print(fecha)


cantidad = int(input('Dime la cantidad de personas a ingresar'))
contador = 1
lista = []
for i in range(cantidad):
    print('Persona ', contador)
    nombre = input('NOMBRE:')
    dni = int(input('DNI:'))
    nacimiento = int(input('Año de Nacimiento de nacimiento:'))
    lista.append({
        'nombre': nombre,
        'dni': dni,
        'nacimiento': nacimiento

    })

    contador += 1
# lista.sort()
edades = []
for i in lista:
    edades.append(fecha - i['nacimiento'])
edades.sort()
# print(edades)
lista2 = []
for edad in edades:
    for persona in lista:
        if fecha - persona['nacimiento'] == edad:
            lista2.append({
                'nombre': persona['nombre'],
                'edad' : edad
            })

print('lista de la mas joven a la mas adulta',lista2)
