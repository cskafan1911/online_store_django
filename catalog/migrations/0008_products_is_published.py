# Generated by Django 4.2.7 on 2024-01-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_products_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
    ]
