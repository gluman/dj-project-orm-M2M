from django.db import models

class Tags(models.Model):
    topic = models.CharField(max_length=256, verbose_name='Раздел')
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.topic
class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scope = models.ManyToManyField(Tags, through='Scope')
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name='Раздел')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основная')


