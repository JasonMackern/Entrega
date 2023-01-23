from django import forms

class Empanada_Form (forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    stock = forms.BooleanField(required=False)