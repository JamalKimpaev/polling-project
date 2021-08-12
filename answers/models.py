from django.db import models

from questions.models import Question
from users.models import CustomUser


class Answer(models.Model):
    text = models.TextField(verbose_name='Текст')
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE, related_name='Ответ')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='Пользователь')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
