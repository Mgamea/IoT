"""
URL configuration for PHD207 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'administration Django

    # URL pour afficher la liste des sauvegardes
    #path('sauvegardes/', lister_sauvegardes, name='lister_sauvegardes'),

    # URL pour inclure les URLs de notre application
    path('notre-application/', include('sauvegarde.urls')),
    
    # D'autres patterns d'URL peuvent être ajoutés ici
]
