# Generated by Django 4.1.7 on 2023-05-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.CharField(default='00:00', max_length=5)),
                ('estancia', models.IntegerField()),
                ('metodo_pago', models.CharField(max_length=50)),
                ('direccion_factura', models.CharField(max_length=120)),
                ('habitacion', models.IntegerField()),
                ('primer_nombre', models.CharField(default='None', max_length=50)),
                ('segundo_nombre', models.CharField(default='None', max_length=50)),
                ('identificacion', models.CharField(default='00', max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('numero_contacto', models.IntegerField(default=123)),
            ],
        ),
    ]
