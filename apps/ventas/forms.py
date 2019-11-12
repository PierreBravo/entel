from django import forms

from apps.ventas.models import Producto

class ProductoForm(forms.ModelForm):
  
    class Meta:
         model = Producto
       
         fields = [ 
         'nombre',
         'cantidad',
         'fecha_venta',
         'hora_venta',
         'comentario',
         'vendedor',
         'venta',
        ]
         labels = {
         'nombre':'Nombre de producto',
         'cantidad':'cantidad',
         'fecha_venta': 'Fecha de venta',
         'hora_venta': 'Hora de venta',
         'comentario': 'Comentario',
         'vendedor': 'Vendedor',
         'venta': 'Ventas',
        }
         widgets = {
         'nombre' : forms.TextInput(attrs={'class':'form-control'}),
         'cantidad' : forms.TextInput(attrs={'class':'form-control'}),
         'fecha_venta': forms.TextInput(attrs={'class':'form-control'}),
         'hora_venta': forms.TextInput(attrs={'class':'form-control'}),
         'comentario':forms.Textarea(attrs={'class':'form-control'}),
         'vendedor': forms.Select(attrs={'class':'form-control'}),
         'venta':forms.CheckboxSelectMultiple(),
        }