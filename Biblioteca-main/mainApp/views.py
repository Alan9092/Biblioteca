from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

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
