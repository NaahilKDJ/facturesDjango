from django.contrib import admin
from .models import Facture

# Register your models here.

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'article_name', 'article_quantity', 'ttc', 'ht', 'date', 'paid')
    search_fields = ('client', 'article_name')
    list_filter = ('paid', 'date')
