from django.shortcuts import render, redirect
from django.http import HttpResponse
# libreria de autenticación de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    """ indicamos que hace si recibe GET o POST"""

    # Si me visitan con el metodo GET enviamos el formulario
    if request.method == 'GET':
        print('Enviando formulario, GET')
        return render(request, 'signup.html', {
            'form': UserCreationForm,
        })
    else:
        print(request.POST)
        print('Obteniendo datos, POST')

        if request.POST['password1'] == request.POST['password2']:
            # Es importante el uso de try y except, si hay un error la aplicacion no falla
            # si coinciden guardamos los datos usando el modelo User de Django
            try:
                # creacion de usuario, aun no lo guarda, ademas cifra el pass
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                # Ahora lo guardamos, lo tratara de guardar en db.sqlite
                user.save()
                #guardar cookie: una vez guardado ejecutar login pasando request y el usuario
                login(request, user)
                # redirecionamos a localhost:8000/tasks/
                return redirect('tasks')

            except Exception as e:
                # se vuelve a enviar el signup, y enviamos el error
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe',
                })

        # si no coinciden(else) enviar formulario con mensaje de error
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden',
        })

    return render(request, 'signup.html', {
        'form': UserCreationForm,
    })


def tasks(request):
   return render(request, 'tasks.html')

#funcion para manejar el logout
def signout(request):
    logout(request)
    return redirect('home')

#funcion para manejar el login
def signin(request):
    #se va a enviar un formulario para el Login
    #primero tenemos que validar los datos ingresados al formulario
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form':AuthenticationForm,
        })
    else:
        print(request.POST)
        print('Obteniendo datos POST')
        #comprobar en la base deatos si existe el usuario
        #devuelve un user si es valido, sino estara vacio
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        #si no existe el usuario
        if user is None:
            return render(request, 'signin.html', {
            'form':AuthenticationForm,
            'error': "Username or password is incorrect"
            })
        #si el usuario y pass es correcto
        else:
            #guardamos la sesion del usuario que se autenticó correctamente
            login(request, user)
            #redireccionamos a tasks
            redirect('tasks')
