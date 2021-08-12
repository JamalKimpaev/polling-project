from rest_framework import generics

from answers.models import Answer
from answers.serializers import AnswersListSerializer, AnswersCreateSerializer


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswersCreateSerializer

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'user_id': self.kwargs['user_id']}
        return super().create()

    def get_serializer(self, *args, **kwargs):
        data = {**self.request.data, 'user_id': self.kwargs['user_id']}


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswersListSerializer

    def get_queryset(self):
        return Answer.objects.filter(user__id=self.kwargs['user_id'])

