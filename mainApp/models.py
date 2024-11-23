from django.db import models
from django.utils.timezone import now

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    folio = models.CharField(max_length=255, default='Sin Folio')
    editorial = models.CharField(max_length=255, blank=True, null=True)
    volumen = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    numero_control = models.CharField(max_length=50, default="No especificado")
    nombre = models.CharField(max_length=255, default="Nombre no especificado")
    grado = models.CharField(max_length=255, default="No especificado")
    grupo = models.CharField(max_length=50, default="No especificado")
    fecha_entrega = models.DateField(default=now)
    fecha_devolucion = models.DateField(default=now)
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('devuelto', 'Devuelto')])
    codigo_barras = models.CharField(max_length=255)
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE)  # Relación con el modelo Libro

    def __str__(self):
        return f"Prestamo {self.numero_control} - {self.libro.titulo}"
    
    from django.db import models

class Tesis(models.Model):
    numero_de_control = models.CharField(max_length=20, unique=True)
    nombre1 = models.CharField(max_length=100)
    grado_y_grupo = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    generacion = models.CharField(max_length=50)
    titulo_de_tesis = models.CharField(max_length=200)
    asesor_academico = models.CharField(max_length=100)
    asesor_empresarial = models.CharField(max_length=100, blank=True, null=True)
    codigo_de_barras = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.titulo_de_tesis} ({self.numero_de_control})"
