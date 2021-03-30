from django.urls import path, include
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'utilisateur', views.UtilisateurViewSet)
routers.register(r'administeur', views.AdministrateurViewSet)
routers.register(r'investisseur', views.InvestisseurViewSet)
routers.register(r'porteur-porteur', views.Porteur_ProjetViewSet)
routers.register(r'projet', views.ProjetViewSet)
routers.register(r'technologie', views.TechnologieViewSet)
routers.register(r'investir', views.InvestirViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]