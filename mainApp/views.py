from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .forms import LibroForm, PrestamoForm, TesisForm
from .models import Libro, Prestamo, Tesis
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from login_required import login_not_required
from django.contrib.auth import login
from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  

@login_not_required
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, 'Correo o contraseña incorrectos')
            return render(request, 'login.html')
    return render(request, 'login.html')

# Vista para validar el correo

@login_not_required 
@csrf_exempt
def validar_correo(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            usuario = Usuario.objects.get(correo=email)
            return JsonResponse({"valid": True, "correo": usuario.correo})
        except Usuario.DoesNotExist:
            return JsonResponse({"valid": False, "message": "No existe el correo."})
    return JsonResponse({"valid": False, "message": "Método no permitido."})

# Vista para validar la contraseña

@login_not_required 
@csrf_exempt
def validar_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'valid': True, 'redirect_url': '/index/'})
        else:
            return JsonResponse({'valid': False, 'message': 'Credenciales inválidas'})



# Create your views here.


def index(request):
    return render(request, 'index.html')  # Redirige a index.html

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



def formTesis(request):
    return render(request, 'formTesis.html')

# Vista para listar libros
def index(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros}) 
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

def crear_editar_tesis(request, pk=None):
    tesis = get_object_or_404(Tesis, pk=pk) if pk else None
    if request.method == 'POST':
        form = TesisForm(request.POST, instance=tesis)
        if form.is_valid():
            form.save()
            return redirect('listar_tesis')
    else:
        form = TesisForm(instance=tesis)
        
    return render(request, 'formTesis.html', {'form': form})

def listar_tesis(request):
    tesis_list = Tesis.objects.all()
    return render(request, 'Tesis.html', {'tesis_list': tesis_list})

def eliminar_tesis(request, pk):
    tesis = get_object_or_404(Tesis, pk=pk)
    if request.method == 'POST':
        tesis.delete()
        return redirect('listar_tesis')
    return render(request, 'eliminar_tesis.html', {'tesis': tesis})