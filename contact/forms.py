
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'escribe tu nombre por favor'
        }
    ), min_length=2, max_length=100)

    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder':'escribe tu email por favor'
        }
    ), min_length=2, max_length=100)

    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder':'escribe el texto por favor',
            'row':5,
          
         
        }
    ), min_length=2, max_length=100)