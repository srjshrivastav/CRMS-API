from django.contrib import admin
# Register your models here.
from .models import Police,PoliceStation,Criminal,FIR,Court,Jail,Cell,Punishment



@admin.register(FIR)
class FIRAdmin(admin.ModelAdmin):
    list_display = ("crime_type", "crime_place", "fir_dateTime")
    autocomplete_fields =["criminal"]
    
@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    list_display=("first_name","middle_name","last_name","post")


@admin.register(Criminal)
class CriminalAdmin(admin.ModelAdmin):
    list_display=("first_name","middle_name","last_name","status")
    search_fields = ['foreignkeyfield__criminal_id']

admin.site.register([Punishment,Cell,Court,Jail,PoliceStation])