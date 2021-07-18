from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class  Person(models.Model):
    first_name = models.CharField(max_length=15,db_index=True,verbose_name="First Name")
    middle_name = models.CharField(max_length=10,default="",blank=True,verbose_name="Middle Name")
    last_name = models.CharField(max_length=20,verbose_name="Last Name")
    date_of_birth = models.DateField(verbose_name="D.O.B",blank=False)
    gender = models.CharField(choices=[("M","Male"),("F","Female"),("O","Other")],max_length=1)
    contact_no = models.CharField(max_length=10,verbose_name="Contact Number")
    address  = models.TextField(max_length=70,verbose_name="Address")
    joined_date = models.DateTimeField(default=timezone.now,editable=False)

    def __str__(self):
        first_name = self.first_name
        middle_name = " "+self.middle_name+" " if self.middle_name != "" else " "
        last_name = self.last_name
        return first_name+middle_name+last_name
    class Meta:
        abstract = True


class PoliceStation(models.Model):
    police_station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.station_name


class Jail(models.Model):
    jail_id = models.AutoField(primary_key=True)
    jail_name = models.CharField(max_length=30)
    jail_address = models.CharField(max_length=100)

    def __str__(self):
        return self.jail_name

class Cell(models.Model):
    cell_number = models.IntegerField(primary_key=True)
    police_station =  models.ForeignKey(PoliceStation,on_delete=models.CASCADE,null=True)
    jail = models.ForeignKey(Jail,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.cell_number

class Police(Person):
    police_id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name="Username",max_length=20,unique=True)
    password = models.CharField(verbose_name="Password",max_length=20)
    email = models.EmailField(verbose_name="Email Address",unique=True)
    post = models.CharField(max_length=10,verbose_name="Post",null=False)
    police_station = models.ForeignKey(PoliceStation,on_delete=models.SET_NULL,null=True)
    

    def has_module_perms(perm_list,obj=None):
        print(perm_list,obj,"In has perms module")
        return True
    def has_perm(perm,obj=None):
        print(perm,obj,"In has perms")
        return True


class Court(models.Model):
    court_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    court_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.court_name

class Criminal(Person):
        criminal_id = models.AutoField(primary_key=True)
        status = models.CharField(max_length=15)
        photo = models.ImageField()
        height = models.FloatField()
        weight = models.FloatField()
        complexion = models.CharField(max_length=15)
        hair_color = models.CharField(max_length=15)
        birth_mark = models.CharField(max_length=30,null=True)
        eye_color = models.CharField(max_length=15)
        court = models.ForeignKey(Court,on_delete=models.RESTRICT,null=True)
        cell = models.ForeignKey(Cell,on_delete=models.SET_NULL,null=True)

class Punishment(models.Model):
    punishment_id = models.AutoField(primary_key=True)
    punishment_name = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.punishment_name



class Crimes(models.Model):
    criminal = models.ForeignKey(Criminal,on_delete=models.RESTRICT)
    punisment = models.ForeignKey(Punishment,on_delete=models.RESTRICT)
    crime_name = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    reported_by = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.crime_name











