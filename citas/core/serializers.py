from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import PersonaModel


class PersonasSerializer(serializers.ModelSerializer):
    # si el serializador es correspondente a un modelo entonces tendremos que pasar informacion a su metadat ndicando a que modelo corresponder
    class Meta:
        # model > indica en que modelo se tiene que basar para traer toda su configuracion (que serian las columnas y sus tipos de datos) para que al momento de serializar (formatear) lo convierta al tipo de dato correcto
        model = PersonaModel
        # fields > indica qu colnas (atriutos) va a utilizar de ese modelo este serializador, si queremos que use todos entonces pondremos de valor '__all__', sin embargo si querremos que solamente use determinadas colmnas seria asi: ['personaNombre','personaCorreo']
        fields = '__all__'
    pass
