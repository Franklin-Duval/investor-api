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

    def create(self, request, *args, **kwargs):
        
        try:
            serializer = Porteur_ProjetSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            """ data = serializer.data[0]
            data.pop("date_inscription") """
            
            result = {
                "success": True,
                "message": "Porteur de projet crée.",
                "data": serializer.data
            }
            return Response(result, status=status.HTTP_201_CREATED)
        except:
            result = {
                "success": False,
                "message": "Porteur de projet not created",
                "data": {}
            }
            return Response(result, status=status.HTTP_200_OK)


class InvestisseurViewSet(viewsets.ModelViewSet):
    queryset = Investisseur.objects.all()
    serializer_class = InvestisseurSerializer

    def create(self, request, *args, **kwargs):
        
        
        serializer = InvestisseurSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        """ data = serializer.data[0]
        data.pop("date_inscription") """
        
        result = {
            "success": True,
            "message": "Investisseur successfully created",
            "data": serializer.data
        }
        return Response(result, status=status.HTTP_201_CREATED)
       


class TechnologieViewSet(viewsets.ModelViewSet):
    queryset = Technologie.objects.all()
    serializer_class = TechnologieSerializer

class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer

    def create(self, request, *args, **kwargs):
        
        try:
            print(type(request.data["image"]), "\n\n")
            print(type(request.data["document"]), "\n")
            serializer = ProjetSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            """ data = serializer.data[0]
            data.pop("date_inscription") """
            
            result = {
                "success": True,
                "message": "Projet crée avec succès.",
                "data": serializer.data
            }
            return Response(result, status=status.HTTP_201_CREATED)
        except:
            result = {
                "success": False,
                "message": "Porteur de projet not created",
                "data": {}
            }
            return Response(result, status=status.HTTP_200_OK)


class InvestirViewSet(viewsets.ModelViewSet):
    queryset = Investir.objects.all()
    serializer_class = InvestirSerializer


@api_view(['POST'])
def login(request):

    if (("email" not in request.data) or ("password" not in request.data)):
        result = {
            "success": False,
            "message": "Seul les champs 'email' et 'password' sont acceptés",
            "data": {}
        }
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
    if (request.method=='POST'):
        email = request.data["email"]
        password = request.data["password"]
        
        user = None
        try:
            user = Utilisateur.objects.filter(email=email, password=password)
            print(user, "\n")
            serializer = UtilisateurSerializer(user, many=True, context={'request': request})
            print(serializer.data)
            data = serializer.data[0]
            data.pop("date_inscription")
            result = {
                "success": True,
                "message": "La connexion s'est bien passée",
                "data": data
            }
            return Response(result, status=status.HTTP_200_OK)
        except:
            result = {
                "success": False,
                "message": "Vérifiez votre email et mot de passe",
                "data": {},
            }
            return Response(result, status=status.HTTP_200_OK)     


@api_view(['POST'])
def create_project(request):
    projet = request.data

    technologie = Technologie.objects.get(id = projet["technologie"])
    porteur = Porteur_Projet.objects.get(id = projet["porteur"])
    try:
        
        project = Projet.objects.create(
            nom = projet["nom"],
            description = projet["description"],
            technologie = technologie,
            porteur = porteur,
            montant = projet["montant"],
            duree = projet["duree"],
            image = projet["image"],
            document = projet["document"],
            statut = 'En attente de validation'
        )

        serializer = ProjetSerializer(project, context={"request": request})
        
        result = {
            "success": True,
            "message": "Le projet à été crée",
            "data": serializer.data
        }

        return Response(result, status=status.HTTP_200_OK)
    except:
        result = {
            "success": False,
            "message": "La creation du projet a échoué",
            "data": {}
        }
        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def valider_project(request, id):
    """
        Permet de valider un projet
    """

    projet = Projet.objects.get(id=id)
    projet.validation = True
    projet.statut = "En attente de financement"

    projet.save()
    
    result = {
        "success": True,
        "message": "Le projet a été validé avec succès",
        "data": {}
    }

    return Response(result, status=status.HTTP_200_OK)

@api_view(['GET'])
def rejeter_project(request, id):
    """
        Permet de rejeter un projet
    """

    projet = Projet.objects.get(id=id)
    projet.validation = False
    projet.statut = "Rejété"

    projet.save()
    
    result = {
        "success": True,
        "message": "Le projet a été rejété avec succès",
        "data": {}
    }

    return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
