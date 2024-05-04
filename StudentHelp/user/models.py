from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    telephone = models.DecimalField(max_digits=8, decimal_places=0)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return f"nom: {self.nom} prenom: {self.prenom} telephone: {str(self.telephone)} email: {self.email} password: {self.password}"