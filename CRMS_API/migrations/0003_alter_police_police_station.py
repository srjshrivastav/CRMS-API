# Generated by Django 3.2.2 on 2021-08-11 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRMS_API', '0002_auto_20210808_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='police_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRMS_API.policestation'),
        ),
    ]