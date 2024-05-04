from django.db import models
from django.utils import timezone
from user import models as userModels
from datetime import date
# Create your models here.
class Post(models.Model):
    PostType = [(0,"Offre"), (1,"Demande")]
    image = models.ImageField(blank=True)
    type = models.DecimalField(max_digits=1, decimal_places=0, choices=PostType, default=1)
    date = models.DateField(default=date.today())
    user = models.ForeignKey(userModels.User, on_delete=models.CASCADE, null=True)
    class Meta:
        abstract = True
    
    def __str__(self):
        return f"type: {self.type} date: {self.date}"

class Stage(Post):
    typeStage = [(1, "ouvrier"), (2, "technicien"), (3, "PFE")]
    typeStg = models.DecimalField(max_digits=1, decimal_places=0, choices=typeStage, default=1)
    societe = models.CharField(max_length=35)
    duree = models.DecimalField(max_digits=1, decimal_places=0)
    sujet = models.CharField(max_length=200) #min == ??????????
    contactInfo = models.CharField(max_length=50) #min == numéro du telephone
    specialite = models.CharField(max_length=60)
    
    def __str__(self):
        super().__str__()
        return f"typeStg: {self.typeStg} societé: {self.societe} durée: {self.duree} mois sujet: {self.sujet} contact info: {self.contactInfo} specialité: {self.specialite}"
    
class Logement(Post):
    localisation = models.CharField(max_length=50)
    description = models.CharField(max_length=250) #min == numéro du telephone
    contactInfo = models.CharField(max_length=50)
    
    def __str__(self):
        super().__str__()
        return f"localisation: {self.localisation} description: {self.description} contact info: {self.contactInfo}"
    
class Transport(Post):
    depart = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    hrDep = models.DateTimeField()
    nbSiege = models.DecimalField(max_digits=10, decimal_places=0)
    contactInfo = models.CharField(max_length=50)
    
    def __str__(self):
        super().__str__()
        return f"depart: {self.depart} destination: {self.destination} heure depart: {self.hrDep} nombre siege: {self.nbSiege} contact info: {self.contactInfo}"

class Recommendation(Post):
    texte = models.CharField(max_length=250)
    
class Evenement(Post):
    intitule = models.CharField(max_length=50)
    description = models.CharField(max_length=60)
    lieu = models.CharField(max_length=30)
    contactInfo = models.CharField(max_length=50)

    def __str__(self):
        super().__str__()
        return f"intitulé: {self.intitule} description: {self.description} lieu: {self.lieu} contact info: {self.contactInfo}"

class EvenementClub(Evenement):
    club = models.CharField(max_length=20)
    def __str__(self):
        super().__str__()
        return f"club hôte: {self.club}"
    
class EvenementSociale(Evenement):
    prix = models.FloatField()
    def __str__(self):
        super().__str__()
        return f"prix d'évènement: {self.prix}"