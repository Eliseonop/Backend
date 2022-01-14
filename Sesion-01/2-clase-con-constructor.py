class Vehiculo:
    '''clase que sirve para el uso de la instancia de un vehiculo'''

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

    def __prueba(self):
        '''metodo privado de la clase que solo uede ser accedido denro de la misma'''
        print('Esto no debeeria pasar')


vehiculo1 = Vehiculo('azul', 'x3', '4x2')
vehiculo1.velocidad = 100
print(vehiculo1.acelerar())
print(vehiculo1.acelerar())
print(vehiculo1.acelerar())
print(vehiculo1.desacelerar())
