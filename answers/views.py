from rest_framework import generics

from answers.models import Answer
from answers.serializers import AnswersListSerializer, AnswersCreateSerializer


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswersCreateSerializer

    def get_serializer(self, *args, **kwargs):
        data = {**kwargs.pop('data', {}), 'user_id': self.kwargs.pop('user_id', None)}
        return super().get_serializer(*args, data=data, **kwargs)


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswersListSerializer

    def get_queryset(self):
        return Answer.objects.filter(user__id=self.kwargs['user_id'])

