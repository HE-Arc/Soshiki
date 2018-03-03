from django.views import generic
from django.urls import reverse_lazy

from ..models import List


class ListCreateView(generic.CreateView):
    model = List

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["pk"]
        return super(ListCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["pk"]})

    fields = ['name', 'position']


class ListUpdateView(generic.UpdateView):
    model = List

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["pk"]
        return super(ListUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["pk"]})

    fields = ['name', 'position']


class ListDeleteView(generic.DeleteView):
    model = List

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["pk"]})
