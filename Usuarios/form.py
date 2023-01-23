from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Usuarios.models import Prefil_de_usuario
from django import forms

class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Usuario_actulizado(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Nombre de usuario')
    class Meta:
        model = User
        fields = ['username']

class Perfil_de_usuario(forms.ModelForm):
    class Meta:
        model = Prefil_de_usuario
        fields = ['telefono', 'fecha_de_nacimiento', 'foto_de_perfil']