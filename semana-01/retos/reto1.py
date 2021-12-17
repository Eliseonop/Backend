from datetime import datetime

tiempo= datetime.now()
hora = int(tiempo.strftime(" %H"))
print(hora)

nombre = input('Ingrese su nombre:')
edad = int(input('Ingrese su edad:'))

if edad < 18 :
    if  hora > 6:
        print('debes ir a dormir ya es mas de las 6pm')
    else :
        print('Si no has terminado tu tarea ¿Que esperas?')
else:
    print('No estas obligado hacer nada')