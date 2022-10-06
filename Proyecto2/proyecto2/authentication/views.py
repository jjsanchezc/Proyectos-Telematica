from django.http import HttpResponse
from django.shortcuts import render

from authentication.forms import usuario_form
from .models import Usuario

# Create your views here.
def seleccion(request):
    return render(request,'./select_type_user.html',{})

def user_data(request):
    datos=request.POST
    formulario=usuario_form(request.POST or None)
    if formulario.is_valid():
        print('si es valido')
    print(datos)
    return render(request,'./user_data.html',{})