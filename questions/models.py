from django.db import models

from polls.models import Poll


class Question(models.Model):
    QUESTION_TYPES = [
        (1, 'ответ текстом'),
        (2, 'ответ с выбором одного варианта'),
        (3, 'ответ с выбором нескольких вариантов'),
    ]

    text = models.TextField(verbose_name='Текст')
    type = models.IntegerField(choices=QUESTION_TYPES, verbose_name='Тип ответа')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions', verbose_name='Опрос')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
