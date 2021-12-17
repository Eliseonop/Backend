import random
# Para esta primera semana tendrás que crear 3 clases: Persona, Profesor y Alumno. Una Persona puede ser Profesor o Alumno por lo que tendrás que usar la Herencia para heredar unos atributos como por ejemplo su nombre, sexo, fecha de nacimiento entre otros y métodos como saludar entre otros.


#CREO LA CLASE PADRE 'PERSONA'
class Persona:
    def __init__(self, nombre, sexo, ocupacion, edad):
        self.nombre = nombre
        self.sexo = sexo
        self.ocupacion = ocupacion
        self.edad = edad

    def datos(self):
        print('Tus datos son :', self.nombre,
              self.sexo, self.ocupacion, self.edad)
    def saludar(self):
        print(random.choice(['Hola', 'Que tal', 'Buenos dias a todos']))
    def __decir_ocupacion_privada(self):
        print('Mi ocupacion es', self.ocupacion)
    def decir_ocupacion_publica(self):
        if(self.ocupacion != 'profesor'):
           self.__decir_ocupacion_privada()
        else:
            print('no puedo decir mi ocupacion ')


#AQUI CREO LA CLASE PROFESOR QUE HEREDO DE PERSONA
class Profesor(Persona):
    def __init__(self, nombre, sexo, ocupacion, edad,materia):
        super().__init__(nombre, sexo, ocupacion, edad)
        self.materia = materia
    def decir_materia(self):
        print('soy de la materia',self.materia)

#AQUI CREO LA CLASAE ALUMNO QUE HEREDO DE PERSONA
class Alumno(Persona):
    def __init__(self, nombre, sexo, ocupacion, edad,ciclo):
        super().__init__(nombre, sexo, ocupacion, edad)
        self.ciclo = ciclo
    def decir_ciclo(self):
        print('Mi ciclo es', self.ciclo)

#INSTANCIO PROFESOR
nuevo_profesor = Profesor('Juan','M','profesor',40,'Matematica')
nuevo_profesor.decir_materia()
nuevo_profesor.saludar()
nuevo_profesor.decir_ocupacion_publica()

#INSTANCIO ALUMNO
nuevo_Alumno = Alumno('Pedrito','F','Alumno',20,'cuarto')
nuevo_Alumno.decir_ciclo()
nuevo_Alumno.saludar()
nuevo_Alumno.decir_ocupacion_publica()