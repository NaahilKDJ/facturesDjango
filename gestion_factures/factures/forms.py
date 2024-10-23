from django import forms
from factures.models import Facture

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client', 'article_name', 'article_quantity', 'ttc', 'ht', 'date']
        widgets = {
            'Date'              : forms.DateInput(attrs={'type': 'date', 'class': 'form-control input'}),
            'Client'            : forms.TextInput(attrs={'class': 'form-control input'}),
            'Article Name'      : forms.TextInput(attrs={'class': 'form-control input'}),
            'Article Quantity'  : forms.NumberInput(attrs={'class': 'form-control input'}),
            'TTC'               : forms.NumberInput(attrs={'class': 'form-control input', 'step': '0.01'}),
            'HT'                : forms.NumberInput(attrs={'class': 'form-control input', 'step': '0.01'}),
        }


    def clean_ttc(self):
        ttc = self.cleaned_data['ttc']
        if ttc < 0:
            raise forms.ValidationError("Le montant TTC ne peut pas être négatif.")
        return ttc
