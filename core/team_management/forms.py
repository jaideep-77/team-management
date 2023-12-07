from django import forms
from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        role_choices = [(True, 'Admin'),(False, 'Regular')]
        widgets = {
            'is_admin' : forms.RadioSelect(choices=role_choices)
            }
        

       
