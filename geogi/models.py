from django.db import models

class Ubicacion(models.Model):
    direccion = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direccion} ({self.latitud}, {self.longitud})"