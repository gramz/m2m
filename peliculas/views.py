from django.shortcuts import render
from django.contrib import messages
from .forms import PeliculaForm
from peliculas.models import Pelicula, Actuacion

# Create your views here.

def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'pelicula/pelicula_lista.html', {'peliculas':peliculas})

'''
def pelicula_nueva(request):
    formulario = PeliculaForm()
    return render(request, 'pelicula/pelicula_editar.html', {'formulario': formulario})


def pelicula_nueva(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            #pelicula = formulario.save(commit=False)
            pelicula = formulario.save()
            #pelicula.save()
            formulario.save_m2m()
    else:
        formulario = PeliculaForm()
    return render(request, 'pelicula/pelicula_editar.html', {'formulario': formulario})
'''

def pelicula_nueva(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            pelicula = Pelicula.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])

            for actor_id in request.POST.getlist('actores'):
                actuacion = Actuacion(actor_id=actor_id, pelicula_id = pelicula.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = PeliculaForm()
    return render(request, 'pelicula/pelicula_editar.html', {'formulario': formulario})