def investir_project(request):
    """
        Permet de valider l'investissement dans un projet
    """

    post_data = request.data
    idInvestor = post_data["investisseur"]
    idProjet = post_data["projet"]

    investisseur = Investisseur.objects.get(id=idInvestor)
    projet = Projet.objects.get(id=idProjet)
    
    if not projet.validation:
        result = {
            "success": False,
            "message": "Le projet n'a pas encore été validé",
            "data": {}
        }
        return Response(result, status=status.HTTP_200_OK)
    
    projet.statut = "Financé"
    projet.save()

    investir = Investir.objects.create(
        investisseur=investisseur,
        projet=projet
    )
    
    result = {
        "success": True,
        "message": "L'opération a été éffectué avec succès",
        "data": {}
    }

    return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_project(request, id):
    """
        Permet de valider un projet
    """

    try:
        porteur = Porteur_Projet.objects.get(id=id)
        projet = Projet.objects.filter(porteur=porteur).order_by('-date_creation')

        serializer = ProjetSerializer(projet, many=True, context={'request': request})
        data = serializer.data

        technologie = Technologie.objects.all()

        for d in data:
            p = d["technologie"]
            id = p[p.find('technologie')+11: ]
            id = id.replace('/', '')

            for tech in technologie:
                if id == str(tech.id):
                    d["technologie"] = tech.nom
            
            dates = d["date_creation"]
            dates = dates[ : 19]
            dates = dates.replace('T', ' à ')
            d["date_creation"] = dates
        
        result = {
            "success": True,
            "message": "Le projet a été récupéré avec succès",
            "data": data
        }

        return Response(result, status=status.HTTP_200_OK)
    
    except:
        result = {
            "success": False,
            "message": "Une erreur s'est produite",
            "data": {}
        }

        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_admin_project(request):
    """
        Permet a l'admin d'obtenir tous les projets
    """

    try:
        projet = Projet.objects.all().order_by('-date_creation')
        porteur = Porteur_Projet.objects.all()

        serializer = ProjetSerializer(projet, many=True, context={'request': request})
        data = serializer.data

        for proj in data:
            for pro in projet:
                if proj["id"] == str(pro.id):
                    proj["technologie"] = pro.technologie.nom
                    break
            
            p = proj["porteur"]
            id = p[p.find('projet')+6: ]
            id = id.replace('/', '')
            for port in porteur:
                if id == str(port.id):
                    proj["porteur"] = port.nom + " " + port.prenom
                    break
                    
        
        result = {
            "success": True,
            "message": "Le projet a été récupéré avec succès",
            "data": data
        }

        return Response(result, status=status.HTTP_200_OK)
    
    except:
        result = {
            "success": False,
            "message": "Une erreur s'est produite",
            "data": {}
        }

        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_investor_project(request):
    """
        Permet au investisseur d'obtenir tous les projets
    """

    try:
        projet = Projet.objects.all().exclude(statut='En attente de validation').exclude(statut='Rejété').order_by('-date_creation')
        #projet = Projet.objects.all()
        porteur = Porteur_Projet.objects.all()

        serializer = ProjetSerializer(projet, many=True, context={'request': request})
        data = serializer.data

        for proj in data:
            for pro in projet:
                if proj["id"] == str(pro.id):
                    proj["technologie"] = pro.technologie.nom
                    break
            
            p = proj["porteur"]
            id = p[p.find('projet')+6: ]
            id = id.replace('/', '')
            for port in porteur:
                if id == str(port.id):
                    proj["porteur"] = port.nom + " " + port.prenom
                    break
                    
        
        result = {
            "success": True,
            "message": "Le projet a été récupéré avec succès",
            "data": data
        }

        return Response(result, status=status.HTTP_200_OK)
    
    except:
        result = {
            "success": False,
            "message": "Une erreur s'est produite",
            "data": {}
        }

        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_taches(request, id):
    """
        Permet de recuperer les tahces d'un projet
    """

    projet = Projet.objects.get(id=id)
    taches = Tache.objects.filter(projet=projet)

    serializer = TacheSerializer(taches, many=True, context={'request': request})
    data = serializer.data
    
    result = {
        "success": True,
        "message": "Les taches ont été recupéré avec succès",
        "data": data
    }

    return Response(result, status=status.HTTP_200_OK)


def root(request):
    return redirect('api/')