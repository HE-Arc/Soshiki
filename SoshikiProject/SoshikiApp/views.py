from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy

from .models import Table

def index(request):
	context = {}

	return render(request, 'SoshikiApp/index.html', context)

class DashboardView(generic.TemplateView):
	template_name = "SoshikiApp/dashboard.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tables'] = Table.objects.all()
		context['table_private'] = Table.objects.filter(private=True).all()
		context['table_favorite'] = Table.objects.filter(favorite=True).all()
		return context

class TablesListView(generic.ListView):
    model = Table

    def get_queryset(self):
        return Table.objects.all()

class TableDetailView(generic.DetailView):
    model = Table

class TableCreateView(generic.CreateView):
    model = Table
    fields = ['name', 'favorite', 'private']
    success_url = reverse_lazy('dashboard-tables')

class TableUpdateView(generic.UpdateView):
	model = Table
	fields = ['name', 'favorite', 'private']
	success_url = reverse_lazy('dashboard-tables')

class TableDeleteView(generic.DeleteView):
	model = Table
	success_url = reverse_lazy('dashboard-tables')