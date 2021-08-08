from django.core.files import storage
from django.core.files.storage import FileSystemStorage
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
    joining_date = models.DateField(default=timezone.now,editable=False)
    photo = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return f"{self.first_name} "+f"{self.middle_name} "+f"{self.last_name}"

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
        return str(self.cell_number)

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
        height = models.FloatField()
        weight = models.FloatField()
        complexion = models.CharField(max_length=15)
        hair_color = models.CharField(max_length=15)
        birth_mark = models.CharField(max_length=30,null=True)
        eye_color = models.CharField(max_length=15)
        court = models.ForeignKey(Court,on_delete=models.RESTRICT,null=True,blank=True)
        cell = models.ForeignKey(Cell,on_delete=models.SET_NULL,null=True,blank=True)


class Punishment(models.Model):
    punishment_id = models.AutoField(primary_key=True)
    punishment_name = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.punishment_name



class FIR(models.Model):
    CRIME_CHOICES = [
    ('MUR', 'Murder'),
    ('KID', 'Kidnapping'),
    ('TFT', 'Theft'),
    ('RAP', 'Rape'),
    ('ACC', 'Accident'),
    ('VOL', 'Voilence'),
]
    FIR_STATUS = [
        ('CL',"Closed"),
        ('OP','Open')
    ]
    crime_place = models.CharField(max_length=30)
    crime_type = models.CharField(max_length=3,choices=CRIME_CHOICES,default='TFT')
    crime_dateTime = models.DateTimeField(verbose_name="Crime date and Time",default=timezone.now)
    fir_dateTime = models.DateTimeField(verbose_name="Fir date and Time",default=timezone.now,editable=False)
    description = models.CharField(verbose_name="Crime description",max_length=1000)
    victim_name = models.CharField(verbose_name="Victim Name",blank=True,max_length=30)
    reporter_name = models.CharField(verbose_name="Reporter name",null=False,max_length=30)
    reporter_photo = models.ImageField(verbose_name="Reporter Photo",upload_to='images/',blank=True)
    repoter_phone_number = models.CharField(verbose_name="Reporter Contact No.",max_length=10)
    fir_status = models.CharField(max_length=2,choices=FIR_STATUS,default='OP')
    criminal = models.ForeignKey(Criminal,on_delete=models.PROTECT,blank=True,null=True,related_name = "firOf")
    punishment = models.ForeignKey(Punishment,on_delete=models.PROTECT,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.fir_dateTime = timezone.now()
        super(FIR,self).save(*args,**kwargs)
    def __str__(self):
        return "Reported By "+self.reporter_name











