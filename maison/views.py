import os

from django.http import FileResponse, HttpResponse
from django.shortcuts import render, HttpResponseRedirect,get_object_or_404,redirect
from .models import *
from .forms import *
import csv

def main(resquest):




def purge(request):
    Donnee = donnee.objects.all().delete()
    return HttpResponseRedirect("/maison/")

def updatetraitement(request, id):
    form = capteurForm(request.POST)
    update = form.save(commit = False)
    update.id = id 
    update.save()
    return HttpResponseRedirect("/maison/")


def affichage_spe(request):
    donnee_capteur = donnee.objects.all()
    return render(request,"affichage_spe.html",{"donnee":donnee_capteur})

def capteur_data(request, id):
    donnee_capteur = donnee.objects.filter(id_capteur_id=id)
    return render(request, "capteur_data.html", {"donnee": donnee_capteur})




def export_csv(request):
    Donnee = donnee.objects.all()

    data = [["id", "temperature", "timestamp", "id_capteur"]]

    for d in Donnee:
        d_list = [d.id, d.temperature, d.timestamp, d.id_capteur_id]
        data.append(d_list)

    # Ouvrir un nouveau fichier CSV en mode écriture
    with open('export.csv', 'w', newline='') as csvfile:
        # Créer un écrivain CSV à partir du fichier ouvert
        writer = csv.writer(csvfile)
        # Écrire la ligne d'en-tête dans le fichier CSV
        writer.writerow(data[0])
        # Parcourir toutes les données
        for row in data[1:]:
            # Écrire chaque ligne de données dans le fichier CSV
            writer.writerow(row)

        with open('export.csv', 'r') as file:
            file_content = file.read()

        # Créer une réponse avec le contenu du fichier CSV
        response = HttpResponse(file_content, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        return response