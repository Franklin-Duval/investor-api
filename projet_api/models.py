from django.db import models
import uuid

# Create your models here.
class Utilisateur(models.Model):
    ROLE = (
        ('Admin', 'Admin'),
        ('Investisseur', 'Investisseur'),
        ('Porteur Projet', 'Porteur Projet'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    adresse = models.CharField(max_length=100, null=False)
    role = models.CharField(choices=ROLE, max_length=15, null=False)
    date_inscription = models.DateTimeField(auto_now_add=True, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nom + " : " + self.role

class Administrateur(Utilisateur):
    pass

class Porteur_Projet(Utilisateur):
    contact = models.CharField(max_length=20, null=False)
    num_passport = models.IntegerField(null=False)
    KBIS = models.CharField(max_length=100, unique=True, null=False)
    depot_KBIS = models.FileField(null=False, upload_to='KBIS/')


class Investisseur(Utilisateur):
    contact = models.CharField(max_length=20, null=False)

class Technologie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100, null=False)
    description = models.TextField()


class Projet(models.Model):
    STATUT = (
        ('En attente de financement', 'En attente de financement'),
        ('Financé', 'Financé'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100, null=False)
    description = models.TextField()
    technologie = models.ForeignKey(Technologie, null=False, on_delete=models.PROTECT)
    porteur = models.ForeignKey(Porteur_Projet, null=True, on_delete=models.CASCADE)
    montant = models.IntegerField(default=0, null=False)
    duree = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="default.jpg", upload_to="images/")
    document = models.FileField(null=False, upload_to='document/')
    validation = models.BooleanField(default=False)
    supprime = models.BooleanField(default=False)
    statut = models.CharField(max_length=30, choices=STATUT)

    def __str__(self):
        return self.nom

class Investir(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    investisseur = models.ForeignKey(Investisseur, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)