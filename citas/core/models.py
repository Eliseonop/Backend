from distutils.command.upload import upload
from enum import unique
from django.db import models

# Create your models here.


class PersonaModel(models.Model):
    opcionesEstadoCivil = [
        ('SOLTERO', 'SOLTERO'),
        ('CASADO', 'CASADO'),
        ('VIUDO ', 'VIUDO'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('COMPLICADO', 'COMPLICADO'),
        ('NO_ESPECIFICA', 'NO_ESPECIFICA')]

    personaId = models.AutoField(
        primary_key=True,  # sera la pimera columna de la tabla
        unique=True,  # INDICA QUE NO PUEDE TENER VALORES REPETIDOS
        null=False,  # INDICA QUE NO PUEDE TENER VALOR ALGUNO
        db_column='id')  # INDICA EL NOMBRE QUE LLEVARA EN LA TABLA DB
    personaNombre = models.CharField(
        max_length=50,  # almacenera como maximo 50 caracteres
        unique=True,
        null=False,
        # si no le indicamos entonces su nombre sera el mismo que el atributo(persona nombre)
        db_column='nombre'

    )
    personaApellido = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='apellido'
    )
    personaEmail = models.EmailField(
        max_length=50,
        db_column='email',
        null=False,
        unique=True
    )
    personaFechaNacimiento = models.DateField(
        db_column='fec_nac',
    )
    personaEstadoCivil = models.CharField(
        choices=opcionesEstadoCivil,
        db_column='estadoCivil',
        default='NO_ESPECIFICA'

    )
    # ImageField > sirve para almacenar imagenes pero solamnete guardara en la bd su ubicacion del archivo como tal lo guardara en el proyecto
    personaFoto = models.ImageField(
        db_column='foto',
        # es la carpeta donde se almacenara  estos archivos dentro del proyecto
        upload_to='personas/',
        null=True,
    )

    class Meta:
        # sirve para pasar metadata al padre,a la configracion del modelo (model)
        db_table = 'personas'
        # para modifica el ordenamiento de manera personalizada
        # ordering=['-email','apellido']
