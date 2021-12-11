# variables numericas
numero = 10
numero2 = 10.5

nombre = 'edu falcon'

# fecha = 0

# print('holaaa :)')

# soltero = True
# frio = False

# print(type(soltero))


# VARIABLES que tienen varios VALORES
# ARREGLOS > LISTAS LIST

edades = [10 , 12, 40, 60 , 'Eduardo', 14.5, False, [1, 2]]
# para ingresar a los valores de una lista debemos indicar la POSICION que siempre empieza en 0 (CERO) ademas si queremos usar valores negativos entonces la lista empezara por la ultima posicion (-1 : la ultima posicion)
# si nosotros en la posicion colocamos el siguiente formato: [n:m] entonces estaremos indicando que queremos ir desde la posicion 'n' hasta <'m' NOTA: Siempre el recorrido sera de izq a der aun asi usemos posiciones negativas
print(edades[1:-1])


# JSON (JavaScript Object Notation) | Diccionario
# Nota : Si una llave se repite su valor sera modificado y se perdera el 

# JSON (javascript object notation)| Diccionario
curso = {
    'nombre': 'backend',
    'nombre': 'frontend',
    'dificultad': 'Dificil',
    'skills': [
        {
            'nombre': 'base de datos',
            'nivel': 'Intermedio'

        },
        {
            'nombre': 'ORM',
            'nivel': 'Avanzado'
        }
    ]

}
# print(curso['skills'])

#quiero el nivel de la skill orm
# print(curso['skills'][1]['nombre'])


###########333


meses =[ 'enero', 'febrero','marzo' ,'abril']

# print(meses)

personas = [{
    'nombre': 'Eduardo',
    'nacionalidad': 'peruano',
    'hobbies':[
        {
            'nombre': 'Volar drones',
            'experiencia': '2 años'
        },{
            'nombre':'Programar',
            'experiencia': '1 mes'
        }
    ]
},{
    'nombre': 'Juliana',
    'nacionalidad': 'colombiana',
    'hobbies':[
        {
            'nombre': 'Montar bici',
            'experiencia': '4 años'
        },{
            'nombre':'Bases de datos',
            'experiencia': '8 mes'
        }
    ]
}]
# nacionalidad de la primera persona
print(personas[0]['nacionalidad'])
print(personas[1]['hobbies'])
print(personas[0]['hobbies'][1]['experiencia'])

# si se elimina

del(personas)