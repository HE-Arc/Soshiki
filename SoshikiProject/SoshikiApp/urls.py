from django.urls import path, include

from .views import *

urlpatterns = [
    # Home Page and the Dashboard.
    path('', home_views.index, name='index'),
    path('dashboard', home_views.DashboardView.as_view(), name='dashboard'),

    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', user_views.signup_view, name='signup'),
    path('accounts/<slug>/', user_views.UserDetailView.as_view(), name='profile-detail'),
    path('accounts/<slug>/update', user_views.UserUpdateView.as_view(), name='profile-update'),

    # Routes for the CRUD of the Table model
    path('tables', table_views.TablesListView.as_view(), name='tables-list'),
    path('tables/<pk>/', table_views.TableDetailView.as_view(), name='table-detail'),
    path('tables/create', table_views.TableCreateView.as_view(), name='table-create'),
    path('tables/<pk>/update', table_views.TableUpdateView.as_view(), name='table-update'),
    path('tables/<pk>/delete', table_views.TableDeleteView.as_view(), name='table-delete'),

    path('tables/<table>/list/create', list_views.ListCreateView.as_view(), name='list-create'),
    path('tables/<table>/list/<pk>/update', list_views.ListUpdateView.as_view(), name='list-update'),
    path('tables/<table>/list/<pk>/delete', list_views.ListDeleteView.as_view(), name='list-delete'),

    path('tables/<table>/list/<list>/card/<pk>/', card_views.CardDetailView.as_view(), name='card-detail'),
    path('tables/<table>/list/<list>/card/create', card_views.CardCreateView.as_view(), name='card-create'),
    path('tables/<table>/list/<list>/card/<pk>/update', card_views.CardUpdateView.as_view(), name='card-update'),
    path('tables/<table>/list/<list>/card/<pk>/delete', card_views.CardDeleteView.as_view(), name='card-delete'),
]
