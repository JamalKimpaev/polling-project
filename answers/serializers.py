from rest_framework import serializers
from django.db import transaction

from answers.models import Answer
from users.models import CustomUser
from questions.serializers import QuestionSerializer


class AnswersListSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Answer
        fields = ('question', 'text')


class AnswersCreateSerializer(serializers.Serializer):

    class Meta:
        model = Answer
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):
        user = CustomUser.objects.get_or_create()
        validated_data['user'] = user
        return super().create(validated_data)
