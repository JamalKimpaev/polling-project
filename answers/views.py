from rest_framework import generics

from answers.models import Answer
from answers.serializers import AnswerSerializer


class PollAnswerView(generics.CreateAPIView):
    pass
