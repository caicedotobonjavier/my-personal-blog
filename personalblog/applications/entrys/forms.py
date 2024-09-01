from django import forms
#
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = (
            'category',
            'title',
            'resumen',
            'content',
            'imagen',
            'active',
            'in_home',
            'portada',
            'user',
        )

        widgets = {
            'title':forms.TextInput(
                {
                    'placeholder' : 'Titulo de la entrada'
                }
            ),

            'resumen':forms.TextInput(
                {
                    'placeholder' : 'Resumen de la entrada'
                }
            ),

            'content':forms.Textarea(
                {
                    'placeholder' : 'Contenido de la entrada',
                }
            )
        }