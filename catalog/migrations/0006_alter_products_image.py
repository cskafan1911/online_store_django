# Generated by Django 4.2.7 on 2023-12-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Изображение'),
        ),
    ]
