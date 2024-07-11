from django import forms
from django.contrib.auth.models import User




class CreateUserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
       # exclude = ['id']

