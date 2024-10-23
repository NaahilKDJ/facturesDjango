from django.urls import path
from .views import FactureListView, FactureCreateView, FactureUpdateView, FactureDeleteView, FactureDetailView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('factures/', FactureListView.as_view(), name='facture-list'),
    path('create/', FactureCreateView.as_view(), name='facture-create'),
    path('update/<int:pk>/', FactureUpdateView.as_view(), name='facture-update'),
    path('delete/<int:pk>/', FactureDeleteView.as_view(), name='facture-delete'),
    path('factures/<int:pk>/', FactureDetailView.as_view(), name='facture-detail'),
]
