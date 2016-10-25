from django.db import models
from django.contrib import admin

class Actor(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

#En una misma pelicula actuan varios actores
#por lo tanto necesitamos una relacion many to many
#recordemos que esto no es SQL por lo tanto las reglas de normalización no se
#aplican, esto es un ORM (orientado a objetos), aunque internamente la BD
#si sea SQL
class Pelicula(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    #actores   = models.ManyToManyField(Actor, related_name='peliculas',  through='Actuacion')
    actores   = models.ManyToManyField(Actor, through='Actuacion')

    def __str__(self):
        return self.nombre

class Actuacion (models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

class ActuacionInLine(admin.TabularInline):
    model = Actuacion
    extra = 1

class ActorAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLine,)

class PeliculaAdmin (admin.ModelAdmin):
    inlines = (ActuacionInLine,)
