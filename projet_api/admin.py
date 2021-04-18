from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Administrateur)
admin.site.register(Tache)
admin.site.register(Porteur_Projet)
admin.site.register(Investisseur)
admin.site.register(Investir)
admin.site.register(Projet)
admin.site.register(Technologie)
