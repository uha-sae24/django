import os
import matplotlib.pyplot as plt
from django.http import FileResponse, HttpResponse
from django.utils import timezone
from io import BytesIO
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect,get_object_or_404,redirect
from .models import *
from .forms import *
import csv



def index(request):
    sensors = capteur.objects.all()  # Assuming Capteur is your Sensor model
    latest_temperatures = {sensor: donnee.objects.filter(id_capteur=sensor).last().temperature for sensor in sensors}
    return render(request, 'index.html', {'latest_temperatures': latest_temperatures})

def sensor_data(request, sensor_id):
    sensor = get_object_or_404(capteur, id=sensor_id)
    start = request.GET.get('start')
    end = request.GET.get('end')
    if start and end:
        start = timezone.make_aware(datetime.strptime(start, "%Y-%m-%dT%H:%M"))
        end = timezone.make_aware(datetime.strptime(end, "%Y-%m-%dT%H:%M"))
        data = donnee.objects.filter(id_capteur=sensor, timestamp__range=(start, end))
    else:
        data = donnee.objects.filter(id_capteur=sensor)

    plt.figure()
    plt.plot([d.timestamp for d in data], [d.temperature for d in data])
    plt.title('Temperature over time')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature')

    # Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return render(request, 'sensor_data.html', {'data': data, 'sensor': sensor, 'plot': buf.getvalue()})

def purge(request):
    Donnee = donnee.objects.all().delete()
    sensors = capteur.objects.all().delete()
    return HttpResponseRedirect("/")

def all_data(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    if start and end:
        start = timezone.make_aware(datetime.strptime(start, "%Y-%m-%dT%H:%M"))
        end = timezone.make_aware(datetime.strptime(end, "%Y-%m-%dT%H:%M"))
        all_data = donnee.objects.filter(timestamp__range=(start, end)).order_by('timestamp')
    else:
        all_data = donnee.objects.all().order_by('timestamp')
    return render(request, 'all_data.html', {'all_data': all_data})

def edit_sensor(request, sensor_id):
    sensor = get_object_or_404(capteur, id=sensor_id)
    if request.method == "POST":
        form = capteurForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return redirect('sensor_data', sensor_id=sensor.id)
    else:
        form = capteurForm(instance=sensor)
    return render(request, 'edit_sensor.html', {'form': form, 'sensor': sensor})



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

        file = open('export.csv', 'rb')

        #return HttpResponseRedirect("/")
        # Créer une réponse avec le contenu du fichier CSV
        return FileResponse(file, as_attachment=True, filename='export.csv')

        #return response