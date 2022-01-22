from django.forms import ModelForm, TextInput
from core.erp.models import Category


class CategoryForms(ModelForm):

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for form in self.visible_fields():
             form.field.widget.attrs['class'] = 'form-control'
             form.field.widget.attrs['autocomplete'] = 'off'
         self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name' : TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'ingresa tu nombre',
                    'autocomplete':'off'
                }
            ),
            'desc': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingresa un nombre',
                    'autocomplete': 'off',
                    'rows': 3,
                    'cols': 3
               }
            ),
        }