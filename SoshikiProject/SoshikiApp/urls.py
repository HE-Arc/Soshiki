from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),

    path('dashboard/tables', views.TablesListView.as_view(), name='tables-list'),
    path('dashboard/tables/<pk>/', views.TableDetailView.as_view(), name='table-detail'),
    path('dashboard/tables/create', views.TableCreateView.as_view(), name='table-create'),
    path('dashboard/tables/<pk>/update', views.TableUpdateView.as_view(), name='table-update'),
    path('dashboard/tables/<pk>/delete', views.TableDeleteView.as_view(), name='table-delete'),
]