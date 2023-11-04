from django.db import models
from django.core.exceptions import ValidationError

def longituddpi(value):
    if not (isinstance(value, int) and 10 ** 12 <= value < 10 ** 13):
        raise ValidationError('El valor debe de ser de 13 dígitos.')
def longitudnumero(value):
    if not (isinstance(value, int) and 10 ** 7 <= value < 10 ** 8):
        raise ValidationError('El valor debe ser de 8 dígitos.')


# Create your models here.

class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    dpi= models.IntegerField(validators=[longituddpi])
    fecha_de_nacimiento= models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    razon=models.CharField(max_length=200)
    receta=models.CharField(max_length=200)
    numero=models.IntegerField(validators=[longitudnumero])
    otros=models.CharField(max_length=300)
    visita=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    diagnóstico=models.CharField(max_length=300)
class Medico(models.Model):
    nombre= models.CharField(max_length=30)
    numero_de_colegiado= models.IntegerField()
    especialidad= models.CharField(max_length=200)
    otros=models.CharField(max_length=200)
class Mensajes(models.Model):
    nom_paciente=models.CharField(max_length=30)
    numero=models.IntegerField(validators=[longitudnumero])
    mensaje=models.CharField(max_length=500)



