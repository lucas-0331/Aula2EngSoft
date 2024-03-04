from django.urls import path
from core.views import index
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('', index),
    path('consumer/', TemplateView.as_view(template_name='consumer/index.html'), name='consumer_page'),
    path('kitchen/', TemplateView.as_view(template_name='kitchen/index.html'), name='kitchen_page'),
]