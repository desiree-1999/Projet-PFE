from django.db import models

class Capteur(models.Model):
    type = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    etat = models.BooleanField(default=True)

    def activerCapteur(self):
        self.etat = True
        self.save()

    def desactiverCapteur(self):
        self.etat = False
        self.save()

    def signalerCapteur(self):
        pass


class Incendie(models.Model):
    gravite = models.IntegerField()
    dateDebut = models.DateTimeField()
    description = models.TextField()

    def creerSignalement(self):
        pass

    def bloquerSignalement(self):
        pass


class Zone(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    localisation = models.CharField(max_length=255)

    def __str__(self):
        return self.nom