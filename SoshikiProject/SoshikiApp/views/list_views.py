from django.views import generic
from django.urls import reverse_lazy

from ..models import List


class ListsListView(generic.ListView):
    model = List

    def get_queryset(self):
        return List.objects.all()


class ListDetailView(generic.DetailView):
    model = List


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