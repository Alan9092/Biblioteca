from django.contrib.auth.hashers import make_password
import os
import sys
import django

# Asegúrate de que la ruta raíz de tu proyecto esté en sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Configura Django para usarlo fuera del servidor
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Biblioteca.settings')
django.setup()

from mainApp.models import Usuario  # Ahora debería poder importar correctamente

# Lista de usuarios a agregar
usuarios = [
    {'nombre': 'gabi2', 'password': 'gabi2', 'correo': 'gabi2@gabi2.com'},  # Agrega más usuarios si lo deseas
    # {'nombre': 'juan', 'password': 'juan123', 'correo': 'juan@example.com'},
]

# Agregar usuarios evitando correos repetidos
for usuario in usuarios:
    if Usuario.objects.filter(correo=usuario['correo']).exists():
        print(f"El usuario con el correo {usuario['correo']} ya existe. No se registrará de nuevo.")
    else:
        contrasena_cifrada = make_password(usuario['password'])  # Cifra la contraseña
        nuevo_usuario = Usuario(
            nombre=usuario['nombre'],
            password=contrasena_cifrada,
            correo=usuario['correo']
        )
        nuevo_usuario.save()  # Guarda el nuevo usuario en la base de datos
        print(f"Usuario {nuevo_usuario.nombre} agregado con ID {nuevo_usuario.idUsuario}")
# CORRER ARCHIVO PARA CREACION DE USUARIOS 
# python mainApp/agregarUsuarios.py