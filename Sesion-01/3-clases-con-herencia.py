class Vehiculo:
    '''clase que sirve para el uso de los vehiculos'''

    def __init__(self, color, modelo, traccion):
        self.color = color
        self.modelo = modelo
        self.traccion = traccion
        self.__velocidad = 0

    def acelerar(self):
        '''metodo que aceleera el vehiculo de 20 en 20'''
        self.__velocidad += 20
        return 'La velocidad actual es : {} km/h'.format(self.__velocidad)

    def desacelerar(self):
        '''metodo que desaceleera el vehiculo de 20 en 20'''
        self.__velocidad -= 20
        self.__prueba()
        return self.__velocidad

    def get_velocidad(self):
        return self.__velocidad


class VehiculoVolador(Vehiculo):
    def __init__(self, color, modelo, traccion, vuela=False):
        super().__init__(color, modelo, traccion,)
        self.__vuela = vuela

    def volar(self):
        self.__vuela = True

    def aterrizar(self):
        self.__vuela = False

    def estado(self):
        estado_volando = 'estado volando' if self.__vuela else 'estado aterrizando'
        return 'La velocidad del vehiculo  es : {} \n El modelo es: {} \n La traccion es {} \n {} '.format(self.get_velocidad, self.modelo, self.traccion, estado_volando)


class VehiculoOffRoad(VehiculoVolador):
    def __init__(self, color, modelo, traccion, vuela=False, sumergidos=False):
        super().__init__(color, modelo, traccion, vuela)


obj_vehiculo = Vehiculo('verder', 'rx5', '4x4')
obj_vehiculo_volador = VehiculoVolador('blanco', 'xyz', '1x1')
obj_vehiculo_volador.volar()
print(obj_vehiculo_volador.estado())


# obj_vehiculo_offroad = VehiculoOffRoad('azul', '76542', '6x8')
# obj_vehiculo_offroad.acelerar()
# obj_vehiculo_offroad.desacelerar()
# obj_vehiculo_offroad.volar()

# Primero que el atributo vuela sea privado y luego tener un metodo llamado estado en el cual me indique cual es el estado del vehiculo, que me diga su color, modelo, traccion, velocidad y si esta volando o si esta aterrizado

print(obj_vehiculo_volador.estado())

# isinstance() > devolvera True si es que la instacia es de la clase
print(isinstance(obj_vehiculo_volador, Vehiculo))

# issubclass() devolvera True si es que la primera clase es herecia de la segunda clase
print(issubclass(obj_vehiculo_volador, Vehiculo))
