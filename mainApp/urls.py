from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirige directamente a la vista de login
    path('login/', views.login_view, name='login'),  # Vista del login
    path('index/', views.index_view, name='index'),  # Vista del index, después de login
    path('sidebar/', views.dashboard, name="sidebar"),
    
    # Asegúrate de tener solo una ruta para 'index'
    path('index/', views.lista_libros, name="index"),  # Lista de libros en 'index'
    
    path('formagg/', views.agregar_libro, name='formagg'),  # Ruta para agregar un libro
    path('Tesis/', views.listar_tesis, name='listar_tesis'),  # Lista de tesis
    path('formTesis/', views.crear_editar_tesis, name='formTesis'),  # Ruta para crear una nueva tesis
    path('Tesis/editar/<int:pk>/', views.crear_editar_tesis, name='editar_tesis'),  # Editar una tesis
    path('Tesis/eliminar/<int:pk>/', views.eliminar_tesis, name='eliminar_tesis'),  # Eliminar una tesis
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),  # Listar préstamos
    path('prestamos/nuevo/', views.nuevo_prestamo, name='agregar_prestamo'),  # Nuevo préstamo
    path('prestamos/editar/<int:pk>/', views.editar_prestamo, name='editar_prestamo'),  # Editar préstamo
    path('prestamos/eliminar/<int:pk>/', views.eliminar_prestamo, name='eliminar_prestamo'),  # Eliminar préstamo

    # Rutas CRUD de libros
    path('libros/', views.lista_libros, name='lista_libros'),  # Lista de libros
    path('libros/agregar/', views.agregar_libro, name='agregar_libro'),  # Agregar libro
    path('libros/editar/<int:id>/', views.editar_libro, name='editar_libro'),  # Editar libro
    path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),  # Eliminar libro
    
    # LOGIN
    path('login/validar-correo/', views.validar_correo, name='validar_correo'),
    path('login/validar-password/', views.validar_password, name='validar_password'),
]
