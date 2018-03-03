from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import List
from ..models import Table


class ListCreateView(LoginRequiredMixin, generic.CreateView):
    model = List
    fields = ['name', 'position']

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["list"]
        return super(ListCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["list"]})


class ListUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = List
    fields = ['name', 'position']

    def form_valid(self, form):
        form.instance.table_id = self.kwargs["list"]
        return super(ListUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["list"]})


class ListDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = List

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        # TODO: Moyen de faire plus propre ?
        table = Table.objects.get(id=self.object.table_id)
        if table.creator_id == request.user.id:
            return super(ListDeleteView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('tables-list')

    def get_success_url(self):
        return reverse_lazy('table-detail', kwargs={'pk': self.kwargs["list"]})
