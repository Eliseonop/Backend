class Vehiculo:
    ruedas = 4
    color = 'Azul'


vehiculo1 = Vehiculo()
vehiculo1.ruedas = 67
# PODEMOS AGREGAR ATRIBUOS EXTRA A UNA CLASE, NOTA: ES UNA MALA PRACTICA
vehiculo1.procedencia = 'Japanese'


vehiculo2 = Vehiculo()

print(vehiculo1.ruedas)
print(vehiculo2.ruedas)


class VehiculoConstructor():

    # en todo metodo de la clase SIEMPRE tendremos que colocar como prumer parametro la palabra  self
    # self: sirve para referencia a la instacia actual de la claase esto se podria comparar con el uso de this

    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color

    def __str__(self):
        return 'Esta es una instacia de la clase VehiculoConstructor'

# cuando la variable se define dentro de la clase, esta pasa a llamarse atriburo


# cuando una funcion se define dentro de la clase, esta pasa a llamarse metodo
vehiculo3 = VehiculoConstructor(4, 'morado')
print(vehiculo3)
