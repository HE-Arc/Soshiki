from django.views import generic
from django.urls import reverse_lazy

from ..models import Card
from ..forms import CardForm


class CardDetailView(generic.DetailView):
    model = Card


class CardCreateView(generic.CreateView):
    model = Card
    form_class = CardForm

    def form_valid(self, form):
        form.instance.list_id = self.kwargs["list"]
        return super(CardCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})


class CardUpdateView(generic.UpdateView):
    model = Card
    fields = ['title', 'description', 'deadline', 'file', 'position']

    def form_valid(self, form):
        form.instance.list_id = self.kwargs["list"]
        return super(CardUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})


class CardDeleteView(generic.DeleteView):
    model = Card

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["table"]})
