# Generated by Django 2.0.1 on 2018-03-29 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categories',
        ),
    ]
