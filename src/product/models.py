from django.db import models
from ..establishment.models import Establishment


class Category(models.Model):
    category_id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    category_name = models.CharField(
        max_length=45,
        verbose_name="Categoria",
    )
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return f"{self.category_name}"



class Product(models.Model):
    product_id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    product_name = models.CharField(
        max_length=45,
        verbose_name="Produto",
    )
    product_value = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Valor",
    )
    product_description = models.CharField(
        max_length=255,
        verbose_name="Descrição",
    )
    product_cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor de Custo",
    )
    product_quantity = models.PositiveIntegerField(
        default=None,
        verbose_name="Quantidade",
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Categoria do Produto",
    )
    product_establishment = models.ForeignKey(
        Establishment,
        on_delete=models.CASCADE,
        verbose_name="Estabelecimento",
    )
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
    def __str__(self):
        return f"{self.product_name}"