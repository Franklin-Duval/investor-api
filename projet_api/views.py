from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializer import *

# Create your views here.

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class AdministrateurViewSet(viewsets.ModelViewSet):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer

class Porteur_ProjetViewSet(viewsets.ModelViewSet):
    queryset = Porteur_Projet.objects.all()
    serializer_class = Porteur_ProjetSerializer

class InvestisseurViewSet(viewsets.ModelViewSet):
    queryset = Investisseur.objects.all()
    serializer_class = InvestisseurSerializer

class TechnologieViewSet(viewsets.ModelViewSet):
    queryset = Technologie.objects.all()
    serializer_class = TechnologieSerializer

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer

class InvestirViewSet(viewsets.ModelViewSet):
    queryset = Investir.objects.all()
    serializer_class = InvestirSerializer

def root(request):
    return redirect('api/')