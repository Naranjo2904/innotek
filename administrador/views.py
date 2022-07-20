# Librerias del CRUD
from socket import fromshare
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.decorators import login_required
from administrador.forms import *
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


# Importar el modelo de la base de datos de models.py
from .models import *

# Habilitar el uso de mensajes en Django
from django.contrib import messages

# Habilitar los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitar los formularios en Django
from django import forms

#Importaciones para el formulario de registro
from django.http import HttpRequest
#from Models.Usuario.forms import formulariousuario
@login_required




def formularioContacto(request):
    return render (request, "formularioContacto.html")

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["innotekmobil@gmail.com"]
        send_mail (asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render (request, "contactoExitoso.html")
    return render (request, "formularioContacto.html")

# Inicio de sesion






# Registro
#def registro(request):
    #return render (request, "registro.html")


class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registro.html"
    form_class = RegistroForm
    
    def get_success_url(self):        
        return reverse('login')
    


# Estructura inicial
def index(request):
    return render (request, "index.html")


# Recuperar contraseña
def recuperar(request):
    return render (request, "recuperar.html")

def login(request):
    response = redirect('profile')
    return response





# ADJUNTAR ARCHIVOS
class ListadoAdjuntar(ListView):
    model = AdjuntarArchivos

class AdjuntarCrear(SuccessMessageMixin, CreateView):
    model = AdjuntarArchivos
    form = AdjuntarArchivos
    fields = "__all__"
    success_message ='Archivo adjunto creado correctamente'
    def get_success_url(self):        
        return reverse('leer1') # Redireccionamos a la vista principal 'leer'

class AdjuntarDetalle (DetailView):
    model = AdjuntarArchivos

class AdjuntarActualizar(SuccessMessageMixin,UpdateView):
    model = AdjuntarArchivos
    form = AdjuntarArchivos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = '¡Archivo adjunto actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Postre 
    def get_success_url(self):               
        return reverse('leer1') # Redireccionamos a la vista principal 'leer'

class AdjuntarEliminar(SuccessMessageMixin, DeleteView): 
    model = AdjuntarArchivos
    form = AdjuntarArchivos
    fields = "__all__"     
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = '¡Archivo adjunto eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer1') # Redireccionamos a la vista principal 'leer'



# CARGAR DOCUMENTO
class ListadoCargar(ListView):
    model = CargarDocumento
    
class CargarCrear(SuccessMessageMixin, CreateView):
    model = CargarDocumento
    form = CargarDocumento
    fields = "__all__"
    success_message ='Documento cargado creado correctamente'
    def get_success_url(self):        
        return reverse('leer2') 

class CargarDetalle (DetailView):
    model = CargarDocumento

class CargarActualizar(SuccessMessageMixin,UpdateView):
    model = CargarDocumento
    form = CargarDocumento
    fields = "__all__"  
    success_message = '¡Documento cargado actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer2') 

class CargarEliminar(SuccessMessageMixin, DeleteView): 
    model = CargarDocumento
    form = CargarDocumento
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Documento cargado eliminado correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('leer2')



# CONDUCTOR
class ListadoConductor(ListView):
    model = Conductor

class ConductorCrear(SuccessMessageMixin, CreateView):
    model = Conductor
    form = Conductor
    fields = "__all__"
    success_message ='Conductor creado correctamente'
     
    def get_success_url(self):        
        return reverse('leer3') # Redireccionamos a la vista principal 'leer'

class ConductorDetalle (DetailView):
    model = Conductor

class ConductorActualizar(SuccessMessageMixin,UpdateView):
    model = Conductor
    form = Conductor
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = '¡Conductor actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer3') # Redireccionamos a la vista principal 'leer'

class ConductorEliminar(SuccessMessageMixin, DeleteView): 
    model = Conductor
    form = Conductor
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = '¡Conductor eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer3') # Redireccionamos a la vista principal 'leer'



# DESCARGAR RODAMIENTO
class ListadoDescargarRodamiento(ListView):
    model = DescargarRodamiento

class DescargarRodamientoCrear(SuccessMessageMixin, CreateView):
    model = DescargarRodamiento
    form = DescargarRodamiento
    fields = "__all__"
    success_message ='Plan de rodamiento descargado creado correctamente'
    def get_success_url(self):        
        return reverse('leer4') 

class DescargarRodamientoDetalle (DetailView):
    model = DescargarRodamiento

