from django import forms
from .models import Prestamo, Libro, Tesis


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

class TesisForm(forms.ModelForm):
    class Meta:
        model = Tesis
        fields = '__all__'