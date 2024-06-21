from django.db import models

class capteur(models.Model):
   id = models.CharField(max_length=100,primary_key=True)
   nomCapteur = models.CharField(max_length=100)
   Emplacement = models.CharField(max_length=100)

   def dico(self):
      return{"nomCapteur":self.nomCapteur,"Emplacement":self.Emplacement}

   def __str__(self):
      return self.nomCapteur+" ("+self.id+")"
   
class donnee(models.Model):
   temperature = models.IntegerField(blank=False)
   timestamp = models.DateTimeField(blank=False)
   id_capteur = models.ForeignKey( capteur, on_delete=models.CASCADE)