class DescargarRodamientoActualizar(SuccessMessageMixin,UpdateView):
    model = DescargarRodamiento
    form = DescargarRodamiento
    fields = "__all__"  
    success_message = '¡Plan de rodamiento descargado actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer4') 

class DescargarRodamientoEliminar(SuccessMessageMixin, DeleteView): 
    model = DescargarRodamiento
    form = DescargarRodamiento
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Plan de rodamiento descargado eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer4')


# IMPRIMIR RODAMIENTO
class ListadoImprimirRodamiento(ListView):
    model = ImprimirRodamiento

class ImprimirRodamientoCrear(SuccessMessageMixin, CreateView):
    model = ImprimirRodamiento
    form = ImprimirRodamiento
    fields = "__all__"
    success_message ='Plan de rodamiento impreso creado correctamente'
    def get_success_url(self):        
        return reverse('leer5') 

class ImprimirRodamientoDetalle (DetailView):
    model = ImprimirRodamiento

class ImprimirRodamientoActualizar(SuccessMessageMixin,UpdateView):
    model = ImprimirRodamiento
    form = ImprimirRodamiento
    fields = "__all__"  
    success_message = '¡Plan de rodamiento impreso actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer5') 

class ImprimirRodamientoEliminar(SuccessMessageMixin, DeleteView): 
    model = ImprimirRodamiento
    form = ImprimirRodamiento
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Plan de rodamiento impreso eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer5')
 

# PARADERO
class ListadoParadero(ListView):
    model = Paradero

class ParaderoCrear(SuccessMessageMixin, CreateView):
    model = Paradero
    form =  Paradero
    fields = "__all__"
    success_message ='Paradero creado correctamente'
    def get_success_url(self):        
        return reverse('leer6') 

class ParaderoDetalle (DetailView):
    model = Paradero

class ParaderoActualizar(SuccessMessageMixin,UpdateView):
    model = Paradero
    form =  Paradero
    fields = "__all__"  
    success_message = '¡Paradero actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer6') 

class ParaderoEliminar(SuccessMessageMixin, DeleteView): 
    model = Paradero
    form =  Paradero
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Paradero eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer6')

   
# PERMISOS
class ListadoPermisos(ListView):
    model = Permisos

class PermisosCrear(SuccessMessageMixin, CreateView):
    model = Permisos
    form = Permisos
    fields = "__all__"
    success_message ='Permiso creado correctamente'
    def get_success_url(self):        
        return reverse('leer7') 

class PermisosDetalle (DetailView):
    model = Permisos

class PermisosActualizar(SuccessMessageMixin,UpdateView):
    model = Permisos
    form = Permisos
    fields = "__all__"  
    success_message = '¡Permiso actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer7') 

class PermisosEliminar(SuccessMessageMixin, DeleteView): 
    model = Permisos
    form = Permisos
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Permiso eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer7')


# PLAN DE RODAMIENTO
class ListadoPlanRodamiento(ListView):
    model = PlanRodamiento

class PlanRodamientoCrear(SuccessMessageMixin, CreateView):
    model = PlanRodamiento
    form = PlanRodamiento
    fields = "__all__"
    success_message ='Plan de rodamiento creado correctamente'
    def get_success_url(self):        
        return reverse('leer8') 

class PlanRodamientoDetalle (DetailView):
    model = PlanRodamiento

class PlanRodamientoActualizar(SuccessMessageMixin,UpdateView):
    model = PlanRodamiento
    form = PlanRodamiento
    fields = "__all__"  
    success_message = '¡Plan de rodamiento actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer8') 

class PlanRodamientoEliminar(SuccessMessageMixin, DeleteView): 
    model = PlanRodamiento
    form = PlanRodamiento
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Plan de rodamiento eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer8')


# ROL
class ListadoRol(ListView):
    model = Rol

class RolCrear(SuccessMessageMixin, CreateView):
    model = Rol
    form = Rol
    fields = "__all__"
    success_message ='Rol creado correctamente'
    def get_success_url(self):        
        return reverse('leer9') 

class RolDetalle (DetailView):
    model = Rol

class RolActualizar(SuccessMessageMixin,UpdateView):
    model = Rol
    form = Rol
    fields = "__all__"  
    success_message = '¡Rol actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer9') 

class RolEliminar(SuccessMessageMixin, DeleteView): 
    model = Rol
    form = Rol
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Rol eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer9')



# RUTA
class ListadoRuta(ListView):
    model = Ruta
        
class RutaCrear(SuccessMessageMixin, CreateView):
    model = Ruta
    form = Ruta
    fields = "__all__"
    success_message ='Ruta creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer10') 

