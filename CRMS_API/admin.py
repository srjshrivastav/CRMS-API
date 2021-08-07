from django.contrib import admin
# Register your models here.
from .models import Police,PoliceStation,Criminal,FIR,Court,Jail,Cell,Punishment

admin.site.register([Police,FIR,Criminal,Punishment,Cell,Court,Jail,PoliceStation])
