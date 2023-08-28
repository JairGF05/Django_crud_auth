from django.shortcuts import render
#from django.http import HttpResponse
#libreria de autenticación de Django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    """ indicamos que hace si recibe GET o POST"""

    #Si me visitan con el metodo GET enviamos el formulario
    if request.method == 'GET':
        print('Enviando formulario, GET')
        return render(request, 'signup.html', {
            'form': UserCreationForm,
        })
    else:
        print(request.POST)
        print('Obteniendo datos, POST')

        if request.POST['password1'] == request.POST['password2']:
            #si coinciden guardamos los datos usando el modelo User de Django

    



    return render(request, 'signup.html',{
        'form': UserCreationForm,
    })
