from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ..models import List
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


def reorder_lists(request):
    is_validated = True

    if request.is_ajax():
        ids = request.POST.getlist("arrayIDs[]")

        if check_ids_in_db(request.user.id, ids):
            position = 1

            for id in ids:
                List.objects.filter(id=id).update(position=position)
                position += 1
        else:
            is_validated = False
    else:
        is_validated = False

    # Renvoie une réponse Ajax
    if is_validated:
        return HttpResponse("OK")
    else:
        return HttpResponse("Error", status=401)


def check_ids_in_db(user_id, ids):
    is_ok = True
    table_ids = List.objects.filter(id__in=ids).values_list('table_id', flat=True)
    creator_ids = Table.objects.filter(id__in=table_ids).values_list('creator_id', flat=True)

    for id in creator_ids:
        if id is not user_id:
            is_ok = False

    return is_ok
