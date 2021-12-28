# Desarrollar una API para que nos de la lista de todos los departamentos en el siguiente formato

# {

#   "ok":Boolean,

#   "content": List,

#   "message": String

# }

# en la cual, en el content debe de ir todos los departamentos
# ###############
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app=app)

departamentos = [
    'Ancash', 'Apurimac', 'Arequipa', 'Ayacucho', 'Cajamarca', 'Callao', 'Cusco', 'Huancavelica', 'Huanuco', 'Ica', 'Junín', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 'Madre de Dios', 'Moquegua', 'Pasco', 'Piura', 'Puno', 'San Martín', 'Tacna', 'Tumbes', 'Ucayali'
]


@app.route('/', methods=['POST', 'GET'])
def inicio():
    if request.method == 'POST':

        data = request.get_json()
        return data
    else:
        return 404


@app.route('/departamentos', methods=['GET', 'POST'])
def departamentos():
    if request.method == 'GET':
        return {
            "ok": True,

            "content": departamentos,

            "message": "estos son los depatamentos encontrados"
        }


if __name__ == '__main__':
    app.run(debug=True)
