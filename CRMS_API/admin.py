from django.contrib import admin
# Register your models here.
from .models import Police,PoliceStation,Criminal,Crimes,Court,Jail,Cell,Punishment

admin.site.register([Police,Crimes,Criminal,Punishment,Cell,Court,Jail,PoliceStation])
