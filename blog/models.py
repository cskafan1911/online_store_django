from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    """
    Класс модели Blog.
    """

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, unique=True, verbose_name='Slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='preview_image', **NULLABLE, verbose_name='Превью')
    date_of_creation = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='Дата создания')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')

    def __str__(self):
        """
        Строковое представление модели Blog.
        """
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        permissions = (
            ('blog_custom_perm', 'модератор блога'),
                       )
