class Producto:
    def __init__(self, nombre, precio, cantidad, ):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def informacion(self):
        print(
            f'Nombre del producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}')


cantidad = int(input('Dime la cantidad de productos a ingresar'))
lista = []
contador = 1
for i in range(cantidad):
    print('producto', contador)
    nombre = input('nombre del producto: ')
    cantidad = input('Cantidad del producto: ')
    precio = input('Precio del producto: ')
    lista.append(
         {
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }
    
    )
    contador += 1
valor = True
while (valor):
    informacion = input('desea informacion de un producto en mayusculas por favor y/n :')
    if informacion == "y" :
        producto = input('Nombre del poducto:')
        for i in lista:
            if i['nombre'] == producto:
                nuevo_producto = Producto(i['nombre'],i['precio'],i['cantidad'])
                nuevo_producto.informacion()
            else:
                print('no se agrego ese producto')
        valor = True
    else:
         valor = False
         



# print(lista)
