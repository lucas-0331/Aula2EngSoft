from django.urls import path
from .views import dashboard, search_view

app_name = 'establishment'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path("resultados/", search_view, name="search_view"),
]