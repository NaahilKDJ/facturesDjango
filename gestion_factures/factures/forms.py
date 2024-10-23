from django import forms
from factures.models import Facture

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client', 'article_name', 'article_quantity', 'ttc', 'ht', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'article_name': forms.TextInput(attrs={'class': 'form-control'}),
            'article_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'ttc': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


    def clean_ttc(self):
        ttc = self.cleaned_data['ttc']
        if ttc < 0:
            raise forms.ValidationError("Le montant TTC ne peut pas être négatif.")
        return ttc
