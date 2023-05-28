# Generated by Django 4.1.7 on 2023-05-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reservas',
            name='hora',
            field=models.CharField(default='00:00', max_length=5),
        ),
        migrations.AddField(
            model_name='reservas',
            name='identificacion',
            field=models.CharField(default='00', max_length=50),
        ),
        migrations.AddField(
            model_name='reservas',
            name='numero_contacto',
            field=models.IntegerField(default=123),
        ),
        migrations.AddField(
            model_name='reservas',
            name='primer_nombre',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='reservas',
            name='segundo_nombre',
            field=models.CharField(default='None', max_length=50),
        ),
    ]