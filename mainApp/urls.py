from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta de la vista inicio
    path('sidebar/', views.dashboard, name="sidebar"),
    path('index/', views.lista_libros, name="index"),  # Cambiar para listar libros en 'index'
    path('formagg/', views.agregar_libro, name='formagg'),  # Ruta para agregar un libro
    path('Tesis/', views.Tesis, name='Tesis'),
    path('formTesis/', views.formTesis, name='formTesis'),
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),  # Listar préstamos
    path('prestamos/nuevo/', views.nuevo_prestamo, name='agregar_prestamo'),  # Nuevo préstamo
    path('prestamos/editar/<int:pk>/', views.editar_prestamo, name='editar_prestamo'),  # Editar préstamo
    path('prestamos/eliminar/<int:pk>/', views.eliminar_prestamo, name='eliminar_prestamo'),  # Eliminar préstamo

    
    # Rutas CRUD de libros
    path('libros/', views.lista_libros, name='lista_libros'),  # Lista de libros
    path('libros/agregar/', views.agregar_libro, name='agregar_libro'),  # Agregar libro
    path('libros/editar/<int:id>/', views.editar_libro, name='editar_libro'),  # Editar libro
    path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),  # Eliminar libro
]
