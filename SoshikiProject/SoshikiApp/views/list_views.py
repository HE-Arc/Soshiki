from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ..models import List
from ..models import Table


class ListCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = List
    fields = ['name', 'position']

    def test_func(self):
        table_fk = self.kwargs["table"]
        table = Table.objects.get(id=table_fk)
        return self.request.user.id == table.creator_id

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["table"]
        return super(ListCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})


class ListUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = List
    fields = ['name', 'position']

    def test_func(self):
        self.object = self.get_object()
        table = Table.objects.get(id=self.object.table_id)
        return table.creator_id == self.request.user.id

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["table"]
        return super(ListUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})


class ListDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = List

    def test_func(self):
        self.object = self.get_object()
        table = Table.objects.get(id=self.object.table_id)
        return table.creator_id == self.request.user.id

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})
