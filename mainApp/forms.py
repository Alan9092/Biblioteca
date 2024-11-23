from django import forms
from .models import Prestamo, Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'folio', 'editorial', 'volumen', 'area']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor del libro'}),
            'folio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Folio del libro'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Editorial'}),
            'volumen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Volumen'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Área'})
        }
        
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = [
            'numero_control', 'nombre', 'grado', 'grupo', 'fecha_entrega', 
            'fecha_devolucion', 'estado', 'codigo_barras', 'libro'
        ]
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }
