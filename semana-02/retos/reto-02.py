# Desarrollar una API para ingresar los datos (libre) y que por medio de otro endpoint los devuelva
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app=app)

datos = [

]


@app.route('/', methods=['POST', 'GET'])
def inicio():
    if request.method == 'POST':

        data = request.get_json()
        return data
    else:
        return 404

@app.route('/ingresar/datos', methods=['GET', 'POST'])
def ingresarDatos():
    if request.method == 'POST':
        data = request.get_json()
        datos.append(data)
        return {
            'data': data,
            'message': 'dato agregado exitosamente',
            
        }, 201
    else:
        return 404


@app.route('/datos', methods=['GET', 'POST'])
def datos():
    if request.method == 'GET':
        return {
            "ok": True,

            "content": datos,

            "message": "estos son los datos"
        }
    else:
        return 404


if __name__ == '__main__':
    app.run(debug=True)
