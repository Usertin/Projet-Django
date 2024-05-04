from django.forms import ModelForm
from django import forms
from .models import *
class PostForm(forms.ModelForm):
    #*args : tuple pour les parametres dont on recupere par index. example : args[0]
    #**kwargs: dictionnaire pour les parametres dont on recupaere par cle. example : kwargs['user']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
        if user:
            user_choice = (user.id, str(user))
            self.fields['user'].initial = user_choice
        
    class Meta:
        model = Post
        fields = ['image','type','date','user']
        
class PostStageForm(PostForm):
    class Meta:
        model = Stage
        fields = ['typeStg','societe','duree','sujet','contactInfo','specialite']