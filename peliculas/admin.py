from django.contrib import admin

# Register your models here.
from peliculas.models import Actor, ActorAdmin, Pelicula, PeliculaAdmin

admin.site.register(Actor, ActorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
