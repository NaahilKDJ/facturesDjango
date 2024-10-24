from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import Facture
from .forms import FactureForm
from .forms import FactureFilterForm

# Create your views here.

class FactureListView(ListView):
    model = Facture
    template_name = 'facture_list.html'
    context_object_name = 'factures'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = FactureFilterForm(self.request.GET)
        
        if form.is_valid():
            if form.cleaned_data['client']:
                queryset = queryset.filter(client__icontains=form.cleaned_data['client'])
            if form.cleaned_data['article_name']:
                queryset = queryset.filter(article_name__icontains=form.cleaned_data['article_name'])
            if form.cleaned_data['date_from']:
                queryset = queryset.filter(date__gte=form.cleaned_data['date_from'])
            if form.cleaned_data['date_to']:
                queryset = queryset.filter(date__lte=form.cleaned_data['date_to'])
            if form.cleaned_data['paid'] != '':
                queryset = queryset.filter(paid=form.cleaned_data['paid'] == 'True')
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FactureFilterForm(self.request.GET)
        return context

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
