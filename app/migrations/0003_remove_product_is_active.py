# Generated by Django 5.1.6 on 2025-03-28 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_stock_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_active',
        ),
    ]
