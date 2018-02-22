from django.urls import path, include
from .views import *

urlpatterns = [
    # Home Page and the Dashboard.
    path('', home_views.index, name='index'),
    path('dashboard', home_views.DashboardView.as_view(), name='dashboard'),

    # Routes for the CRUD of the Table model
    path('dashboard/tables', table_views.TablesListView.as_view(), name='tables-list'),
    path('dashboard/tables/<pk>/', table_views.TableDetailView.as_view(), name='table-detail'),
    path('dashboard/tables/create', table_views.TableCreateView.as_view(), name='table-create'),
    path('dashboard/tables/<pk>/update', table_views.TableUpdateView.as_view(), name='table-update'),
    path('dashboard/tables/<pk>/delete', table_views.TableDeleteView.as_view(), name='table-delete'),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
