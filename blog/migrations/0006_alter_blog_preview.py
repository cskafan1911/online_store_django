# Generated by Django 4.2.7 on 2023-12-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='preview_image', verbose_name='Превью'),
        ),
    ]
