# Para este reto deberemos de crear una API en la cual ingresemos una tarea y su prioridad y que nos 
# muestre la lista de tareas con sus prioridades y la opción de poder actualizarla mediante su ID y 
# eliminarla también mediante su ID.

from datetime import date
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app=app)

tareas = [
    
]


@app.route('/', methods=['POST', 'GET'])
def inicio():
    if request.method == 'POST':

        data = request.get_json()
        return data
    else:
        return 404


@app.route('/tareas', methods= ['GET', 'POST'])
def tareas():
    if request.method == 'GET':
        return {
            'data': tareas,
            'message': 'las tareas son:',
            'ok': True
        }

    elif request.method == 'POST':
        data = request.get_json()
        tareas.append(data) # insertando un registro en una bd (INSERT INTO ...)
        return {
            'data': data,
            'message': 'Tarea agregada exitosamente',
            'ok': True
        }, 201

@app.route('/tarea/<int:id>', methods=['GET', 'PUT'])
def tarea(id):
    if request.method == 'GET':
    
        if (id < len(tareas)):
            return {
                'ok': True,
                'data': tareas[id],
                'message':'La tarea es:'
            }
        else:
            return {
                'ok': False,
                'data': None,
                'message': 'La tarea no existe'
            }
    elif request.method == 'PUT':
        data = request.get_json()
        if(id < len(tareas)):
          
            tareas[id] = data
            return {
                'ok': True,
                'data': tareas[id],
                'message': 'tarea actualizada exitosamente'
            }, 201
        else:
            return {
                'ok': False,
                'data': None,
                'message': 'La tarea no existe'
            }


if __name__ == '__main__':
    app.run(debug=True)
