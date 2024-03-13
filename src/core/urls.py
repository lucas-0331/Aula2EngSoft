from django.urls import path
from django.views.generic import TemplateView
from .views import login_view, register_view, index

app_name = 'src.core'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('consumer/', TemplateView.as_view(template_name='consumer/index.html'), name='consumer_page'),
    path('kitchen/', TemplateView.as_view(template_name='kitchen/index.html'), name='kitchen_page'),
    path("login/", login_view, name="login_view"),
    path("cadastro/", register_view, name="register_view"),
]