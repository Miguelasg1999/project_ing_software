from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import FormularioCurso, EditarFormularioCurso
from .models import Curso

#------------------------CLIENT-------------------------
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('index')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las Contraseñas no coinciden'
                })

def signout(request):
    logout(request)
    return redirect('index')

def products(request):
    return render(request, 'products.html')

#------------------------------------------------------




#------------------------ADMIN-------------------------

def register_course(request):
    if request.method == "GET":
        form = {'form': FormularioCurso}
        return render(request, 'admin/register_course.html', form)
    else:
        curso = Curso.objects.create(colegio=request.POST['colegio'],nivel_curso=request.POST['nivel_curso'],cantidad_alumnos=request.POST['cantidad_alumnos'],servicio=request.POST['servicio'],destino=request.POST['destino'], fecha_viaje=request.POST['fecha_viaje'],monto_depositado=request.POST['monto_depositado'],meta_monto=int(request.POST['cantidad_alumnos']) * 500000, id_cliente_id=request.POST['id_cliente'])
        curso.save()
        return redirect('list_course')

def list_course(request):
    cursos = { 'cursos': Curso.objects.all() }
    return render(request, 'admin/list_course.html', cursos)

def admin_index(request):

    return render(request, 'admin/admin_index.html')

def admin_signin(request):
    if request.method == 'GET':
        return render(request, 'admin/admin_signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'admin/admin_signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('admin_index')

def admin_signup(request):
    if request.method == 'GET':
        return render(request, 'admin/admin_signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('admin_index')
            except IntegrityError:
                return render(request, 'admin/admin_signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'admin/admin_signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las Contraseñas no coinciden'
                })
def admin_signout(request):
    logout(request)
    return redirect('admin_index')

def edit_reg(request, id):
    curso = Curso.objects.get(pk=id)
    if request.method == "GET":
        form = EditarFormularioCurso(instance=curso)
        return render(request, 'admin/edit_reg.html',{
            'form': form,
            'curso': curso
        })
    else:
        curso.colegio = request.POST['colegio']
        curso.nivel_curso = request.POST['nivel_curso']
        curso.cantidad_alumnos = request.POST['cantidad_alumnos']
        curso.servicio = request.POST['servicio']
        curso.destino = request.POST['destino']
        curso.id_cliente_id = request.POST['id_cliente']
        curso.meta_monto = int(request.POST['cantidad_alumnos']) * 500000
        curso.save()
        return redirect('list_course')

def delete_reg(request, id):
    Curso.objects.get(pk=id).delete()
    return redirect('list_course')
#------------------------------------------------------
