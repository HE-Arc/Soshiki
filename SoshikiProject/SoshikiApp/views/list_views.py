from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ..models import List
from ..models import Table
from ..forms import ListForm


class ListCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = List
    form_class = ListForm

    def test_func(self):
        table_fk = self.kwargs["table"]
        table = Table.objects.get(id=table_fk)
        return self.request.user.id == table.creator_id

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["table"]
        # Getting maximum position of existing positions
        lists = List.objects.all().filter(table_id=self.kwargs["table"])
        if lists.count() > 0:
            form.instance.position = lists.order_by("-position")[0].position + 1
        else:
            form.instance.position = 1
        return super(ListCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})


class ListUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = List
    form_class = ListForm

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
