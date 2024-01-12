from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Продукт')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='product_image', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    date_of_last_change = models.DateTimeField(**NULLABLE, verbose_name='Дата последнего изменения')

    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='Создатель')

    def __str__(self):
        return f"{self.name} {self.category}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
