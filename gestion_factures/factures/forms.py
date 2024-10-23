from django import forms
from factures.models import Facture

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client', 'article_name', 'article_quantity', 'ttc', 'ht', 'date', 'paid']
        widgets = {
            'Date'              : forms.DateInput(attrs={'type': 'date', 'class': 'form-control input'}),
            'Client'            : forms.TextInput(attrs={'class': 'form-control input'}),
            'Article Name'      : forms.TextInput(attrs={'class': 'form-control input'}),
            'Article Quantity'  : forms.NumberInput(attrs={'class': 'form-control input'}),
            'TTC'               : forms.NumberInput(attrs={'class': 'form-control input', 'step': '0.01'}),
            'HT'                : forms.NumberInput(attrs={'class': 'form-control input', 'step': '0.01'}),
            'Payment status'    : forms.BooleanField()
        }


    def clean_ttc(self):
        ttc = self.cleaned_data['ttc']
        
        if ttc < 0 or ttc==None or ttc=="":
            raise forms.ValidationError("Le montant TTC ne peut pas être négatif ou vide !")
        
        return ttc
    
    
    def clean_Client(self):
        client = self.cleaned_data['client']
        
        if client=="" or client==None:
            raise forms.ValidationError("Veuillez mentionner le nom du client !")
        
        return client
    
