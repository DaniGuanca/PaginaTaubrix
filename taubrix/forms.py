from django import forms

class FormContacto(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField()
    asunto = forms.CharField()
    email = forms.EmailField(required=True)
    contenido = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
