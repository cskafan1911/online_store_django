from django.db import models


class Version(models.Model):
    """
    Класс модели Version
    """

    product = models.ForeignKey('catalog.Products', on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.AutoField(primary_key=True, verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    version_status = models.BooleanField(default=False, verbose_name='Статус версии')

    def __str__(self):
        """
        Строковое представление модели Version.
        """
        return f'{self.version_number} - {self.version_name}: {self.version_status}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
