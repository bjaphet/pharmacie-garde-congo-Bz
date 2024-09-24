from django.db import models

# Modèle pour les périodes de garde
class Periode(models.Model):
    debut = models.DateField("Début de la période")
    fin = models.DateField("Fin de la période")

    def __str__(self):
        return f"{self.debut.strftime('%d %B %Y')} au {self.fin.strftime('%d %B %Y')}"

# Modèle pour les villes
class Ville(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

# Modèle pour les quartiers
class Quartier(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, related_name="quartiers")
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

# Modèle pour les pharmacies
class Pharmacie(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, default=0)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
    localisation = models.TextField(max_length=255)

    def __str__(self):
        return self.nom
    
# Modèle pour lier les pharmacies aux périodes de garde
class GardePharmacie(models.Model):
    pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE, related_name='gardes')
    periode = models.ForeignKey(Periode, on_delete=models.CASCADE, related_name='gardes')

    def __str__(self):
        return f"{self.pharmacie.nom} - Garde du {self.periode.debut.strftime('%d %B %Y')} au {self.periode.fin.strftime('%d %B %Y')}"
