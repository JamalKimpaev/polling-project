from django.db import models

from ..questions.models import Question


class Answer(models.Model):
    text = models.TextField(verbose_name='Текст')
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE, related_name='Ответ')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
