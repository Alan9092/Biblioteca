from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta de la vista inicio
    path('sidebar/', views.dashboard, name="sidebar"),
    path('index/', views.index, name ="index"),
    path('formagg/', views.formAgg, name='formagg'),
    path('prestamos/', views.prestamos, name='prestamos'),
]