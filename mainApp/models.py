from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UsuarioManager(BaseUserManager):
    """Manager personalizado para el modelo Usuario."""
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico es obligatorio.')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)  # Cifra la contraseña automáticamente
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(correo, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    idUsuario = models.AutoField(primary_key=True)  # Mantengo este campo como lo tienes
    nombre = models.CharField(max_length=150)      # Sin cambios
    correo = models.EmailField(max_length=255, unique=True)  # Campo único para login
    password = models.CharField(max_length=128)    # Sin cambios

    is_active = models.BooleanField(default=True)  # Necesario para login
    is_staff = models.BooleanField(default=False)  # Requerido para superusuarios

    objects = UsuarioManager()  # Vincula el manager personalizado

    USERNAME_FIELD = 'correo'  # Campo usado para login
    REQUIRED_FIELDS = ['nombre']  # Campo adicional obligatorio al crear superusuarios

    def save(self, *args, **kwargs):
        # Cifra la contraseña automáticamente si no lo está
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.correo})"


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
