"""innotekmobil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from administrador.views import *
#from administrador import views
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.views import LoginView
from django.conf import settings
#from django.conf.urls.static import static 


urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar),
    #path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',index),
    path('recuperar/', recuperar),
    path('registro/', RegistroUsuario.as_view(),),
    
    
    
 # ADJUNTAR ARCHIVOS
    path('adjuntar_archivos/', ListadoAdjuntar.as_view(template_name = "adjuntar_archivos/formularioadjuntar.html"), name='leer1'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro 
    path('adjuntar_archivos/detalle/<int:pk>', AdjuntarDetalle.as_view(template_name = "adjuntar_archivos/detalle.html"), name='detalles'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un registro  
    path('adjuntar_archivos/crear', AdjuntarCrear.as_view(template_name = "adjuntar_archivos/crear.html"), name='crear'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro de la Base de Datos 
    path('adjuntar_archivos/editar/<int:pk>', AdjuntarActualizar.as_view(template_name = "adjuntar_archivos/actualizar.html"), name='actualizar'), 
    # La ruta 'eliminar' que usaremos para eliminar un registro de la Base de Datos 
    path('adjuntar_archivos/eliminar/<int:pk>', AdjuntarEliminar.as_view(), name='adjuntar_archivos/eliminar.html'),


    # CARGAR DOCUMENTO
    path('cargar_documento/', ListadoCargar.as_view(template_name = "cargar_documento/formulariocargar.html"), name='leer2'),
    path('cargar_documento/detalle/<int:pk>', CargarDetalle.as_view(template_name = "cargar_documento/detalle.html"), name='detalles'),
    path('cargar_documento/crear', CargarCrear.as_view(template_name = "cargar_documento/crear.html"), name='crear'),
    path('cargar_documento/editar/<int:pk>', CargarActualizar.as_view(template_name = "cargar_documento/actualizar.html"), name='actualizar'), 
    path('cargar_documento/eliminar/<int:pk>', CargarEliminar.as_view(), name='cargar_documento/eliminar.html'),

    
    # CONDUCTOR
    path('conductor/', ListadoConductor.as_view(template_name = "conductor/formularioconductor.html"), name='leer3'),
    path('conductor/detalle/<int:pk>', ConductorDetalle.as_view(template_name = "conductor/detalle.html"), name='detalles'),
    path('conductor/crear', ConductorCrear.as_view(template_name = "conductor/crear.html"), name='crear'),
    path('conductor/editar/<int:pk>', ConductorActualizar.as_view(template_name = "conductor/actualizar.html"), name='actualizar'), 
    path('conductor/eliminar/<int:pk>', ConductorEliminar.as_view(), name='conductor/eliminar.html'),

    # DESCARGAR RODAMIENTO 
    path('descargar_rodamiento/', ListadoDescargarRodamiento.as_view(template_name = "descargar_rodamiento/formulariodescargar.html"), name='leer4'),
    path('descargar_rodamiento/detalle/<int:pk>', DescargarRodamientoDetalle.as_view(template_name = "descargar_rodamiento/detalle.html"), name='detalles'),
    path('descargar_rodamiento/crear', DescargarRodamientoCrear.as_view(template_name = "descargar_rodamiento/crear.html"), name='crear'),
    path('descargar_rodamiento/editar/<int:pk>', DescargarRodamientoActualizar.as_view(template_name = "descargar_rodamiento/actualizar.html"), name='actualizar'), 
    path('descargar_rodamiento/eliminar/<int:pk>', DescargarRodamientoEliminar.as_view(), name='descargar_rodamiento/eliminar.html'),

    # IMPRIMIR RODAMIENTO
    path('imprimir_rodamiento/', ListadoImprimirRodamiento.as_view(template_name = "imprimir_rodamiento/formularioimprimir.html"), name='leer5'),
    path('imprimir_rodamiento/detalle/<int:pk>', ImprimirRodamientoDetalle.as_view(template_name = "imprimir_rodamiento/detalle.html"), name='detalles'),
    path('imprimir_rodamiento/crear', ImprimirRodamientoCrear.as_view(template_name = "imprimir_rodamiento/crear.html"), name='crear'),
    path('imprimir_rodamiento/editar/<int:pk>', ImprimirRodamientoActualizar.as_view(template_name = "imprimir_rodamiento/actualizar.html"), name='actualizar'), 
    path('imprimir_rodamiento/eliminar/<int:pk>', ImprimirRodamientoEliminar.as_view(), name='imprimir_rodamiento/eliminar.html'),
    
    # PARADERO
    path('paradero/', ListadoParadero.as_view(template_name = "paradero/formularioparadero.html"), name='leer6'),
    path('paradero/detalle/<int:pk>', ParaderoDetalle.as_view(template_name = "paradero/detalle.html"), name='detalles'),
    path('paradero/crear', ParaderoCrear.as_view(template_name = "paradero/crear.html"), name='crear'),
    path('paradero/editar/<int:pk>', ParaderoActualizar.as_view(template_name = "paradero/actualizar.html"), name='actualizar'), 
    path('paradero/eliminar/<int:pk>', ParaderoEliminar.as_view(), name='paradero/eliminar.html'),

    # PERMISOS
    path('permisos/', ListadoPermisos.as_view(template_name = "permisos/formulariopermisos.html"), name='leer7'),
    path('permisos/detalle/<int:pk>', PermisosDetalle.as_view(template_name = "permisos/detalle.html"), name='detalles'),
    path('permisos/crear', PermisosCrear.as_view(template_name = "permisos/crear.html"), name='crear'),
    path('permisos/editar/<int:pk>', PermisosActualizar.as_view(template_name = "permisos/actualizar.html"), name='actualizar'), 
    path('permisos/eliminar/<int:pk>', PermisosEliminar.as_view(), name='permisos/eliminar.html'),

    # PLAN DE RODAMIENTO
    path('plan_rodamiento/', ListadoPlanRodamiento.as_view(template_name = "plan_rodamiento/formulariorodamiento.html"), name='leer8'),
    path('plan_rodamiento/detalle/<int:pk>', PlanRodamientoDetalle.as_view(template_name = "plan_rodamiento/detalle.html"), name='detalles'),
    path('plan_rodamiento/crear', PlanRodamientoCrear.as_view(template_name = "plan_rodamiento/crear.html"), name='crear'),
    path('plan_rodamiento/editar/<int:pk>', PlanRodamientoActualizar.as_view(template_name = "plan_rodamiento/actualizar.html"), name='actualizar'), 
    path('plan_rodamiento/eliminar/<int:pk>', PlanRodamientoEliminar.as_view(), name='plan_rodamiento/eliminar.html'),

    # ROL
    path('rol/', ListadoRol.as_view(template_name = "rol/formulariorol.html"), name='leer9'),
    path('rol/detalle/<int:pk>', RolDetalle.as_view(template_name = "rol/detalle.html"), name='detalles'),
    path('rol/crear', RolCrear.as_view(template_name = "rol/crear.html"), name='crear'),
    path('rol/editar/<int:pk>', RolActualizar.as_view(template_name = "rol/actualizar.html"), name='actualizar'), 
    path('rol/eliminar/<int:pk>', RolEliminar.as_view(), name='rol/eliminar.html'),

    # RUTA
    path('ruta/', ListadoRuta.as_view(template_name = "ruta/formularioruta.html"), name='leer10'),
    path('ruta/detalle/<int:pk>', RutaDetalle.as_view(template_name = "ruta/detalle.html"), name='detalles'),  
    path('ruta/crear', RutaCrear.as_view(template_name = "ruta/crear.html"), name='crear'),
    path('ruta/editar/<int:pk>', RutaActualizar.as_view(template_name = "ruta/actualizar.html"), name='actualizar'), 
    path('ruta/eliminar/<int:pk>', RutaEliminar.as_view(), name='ruta/eliminar.html'),

    # SUBIR ARCHIVOS
    path('subir_archivos/', ListadoSubirArchivos.as_view(template_name = "subir_archivos/formulariosubir.html"), name='leer11'),
    path('subir_archivos/detalle/<int:pk>', SubirArchivosDetalle.as_view(template_name = "subir_archivos/detalle.html"), name='detalles'),
    path('subir_archivos/crear', SubirArchivosCrear.as_view(template_name = "subir_archivos/crear.html"), name='crear'),
    path('subir_archivos/editar/<int:pk>', SubirArchivosActualizar.as_view(template_name = "subir_archivos/actualizar.html"), name='actualizar'),
    path('subir_archivos/eliminar/<int:pk>', SubirArchivosEliminar.as_view(), name='subir_archivos/eliminar.html'),

    # TURNO
    path('turno/', ListadoTurno.as_view(template_name = "turno/formularioturno.html"), name='leer30'),
    path('turno/detalle/<int:pk>', TurnoDetalle.as_view(template_name = "turno/detalle.html"), name='detalles'),
    path('turno/crear', TurnoCrear.as_view(template_name = "turno/crear.html"), name='crear'),
    path('turno/editar/<int:pk>', TurnoActualizar.as_view(template_name = "turno/actualizar.html"), name='actualizar'), 
    path('turno/eliminar/<int:pk>', TurnoEliminar.as_view(), name='turno/eliminar.html'),  

    # UBICACIÓN
    path('ubicacion/', ListadoUbicacion.as_view(template_name = "ubicacion/formularioubicacion.html"), name='leer13'),
    path('ubicacion/detalle/<int:pk>', UbicacionDetalle.as_view(template_name = "ubicacion/detalle.html"), name='detalles'),
    path('ubicacion/crear', UbicacionCrear.as_view(template_name = "ubicacion/crear.html"), name='crear'),
    path('ubicacion/editar/<int:pk>', UbicacionActualizar.as_view(template_name = "ubicacion/actualizar.html"), name='actualizar'), 
    path('ubicacion/eliminar/<int:pk>', UbicacionEliminar.as_view(), name='ubicacion/eliminar.html'), 

    # USUARIO
    path('usuario/', ListadoUsuario.as_view(template_name = "usuario/formulariousuario.html"), name='leer14'),
    path('usuario/detalle/<int:pk>', UsuarioDetalle.as_view(template_name = "usuario/detalle.html"), name='detalles'),
    path('usuario/crear', UsuarioCrear.as_view(template_name = "usuario/crear.html"), name='crear'),
    path('usuario/editar/<int:pk>', UsuarioActualizar.as_view(template_name = "usuario/actualizar.html"), name='actualizar'), 
    path('usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(), name='usuario/eliminar.html'),  
    
    # VEHÍCULO
    path('vehiculo/', ListadoVehiculo.as_view(template_name = "vehiculo/formulariovehiculo.html"), name='leer15'),
    path('vehiculo/detalle/<int:pk>', VehiculoDetalle.as_view(template_name = "vehiculo/detalle.html"), name='detalles'),
    path('vehiculo/crear', VehiculoCrear.as_view(template_name = "vehiculo/crear.html"), name='crear'),
    path('vehiculo/editar/<int:pk>', VehiculoActualizar.as_view(template_name = "vehiculo/actualizar.html"), name='actualizar'), 
    path('vehiculo/eliminar/<int:pk>', VehiculoEliminar.as_view(), name='vehiculo/eliminar.html'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,documen_root=settings.MEDIA_ROOT)