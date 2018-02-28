from django.shortcuts import render
from django.views import generic

from ..models import Table


def index(request):
    context = {}
    return render(request, 'SoshikiApp/index.html', context)


class DashboardView(generic.TemplateView):
    template_name = "SoshikiApp/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tables'] = Table.objects.filter(creator_id=self.request.user.id).all()
        context['table_favorite'] = Table.objects.filter(favorite=True, creator_id=self.request.user.id).all()
        return context