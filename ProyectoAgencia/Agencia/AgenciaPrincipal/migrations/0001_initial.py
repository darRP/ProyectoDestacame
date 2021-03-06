# Generated by Django 2.1.5 on 2019-02-10 18:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patente', models.CharField(max_length=10)),
                ('AsientoDisponibles', models.IntegerField(default=10, editable=False, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('Pasajeros', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Hora_Inicio', models.DateTimeField(auto_now_add=True)),
                ('Hora_Fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=30)),
                ('Nombre', models.CharField(max_length=30)),
                ('ApellidoPaterno', models.CharField(max_length=30)),
                ('ApellidoMaterno', models.CharField(max_length=30)),
                ('Direccion', models.CharField(max_length=50)),
                ('Telefono', models.IntegerField()),
                ('Eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trayecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lugar_Inicio', models.CharField(max_length=60)),
                ('Lugar_Fin', models.CharField(max_length=60)),
                ('Bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgenciaPrincipal.Bus')),
                ('Horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgenciaPrincipal.Horario')),
            ],
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AgenciaPrincipal.Persona')),
                ('NumeroDeLicencia', models.CharField(max_length=100)),
            ],
            bases=('AgenciaPrincipal.persona',),
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AgenciaPrincipal.Persona')),
                ('NumeroAsientoAsginado', models.IntegerField()),
                ('BusAsignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgenciaPrincipal.Bus')),
            ],
            bases=('AgenciaPrincipal.persona',),
        ),
        migrations.AddField(
            model_name='bus',
            name='Chofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgenciaPrincipal.Chofer'),
        ),
    ]
