from django.db import models
from django.utils import timezone

class Facture(models.Model):
    # num     = models.IntegerField()
    client  = models.CharField(max_length=100)
    article_name        = models.CharField(max_length=100)
    article_quantity    = models.IntegerField()
    ttc     = models.DecimalField(max_digits=10, decimal_places=2)
    ht      = models.DecimalField(max_digits=10, decimal_places=2)
    date    = models.DateField(default=timezone.now)
    
    # You can add more fields as needed, such as:
    # numero_facture = models.CharField(max_length=20, unique=True)
    # statut = models.CharField(max_length=20, choices=[('payée', 'Payée'), ('en_attente', 'En attente'), ('annulée', 'Annulée')])

    def __str__(self):
        return f"Facture {self.id} - {self.client} - {self.montant}€"

    class Meta:
        ordering = ['-date']  # This will order invoices by date, most recent first