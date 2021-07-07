from django import forms
from django.forms import ModelForm,widgets
from django.forms.models import ModelForm
from .models import Colaboradores

class ColaboradoresForm(forms.ModelForm):

    class Meta:
        model = Colaboradores
        fields = ['rut','image','nombreComp','telefono','direccion','email','contrasenia','pais']

        labels={
            'rut': 'Rut',
            'image': 'Imagen',
            'nombreComp': 'Nombre_Completo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'email': 'Email',
            'contrasenia': 'Contraseña',
            'pais': 'Pais',
        }
        
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rut',
                    'name': 'rut',
                    'type': 'text',
                    'placeholder': 'Ingrese su Rut'
                }
            ),
            'nombreComp': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre',
                    'name': 'nombre',
                    'type': 'text',
                    'placeholder': 'Nombre completo:'
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'foto',
                    'name': 'foto',
                    'type': 'file',
                    'placeholder': 'Adjuntar foto'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'name': 'email',
                    'type': 'text',
                    'placeholder': 'Email: '
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fono',
                    'name': 'fono',
                    'type': 'number',
                    'placeholder': 'Telefono: '
                }
            ),
            'contrasenia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'contra',
                    'name': 'contra',
                    'type': 'password',
                    'placeholder': 'Contraseña: '
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'name': 'direccion',
                    'type': 'text',
                    'placeholder': 'Ingrese su Direccion'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rut',
                    'name': 'rut',
                    'type': 'text',
                    'placeholder': 'Ingrese su Rut'
                }
            ),
        }