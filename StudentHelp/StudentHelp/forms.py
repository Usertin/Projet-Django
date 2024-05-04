from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signUpForm(UserCreationForm):
    first_name = forms.CharField(label="Prénom")
    last_name = forms.CharField(label="Nom")
    email = forms.EmailField(label="Adress e-mail")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields+('first_name','last_name','email')