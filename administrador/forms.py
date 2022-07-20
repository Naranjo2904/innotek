from cProfile import *
from dataclasses import *
from pyexpat import *
from socket import *
from tkinter import Widget

from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User 
        fields = [
                 'username',
                 'first_name',
                 'last_name',
                 'email',
        ]


#from administrador.models import *
#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate, Usuario
#from django import forms 

#class Usuario(UserCreationForm):
 #   contraseña = forms.CharField(label="contraseña", widget=forms.PasswordInput)
  #  contraseña = forms.CharField(label="Comfirmar contraseña", widget=forms.PasswordInput)
   # class Meta:
    #    model = Usuario
     #   fields = ('correo_electronico', 'contraseña')
      #  labels = ('nombre','apellido','tipo_documento','numero_documento','telefono')
        
        
#class AutenticarForm(forms.ModelForm):
 #   password = forms.CharField(label ='contraseña', Widget=forms.PasswordInput)
    
  #  class Meta:
   #     model = Usuario
    #    fields = ('correo_electronico', 'contraseña')
        
     #   def clean(self):
      #      correo_electronico = self.cleaned_data['correo_electronico']
       #     contraseña = self.cleaned_data['contraseña']
            
        #    if not authenticate(correo_electronico=correo_electronico, contraseña=contraseña):
         #       raise forms.ValidationError("El email o la contraseña son incorrectos")      
    
    
    
    
    
    