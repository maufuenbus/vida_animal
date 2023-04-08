from django.db import models


# MODELO PERSONA

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return self.id_persona

# MODELO ANIMAL PERDIDO

class AnimalPerdido(models.Model):
    id_anim_perdido = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True, null=True)
    tamano = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    fecha_perdido = models.DateField()
    ubicacion = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.id_anim_perdido

# MODELO ANIMAL ENCONTRADO

class AnimalEncontrado(models.Model):
    id_anim_encontrado = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True, null=True)
    tamano = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    fecha_encontrado = models.DateField()
    ubicacion = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.id_anim_encontrado

# MODELO ANIMAL ADOPTABLE

class AnimalAdoptable(models.Model):
    id_anim_adoptable = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True, null=True)
    tamano = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.id_anim_adoptable

# MODELO SOLICICITUD DE ADOPCION

class SolicitudAdopcion(models.Model):
    id_solic_adop = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    animal_adoptable = models.ForeignKey(AnimalAdoptable, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.id_solic_adop

# MODELO SOLICITUD DE CONTACTO ANIMAL PERDIDO

class SolicitudContacto(models.Model):
    id_solic_contac = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    animal_perdido = models.ForeignKey(AnimalPerdido, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.id_solic_contac