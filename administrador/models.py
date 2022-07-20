# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from email.policy import default
from operator import pos
import profile
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#import os
#from PIL import Image
#from django.db.models.signals import post_save

 
        
        
        


class AdjuntarArchivos(models.Model):
    iddocumento = models.AutoField(primary_key=True)
    registro_fotografico = models.ImageField(upload_to='fotobuses', null= True)
    soat = models.TextField()
    tecnomecanico = models.TextField()
    identificacion_propietario = models.TextField()
    tarjeta_propiedad = models.TextField()

    class Meta:
        managed = False
        db_table = 'adjuntar_archivos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CargarDocumento(models.Model):
    iddocumento = models.AutoField(primary_key=True)
    certificado_alcoholemia = models.TextField()
    certificado_sustancias_psicoactivas = models.TextField()

    class Meta:
        managed = False
        db_table = 'cargar_documento'


class Conductor(models.Model):
    idconductor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo_electronico = models.CharField(max_length=30)
    tipo_identificacion = models.CharField(max_length=20)
    numero_identificacion = models.PositiveIntegerField()
    fecha_expedicion_documento = models.DateField()
    lugar_expedicion_documento = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveIntegerField()
    direccion = models.CharField(max_length=20)
    telefono = models.PositiveIntegerField()
    telefono_alterno = models.PositiveIntegerField()
    turno_idturno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='turno_idturno')
    subir_archivos_iddocumento = models.ForeignKey('SubirArchivos', models.DO_NOTHING, db_column='subir_archivos_iddocumento')

    class Meta:
        managed = False
        db_table = 'conductor'


class DescargarRodamiento(models.Model):
    iddescargar = models.AutoField(primary_key=True)
    documento = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descargar_rodamiento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImprimirRodamiento(models.Model):
    idimprimir_rodamiento = models.AutoField(primary_key=True)
    documento = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imprimir_rodamiento'


class Paradero(models.Model):
    idparadero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    ubicacion_idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='ubicacion_idubicacion')
    ruta_idruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='ruta_idruta')

    class Meta:
        managed = False
        db_table = 'paradero'


class Permisos(models.Model):
    idpermisos = models.AutoField(primary_key=True)
    tipo_permiso = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'permisos'


class PlanRodamiento(models.Model):
    idplan_rodamiento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    inicio_ruta = models.CharField(max_length=30)
    vehiculo = models.PositiveIntegerField(blank=True, null=True)
    ruta = models.PositiveIntegerField(blank=True, null=True)
    vehiculo_idvehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_idvehiculo')
    ruta_idruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='ruta_idruta')
    cargar_documento_iddocumento = models.ForeignKey(CargarDocumento, models.DO_NOTHING, db_column='cargar_documento_iddocumento')
    imprimir_rodamiento_idimprimir_rodamiento = models.ForeignKey(ImprimirRodamiento, models.DO_NOTHING, db_column='imprimir_rodamiento_idimprimir_rodamiento')
    descargar_rodamiento_iddescargar = models.ForeignKey(DescargarRodamiento, models.DO_NOTHING, db_column='descargar_rodamiento_iddescargar')

    class Meta:
        managed = False
        db_table = 'plan_rodamiento'


class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    tipo_rol = models.CharField(max_length=70)
    permisos_idpermisos = models.ForeignKey(Permisos, models.DO_NOTHING, db_column='permisos_idpermisos')

    class Meta:
        managed = False
        db_table = 'rol'


class Ruta(models.Model):
    idruta = models.AutoField(primary_key=True)
    inicio_ruta = models.CharField(max_length=30)
    fin_ruta = models.CharField(max_length=30)
    numero_ruta = models.PositiveIntegerField()
    distancia_kilometros = models.PositiveIntegerField()
    tiempo_estimado = models.CharField(max_length=15, blank=True, null=True)
    numero_vueltas = models.PositiveIntegerField(blank=True, null=True)
    vehiculo_idvehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_idvehiculo')

    class Meta:
        managed = False
        db_table = 'ruta'


class SubirArchivos(models.Model):
    iddocumento = models.AutoField(primary_key=True)
    documento_identidad = models.TextField()
    experiencia_laboral = models.TextField()
    licencia_conduccion = models.TextField()

    class Meta:
        managed = False
        db_table = 'subir_archivos'


class Turno(models.Model):
    idturno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()

    class Meta:
        managed = False
        db_table = 'turno'


class Ubicacion(models.Model):
    idubicacion = models.AutoField(primary_key=True)
    longitud = models.FloatField()
    latitud = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ubicacion'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    tipo_documento = models.CharField(max_length=45)
    numero_documento = models.CharField(max_length=45)
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=70)
    contrasena = models.CharField(max_length=8)
    rol_idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_idrol')
    ubicacion_idubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='ubicacion_idubicacion')

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculo(models.Model):
    idvehiculo = models.AutoField(primary_key=True)
    numero_orden = models.PositiveIntegerField()
    numero_licencia_transito = models.PositiveIntegerField()
    nombre_propietario = models.CharField(max_length=45)
    identificacion_propietario = models.PositiveIntegerField()
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)
    linea = models.CharField(max_length=20)
    modelo = models.PositiveIntegerField()
    capacidad_personas = models.PositiveIntegerField()
    clase_vehiculo = models.CharField(max_length=20)
    cilindraje = models.FloatField()
    numero_chasis = models.CharField(max_length=20)
    tipo_combustible = models.CharField(max_length=10)
    numero_motor = models.CharField(max_length=20)
    tipo_carroceria = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    vin = models.CharField(max_length=20)
    numero_ejes = models.IntegerField()
    conductor_idconductor = models.ForeignKey(Conductor, models.DO_NOTHING, db_column='conductor_idconductor')
    adjuntar_archivos_iddocumento = models.ForeignKey(AdjuntarArchivos, models.DO_NOTHING, db_column='adjuntar_archivos_iddocumento')
    ubicacion_idubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='ubicacion_idubicacion')

    class Meta:
        managed = False
        db_table = 'vehiculo'
