from django.views import generic
from django.urls import reverse_lazy

from ..models import List

class ListCreateView(generic.CreateView):
    model = List
    fields = ['name', 'position','table_id']
    success_url = reverse_lazy('tables-list')


class ListUpdateView(generic.UpdateView):
    model = List
    fields = ['name', 'position','table_id']
    success_url = reverse_lazy('tables-list')


class ListDeleteView(generic.DeleteView):
    model = List
    success_url = reverse_lazy('tables-list')