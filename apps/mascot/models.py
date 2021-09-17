from django.db import models

# Create your models here.
class mascota(models.Model):
    pk_mascota = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    raza = models.CharField(max_length=50, null=False, blank=False)
    años = models.TextField(null=False,blank=False)
    fecha_de_nacimiento= models.DateField(null=False,auto_now = False , auto_now_add = False)
