from django.urls import path
from .views import dashboard, search_view, establishment_view, administration_view, order_view

app_name = "establishment"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("resultados/", search_view, name="search_view"),
    path("<str:name>/<int:id>/", establishment_view, name="establishment_view"),
    path("<int:id>/administracao/<str:name>/", administration_view, name="administration_view"),
    path("order/", order_view, name="order"),
]
