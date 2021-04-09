from .models import *
from rest_framework import serializers


class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [
            'id',
            'url',
            'nom',
            'prenom',
            'email',
            'adresse',
            'role',
            'date_inscription',
            'password',
        ]

class AdministrateurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Administrateur
        fields = [
            'id',
            'url',
            'nom',
            'prenom',
            'email',
            'adresse',
            'role',
            'date_inscription',
            'password',
        ]

class Porteur_ProjetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Porteur_Projet
        fields = [
            'id',
            'url',
            'nom',
            'prenom',
            'email',
            'adresse',
            'role',
            'date_inscription',
            'password',
            'contact',
            'num_passport',
            'KBIS',
            'depot_KBIS',
        ]

class InvestisseurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investisseur
        fields = [
            'id',
            'url',
            'nom',
            'prenom',
            'email',
            'adresse',
            'role',
            'date_inscription',
            'password',
            'contact',
        ]

class TechnologieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technologie
        fields = [
            'id',
            'url',
            'nom',
            'description',
        ]

class ProjetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projet
        fields = [
            'id',
            'url',
            'nom',
            'description',
            'technologie',
            'porteur',
            'montant',
            'duree',
            'date_creation',
            'image',
            'document',
            'validation',
            'statut',
        ]

class InvestirSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investir
        fields = [
            'id',
            'url',
            'investisseur',
            'projet',
            'date',
        ]

class TacheSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tache
        fields = [
            'id',
            'url',
            'nom',
            'projet',
            'duree',
            'debut',
            'fin',
            'image',
            'statut',
            'avancement',
        ]
