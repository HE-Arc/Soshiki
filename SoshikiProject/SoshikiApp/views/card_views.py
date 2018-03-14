from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ..models import Card
from ..models import Table
from ..models import List
from ..forms import CardForm


class CardDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Card

    # TODO: Pas DRY mais en attendant ça marche
    def test_func(self):
        self.object = self.get_object()
        l = List.objects.get(id=self.object.list_id)
        table = Table.objects.get(id=l.table_id)
        return table.creator_id == self.request.user.id


class CardCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Card
    form_class = CardForm

    def test_func(self):
        table_fk = self.kwargs["table"]
        table = Table.objects.get(id=table_fk)
        return self.request.user.id == table.creator_id

    def form_valid(self, form):
        form.instance.list_id = self.kwargs["list"]
        return super(CardCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})


class CardUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Card
    form_class = CardForm

    def test_func(self):
        self.object = self.get_object()
        l = List.objects.get(id=self.object.list_id)
        table = Table.objects.get(id=l.table_id)
        return table.creator_id == self.request.user.id

    def form_valid(self, form):
        form.instance.list_id = self.kwargs["list"]
        return super(CardUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})


class CardDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Card

    def test_func(self):
        self.object = self.get_object()
        l = List.objects.get(id=self.object.list_id)
        table = Table.objects.get(id=l.table_id)
        return table.creator_id == self.request.user.id

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})
