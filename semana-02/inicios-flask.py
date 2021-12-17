import re
from flask import Flask

#enn python tenemos, varias variables, que son deuso propio de python
#esta variable, sirve para indicar, si estamos, en el archivo pincipal del provedor
#__main__
app = Flask(__name__)
#las caractristicas de un decorador sirve para usar, los metodos de una clase   pero implementando, un verbo

@app.route('/')
def inicio():
    return 'bienvenido a mi api'

@app.route( '/bienvenido')
def bienvenido( ):
    return 'bienvenido a mi api'
    
@app.route( '/bienvenido/home')
def bienvenido_home( ):
    return 'biemvenido a mi api'
if __name__ == '__main__':
    #cada aez que hagamos un cambio en cualquier archiivo en, el proyecto, ser reinicie aatomaticamente,
    #  en tonces, tenemos que infdicar el valor de debug, como true, jpor ue tiene el alor de false,
    app.run(debug=True, port=3000)

