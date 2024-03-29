# Generated by Django 5.0.2 on 2024-03-13 01:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establishment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('category_name', models.CharField(max_length=45, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('order_value_total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor total do pedido')),
                ('order_date', models.DateTimeField(verbose_name='Horário do Pedido')),
                ('order_status', models.CharField(choices=[('pending', 'Pendente'), ('preparation', 'Em preparo'), ('done', 'Pronto'), ('delivered', 'Entregue'), ('canceled', 'Cancelado')], max_length=45, verbose_name='Status')),
                ('order_establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishment.establishment', verbose_name='Estabelecimento')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=45, verbose_name='Produto')),
                ('product_value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('product_description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('product_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Valor de Custo')),
                ('product_quantity', models.PositiveIntegerField(default=None, verbose_name='Quantidade')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Categoria do Produto')),
                ('product_establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishment.establishment', verbose_name='Estabelecimento')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Product_Order',
            fields=[
                ('product_order_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_order_quantity', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('product_order_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.order', verbose_name='Pedido')),
                ('product_order_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Produto do Pedido',
                'verbose_name_plural': 'Produtos dos Pedidos',
            },
        ),
    ]
