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

    path('dashboard/list', list_views.ListsListView.as_view(), name='lists-list'),
    path('dashboard/list/<pk>/', list_views.ListDetailView.as_view(), name='list-detail'),
    path('dashboard/list/create', list_views.ListCreateView.as_view(), name='list-create'),
    path('dashboard/list/<pk>/update', list_views.ListUpdateView.as_view(), name='list-update'),
    path('dashboard/list/<pk>/delete', list_views.ListDeleteView.as_view(), name='list-delete'),

    path('dashboard/tables', card_views.CardsListView.as_view(), name='card-list'),
    path('dashboard/card/<pk>/', card_views.CardDetailView.as_view(), name='card-detail'),
    path('dashboard/card/create', card_views.CardCreateView.as_view(), name='card-create'),
    path('dashboard/card/<pk>/update',card_views.CardUpdateView.as_view(), name='card-update'),
    path('dashboard/card/<pk>/delete', card_views.CardDeleteView.as_view(), name='card-delete'),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
