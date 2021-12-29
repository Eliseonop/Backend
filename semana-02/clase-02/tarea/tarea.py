# hacer una api en la cual se almacenen todos los usuarios de una compañia, se debe guardar el nombre, apellido, area y fecha_inicio,
#  DNI vamos a tener un registro y un despido para eliminar el usuario (usar el metodo DELETE) ademas se puede actualizar el usuario
#  con uno de sus campos (si yo quiero solamente puedo actualizar o el nombre o el apellido, etc)
# ademas tener un endpoint para devolver el usuario PERO segun su DNI http://127.0.0.1:5000/usuario/12345678

# implementar un front para este backend


from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app=app)
Lista = []


@app.route('/', methods=['POST', 'GET'])
def inicio():

    if request.method == 'POST':

        data = request.get_json()
        if(data.get('nombre')):
            nombre = data.get('nombre')
            return 'Hola, {}!'.format(nombre)
        else:
            return 'Necesito la informacion', 400

    elif request.method == 'GET':
        # cuando retornamos una respuesta puede contener hasta dos parametros en el cual el primero sera la data enviada y el segundo sera el estado HTTP
        return 'Bienvenido a mi API de Productos', 200


@app.route('/usuarios', methods=['POST', 'GET'])
def usuarios():
    if request.method == 'GET':
        return {
            'data': Lista,
            'message': 'Los usuarios son:',
            'ok': True
        }

    elif request.method == 'POST':
        data = request.get_json()

        # insertando un registro en una bd (INSERT INTO ...)
        Lista.append(data)
        return {
            'data': data,
            'message': 'Producto agregado exitosamente',
            'ok': True
        }, 201


@app.route('/usuarios/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def usuario(id):
    if request.method == 'GET':
        if (id < len(Lista)):
            return {
                'ok': True,
                'data': Lista[id - 1],
                'message': 'El usuario es:'
            }
        else:
            return {
                'ok': False,
                'data': None,
                'message': 'El usuario no existe'
            }
    elif request.method == 'PUT':
        data = request.get_json()
        if(id < len(Lista)):
            Lista[id] = data
            return {
                'ok': True,
                'data': Lista[id],
                'message': 'Usuario actualizado exitosamente'
            }, 201
        else:
            return {
                'ok': False,
                'data': None,
                'message': 'El usuario con el id {} no existe'.format(id)
            }
    elif request.method == 'DELETE':
        # data = request.get_json()
        if(id < len(Lista)):
            Lista.pop(id)
            return {
                'ok': True,
                'data': Lista,
                'message': 'Usuario eliminado exitosamente'
            }, 201
        else:
            return {
                'ok': False,
                'data': None,
                'message': 'El usuario con el id {} no existe'.format(id)
            }


@app.route('/usuario/<int:id>', methods=['GET'])
def usuarioDni(id):
    if request.method == 'GET':

        for i in Lista:
            if(i["dni"] == str(id)):
                return i
        else:
            return {
                'ok': False,
                'data': None,
                'message': 'El usuario no existe'
            }


if __name__ == '__main__':
    app.run(debug=True, )
