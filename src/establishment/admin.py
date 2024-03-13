from django.contrib import admin
from .models import Establishment

# Register your models here.

class EstablishmentAdmin(admin.ModelAdmin):
    list_display = (
        'establishment_name',
        'establishment_cnpj',
        'establishment_address',
    )

admin.site.register(Establishment, EstablishmentAdmin)