from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import Facture
from .forms import FactureForm

# Create your views here.

class FactureListView(ListView):
    model = Facture
    template_name = 'facture_list.html'
    context_object_name = 'factures'

class FactureCreateView(CreateView):
    model = Facture
    form_class = FactureForm
    template_name = 'facture_form.html'
    success_url = reverse_lazy('facture-list')
class FactureDetailView(DetailView):
    model = Facture
    template_name = 'facture_detail.html'
    context_object_name = 'facture'

class FactureUpdateView(UpdateView):
    model = Facture
    form_class = FactureForm
    template_name = 'facture_form.html'
    success_url = reverse_lazy('facture-list')

class FactureDeleteView(DeleteView):
    model = Facture
    template_name = 'facture_confirm_delete.html'
    success_url = reverse_lazy('facture-list')

class HomeView(TemplateView):
    template_name = 'home.html'
