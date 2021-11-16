from django import forms
#from django.db import models
#from django.forms import fields, widgets
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'codigo_barra', 'descripcion','precio','existencia','u_medida','estado']
        labels = {'codigo_barra': "Código de barras",
                    'precio': "Precio Unitario",
                    'codigo': "Código",
                    'descripcion': "Descripción"
                    }
        widget = {'descripción': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })




#----------------------------------------------------------