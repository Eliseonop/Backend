class Electrodomestico:
    def __init__(self):
        self.__nombre = ''
        self.__precio = 0.0
        self.__color = ''
    # getter > sire para devolver el ocntenido de un atributo privado
    # setter > sirve para asignar el contenido de un atriburo privvado que no sea e el constructor
    # deletter > sirve para eliminar un atriburo privado

    def __getNombre(self):
        return self.__nombre

    def __setNombre(self, nombre):
        self.__nombre = nombre

    def __deleteNombre(self):
        del self.__nombre

    nombre_electrodomestico = property(
        __getNombre, __setNombre, __deleteNombre)


microondas = Electrodomestico()

microondas.nombre = 'Microondas'

print(microondas.nombre_electrodomestico)
del microondas.nombre_electrodomestico
