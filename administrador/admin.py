from django.contrib import admin
from administrador.models import AdjuntarArchivos
from administrador.models import CargarDocumento
from administrador.models import Conductor
from administrador.models import DescargarRodamiento
from administrador.models import ImprimirRodamiento
from administrador.models import Paradero
from administrador.models import Permisos
from administrador.models import PlanRodamiento
from administrador.models import Rol
from administrador.models import Ruta
from administrador.models import SubirArchivos
from administrador.models import Turno
from administrador.models import Ubicacion
from administrador.models import Usuario
from administrador.models import Vehiculo
# Register your models here.
admin.site.register(AdjuntarArchivos)
admin.site.register(CargarDocumento)
admin.site.register(Conductor)
admin.site.register(DescargarRodamiento)
admin.site.register(ImprimirRodamiento)
admin.site.register(Paradero)
admin.site.register(Permisos)
admin.site.register(PlanRodamiento)
admin.site.register(Rol)
admin.site.register(Ruta)
admin.site.register(SubirArchivos)
admin.site.register(Turno)
admin.site.register(Ubicacion)
admin.site.register(Usuario)
admin.site.register(Vehiculo)