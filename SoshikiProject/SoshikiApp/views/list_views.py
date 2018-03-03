from django.views import generic
from django.urls import reverse_lazy

from ..models import List


class ListCreateView(generic.CreateView):
    model = List
    fields = ['name', 'position']

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["list"]
        return super(ListCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["list"]})


class ListUpdateView(generic.UpdateView):
    model = List
    fields = ['name', 'position']

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["list"]
        return super(ListUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["list"]})


class ListDeleteView(generic.DeleteView):
    model = List

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["list"]})
