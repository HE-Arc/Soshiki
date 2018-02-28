from django.views import generic
from django.urls import reverse_lazy

from ..models import Card


class CardDetailView(generic.DetailView):
    model = Card


class CardCreateView(generic.CreateView):
    model = Card
    fields = ['title', 'description','deadline','file','position','list_id']
    success_url = reverse_lazy('tables-list')


class CardUpdateView(generic.UpdateView):
    model = Card
    fields = ['title', 'description', 'deadline', 'file', 'position', 'list_id']
    success_url = reverse_lazy('tables-list')


class CardDeleteView(generic.DeleteView):
    model = Card
    success_url = reverse_lazy('tables-list')