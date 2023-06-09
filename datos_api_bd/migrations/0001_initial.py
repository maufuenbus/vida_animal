# Generated by Django 4.2 on 2023-04-04 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalAdoptable',
            fields=[
                ('id_anim_adoptable', models.AutoField(primary_key=True, serialize=False)),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(blank=True, max_length=50, null=True)),
                ('tamano', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('ubicacion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AnimalPerdido',
            fields=[
                ('id_anim_perdido', models.AutoField(primary_key=True, serialize=False)),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(blank=True, max_length=50, null=True)),
                ('tamano', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_perdido', models.DateField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudContacto',
            fields=[
                ('id_solic_contac', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('animal_perdido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_api_bd.animalperdido')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_api_bd.persona')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudAdopcion',
            fields=[
                ('id_solic_adop', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('animal_adoptable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_api_bd.animaladoptable')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_api_bd.persona')),
            ],
        ),
        migrations.AddField(
            model_name='animalperdido',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_api_bd.persona'),
        ),
        migrations.CreateModel(
            name='AnimalEncontrado',
            fields=[
                ('id_anim_encontrado', models.AutoField(primary_key=True, serialize=False)),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(blank=True, max_length=50, null=True)),
                ('tamano', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_encontrado', models.DateField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_api_bd.persona')),
            ],
        ),
    ]
