from django.contrib import admin 
from .models import EvenementClub, EvenementSociale, Recommendation, Stage, Transport, Logement
# Register your models here.
admin.site.register(EvenementClub)
admin.site.register(EvenementSociale)
admin.site.register(Recommendation)
admin.site.register(Stage)
admin.site.register(Transport)
admin.site.register(Logement)