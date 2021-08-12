from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateTimeField(verbose_name='Дата старта', editable=False)
    end_date = models.DateTimeField(verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
