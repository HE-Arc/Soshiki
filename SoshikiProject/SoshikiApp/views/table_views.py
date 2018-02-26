from django.views import generic
from django.urls import reverse_lazy

from ..models import Table


class TablesListView(generic.ListView):
    model = Table

    def get_queryset(self):
        return Table.objects.filter(creator_id=self.request.user.id).all()


class TableDetailView(generic.DetailView):
    model = Table


class TableCreateView(generic.CreateView):
    model = Table

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        return super(TableCreateView, self).form_valid(form)

    fields = ['name', 'favorite']
    success_url = reverse_lazy('tables-list')


class TableUpdateView(generic.UpdateView):
    model = Table

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        return super(TableUpdateView, self).form_valid(form)

    fields = ['name', 'favorite']
    success_url = reverse_lazy('tables-list')


class TableDeleteView(generic.DeleteView):
    model = Table
    success_url = reverse_lazy('tables-list')