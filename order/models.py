from django.db import models


class Order(models.Model):
    """
    Класс модели Order.
    """

    product = models.ForeignKey('catalog.Products', on_delete=models.CASCADE, verbose_name='Товар')

    name = models.CharField(max_length=150, verbose_name='Имя покупателя')
    email = models.EmailField(max_length=150, verbose_name='Почта')
    message = models.TextField(verbose_name='Сообщение')

    closed = models.BooleanField(default=False, verbose_name='Заказ закрыт')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания запроса')

    def __str__(self):
        """
        Строковое представление модели Order.
        """
        return f'{self.product} от ({self.email})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
