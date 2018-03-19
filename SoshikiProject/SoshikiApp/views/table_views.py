from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ..models import Table
from ..forms import TableForm


class TablesListView(LoginRequiredMixin, generic.ListView):
    model = Table

    def get_queryset(self):
        return Table.objects.filter(creator_id=self.request.user.id).all()


class TableDetailView(LoginRequiredMixin, generic.DetailView):
    model = Table

    def get_queryset(self):
        return Table.objects.filter(creator_id=self.request.user.id)


class TableCreateView(LoginRequiredMixin, generic.CreateView):
    model = Table
    form_class = TableForm
    success_url = reverse_lazy('tables-list')

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        return super(TableCreateView, self).form_valid(form)


class TableUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Table
    form_class = TableForm
    success_url = reverse_lazy('tables-list')

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        return super(TableUpdateView, self).form_valid(form)


class TableDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Table
    success_url = reverse_lazy('tables-list')

    def test_func(self):
        self.object = self.get_object()
        return self.object.creator_id == self.request.user.id
