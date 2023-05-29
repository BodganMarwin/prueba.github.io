from django.db import models

# Create your models here.

class Focable(models.Model):
    codigo = models.CharField(unique=True, max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    subtipo = models.CharField(max_length=20, blank=True, null=True)
    capacidad = models.SmallIntegerField(blank=True, null=True)
    buffer = models.SmallIntegerField(blank=True, null=True)
    marca = models.CharField(max_length=20, blank=True, null=True)
    geometria = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'focable'


class Foconexion(models.Model):
    codigo = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    subtipo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'foconexion'


class Fodio(models.Model):
    codigo = models.SmallIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    sala = models.SmallIntegerField(blank=True, null=True)
    rack = models.SmallIntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    subtipo = models.CharField(max_length=20, blank=True, null=True)
    odf = models.ForeignKey('Foodf', models.DO_NOTHING, db_column='odf', blank=True, null=True)
    tabla = models.CharField(max_length=30, blank=True, null=True)
    externo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fodio'


class Foenlace(models.Model):
    codigo = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    subtipo = models.CharField(max_length=20, blank=True, null=True)
    capacidad = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'foenlace'


class Foenlacedet(models.Model):
    idenlace = models.ForeignKey(Foenlace, models.DO_NOTHING, db_column='idenlace', blank=True, null=True)
    posicion = models.SmallIntegerField(blank=True, null=True)
    idhilo = models.ForeignKey('Fohilo', models.DO_NOTHING, db_column='idhilo', blank=True, null=True)
    fila = models.SmallIntegerField(blank=True, null=True)
    columna = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'foenlacedet'


class Fohilo(models.Model):
    hilo = models.SmallIntegerField(blank=True, null=True)
    posicion = models.SmallIntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    buffer = models.SmallIntegerField(blank=True, null=True)
    colorbuffer = models.CharField(max_length=10, blank=True, null=True)
    ststecnico = models.CharField(max_length=10, blank=True, null=True)
    stsocupacion = models.CharField(max_length=10, blank=True, null=True)
    stsoperativo = models.CharField(max_length=10, blank=True, null=True)
    cable = models.ForeignKey(Focable, models.DO_NOTHING, db_column='cable', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fohilo'


class Foodf(models.Model):
    codigo = models.CharField(unique=True, max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    geometria = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'foodf'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'spatial_ref_sys'

