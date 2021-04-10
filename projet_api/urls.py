from django.urls import path, include
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'utilisateur', views.UtilisateurViewSet)
routers.register(r'administeur', views.AdministrateurViewSet)
routers.register(r'investisseur', views.InvestisseurViewSet)
routers.register(r'porteur-projet', views.Porteur_ProjetViewSet)
routers.register(r'projet', views.ProjetViewSet)
routers.register(r'technologie', views.TechnologieViewSet)
routers.register(r'investir', views.InvestirViewSet)
routers.register(r'tache', views.TacheViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('login/', views.login),
    path('create-project/', views.create_project),
    path('all-admin-project/', views.all_admin_project),
    path('all-investor-project/', views.all_investor_project),
    path('validate-project/<str:id>/', views.valider_project),
    path('rejeter-project/<str:id>/', views.rejeter_project),
    path('investir-project/', views.investir_project),
    path('get-project/<str:id>/', views.get_project),
    path('get-taches/<str:id>/', views.get_taches),
    path('update-tache/', views.update_tache),
]