from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from . import models
from .models import capteur, donnee


class capteurForm(ModelForm):
    class Meta : 
        model = models.capteur
        fields = { 'nomCapteur','Emplacement'}
        labels = {
            'nomCapteur' : _('Nom du capteur :'),
            'Emplacement': _('Emplacement de la pièce '),         
        }

class donneeForm(ModelForm):
    class Meta : 
        model = models.donnee
        fields = { 'temperature','timestamp','id_capteur'}
        labels = {
            'temperature' : _('temperature :'),
            'timestamp': _('date et heure '),   
            'id_capteur': _('capteur '),         
        }
 
