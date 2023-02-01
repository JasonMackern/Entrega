from django import forms

class Gaseosa_Form (forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    stock = forms.BooleanField(required=False)
    imagen = forms.ImageField(required=False)