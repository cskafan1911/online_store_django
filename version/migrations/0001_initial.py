# Generated by Django 4.2.7 on 2023-12-23 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0006_alter_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('version_number', models.AutoField(primary_key=True, serialize=False, verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=150, verbose_name='Название версии')),
                ('version_status', models.BooleanField(default=False, verbose_name='Статус версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]