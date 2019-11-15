from django import forms
from apps.vendedor.models import Vendedor

class VendedorForm(forms.ModelForm):

	class Meta:
		 model = Vendedor
		 fields = [
		 'nombre',
		 'apellidos',
         'email',		
		]
		 labels = {
		 'nombre': 'Nombre:',
		 'apellidos': 'Apellidos:',
         'email': 'Correo electrónico:',
        }
		 widgets = {
		 'nombre':forms.TextInput(attrs={'class':'form-control'}),
		 'apellidos':forms.TextInput(attrs={'class':'form-control'}),
         'email':forms.TextInput(attrs={'class':'form-control'}),
		}
