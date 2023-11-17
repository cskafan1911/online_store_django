from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    created_at = models.DateTimeField(**NULLABLE, verbose_name='Создан в ')


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='product_image', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    date_of_last_change = models.DateTimeField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"{self.name} {self.category}"

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'
