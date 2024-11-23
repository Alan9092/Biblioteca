from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .forms import LibroForm, PrestamoForm
from .models import Libro, Prestamo

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'sidebar.html')

def index(request):
    return render(request, 'index.html')

def formAgg(request):
    return render(request, 'formAgregarLibro.html')

def prestamos(request):
    return render(request, 'Prestamos.html')

def formPL(request):
    return render(request, 'formPrestamo.html')

def Tesis(request):
    return render(request, 'Tesis.html')

def formTesis(request):
    return render(request, 'formTesis.html')

# Vista para listar libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})

# Vista para agregar un libro
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'formAgregarLibro.html', {'form': form})

# Vista para editar un libro
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'formAgregarLibro.html', {'form': form, 'libro': libro})

# Vista para eliminar un libro
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'confirmar_eliminar.html', {'libro': libro})

# Vista para listar préstamos
def nuevo_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')  # Cambia por la vista que liste los préstamos
    else:
        form = PrestamoForm()

    return render(request, 'formPrestamo.html', {'form': form})

def lista_prestamos(request):
    prestamos = Prestamo.objects.select_related('libro').all()  # Optimización con select_related
    return render(request, 'Prestamos.html', {'prestamos': prestamos})

def editar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)

    return render(request, 'formPrestamo.html', {'form': form})

def eliminar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('lista_prestamos')
    return render(request, 'confirm_delete.html', {'prestamo': prestamo})