class RutaDetalle (DetailView):
    model = Ruta

class  RutaActualizar(SuccessMessageMixin,UpdateView):
    model =  Ruta
    form = Ruta
    fields = "__all__" 
    success_message = 'Ruta actualizada correctamente !' 

    def get_success_url(self):               
        return reverse('leer10')
class RutaEliminar(SuccessMessageMixin, DeleteView): 
    model = Ruta 
    form = Ruta
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Ruta eliminada correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer10')    



# SUBIR ARCHIVO
class ListadoSubirArchivos(ListView):
    model = SubirArchivos
    
    
class SubirArchivosCrear(SuccessMessageMixin, CreateView):
    model = SubirArchivos
    form = SubirArchivos
    fields = "__all__"
    success_message ='Archivo creado correctamente'
     
    def get_success_url(self):        
        return reverse('leer11') # Redireccionamos a la vista principal 'leer'

class SubirArchivosDetalle (DetailView):
    model = SubirArchivos

class  SubirArchivosActualizar(SuccessMessageMixin,UpdateView):
    model = SubirArchivos
    form = SubirArchivos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = '¡Archivo subido actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer11') # Redireccionamos a la vista principal 'leer'
class SubirArchivosEliminar(SuccessMessageMixin, DeleteView): 
    model = SubirArchivos 
    form = SubirArchivos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = '¡Archivo subido eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer11') # Redireccionamos a la vista principal 'leer'



# TURNO
class ListadoTurno(ListView):
    model = Turno
    
class TurnoCrear(SuccessMessageMixin, CreateView):
    model = Turno
    form = Turno
    fields = "__all__"
    success_message ='Turno creado correctamente'
     
    def get_success_url(self):        
        return reverse('leer30') # Redireccionamos a la vista principal 'leer'

class TurnoDetalle (DetailView):
    model = Turno

class  TurnoActualizar(SuccessMessageMixin,UpdateView):
    model = Turno
    form = Turno
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Turno actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer30') # Redireccionamos a la vista principal 'leer'

class TurnoEliminar(SuccessMessageMixin, DeleteView): 
    model = Turno
    form = Turno
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = '¡Turno eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer30') # Redireccionamos a la vista principal 'leer'



# UBICACIÓN
class ListadoUbicacion(ListView):
    model = Ubicacion

class UbicacionCrear(SuccessMessageMixin, CreateView):
    model = Ubicacion
    form = Ubicacion
    fields = "__all__"
    success_message ='Ubicación creada correctamente'
    def get_success_url(self):        
        return reverse('leer13') 

class UbicacionDetalle (DetailView):
    model = Ubicacion

class UbicacionActualizar(SuccessMessageMixin,UpdateView):
    model = Ubicacion
    form = Ubicacion
    fields = "__all__"  
    success_message = '¡Ubicación actualizada correctamente!' 
    def get_success_url(self):               
        return reverse('leer13') 

class UbicacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Ubicacion
    form = Ubicacion
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Ubicación eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer13')



# USUARIO
class ListadoUsuario(ListView):
    model = Usuario
    
class UsuarioCrear(SuccessMessageMixin, CreateView):
    model = Usuario
    form = Usuario
    fields = "__all__"
    success_message ='Usuario creado correctamente'
    def get_success_url(self):        
        return reverse('leer14') 

class UsuarioDetalle (DetailView):
    model = Usuario

class UsuarioActualizar(SuccessMessageMixin,UpdateView):
    model = Usuario
    form = Usuario
    fields = "__all__"  
    success_message = '¡Usuario actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer14') 

class UsuarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Usuario
    form = Usuario
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Usuario eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer14')



# VEHÍCULO
class ListadoVehiculo(ListView):
    model = Vehiculo

class VehiculoCrear(SuccessMessageMixin, CreateView):
    model = Vehiculo
    form = Vehiculo
    fields = "__all__"
    success_message ='Vehiculo creado correctamente'
    def get_success_url(self):        
        return reverse('leer15') 

class VehiculoDetalle (DetailView):
    model = Vehiculo

class VehiculoActualizar(SuccessMessageMixin,UpdateView):
    model = Vehiculo
    form = Vehiculo
    fields = "__all__"  
    success_message = '¡Vehiculo actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer15') 

class VehiculoEliminar(SuccessMessageMixin, DeleteView): 
    model = Vehiculo
    form = Vehiculo
    fields = "__all__"     

    def get_success_url(self): 
        success_message = '¡Vehiculo eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer15')