from django.db import transaction
from rest_framework import serializers

from answers.models import Answer
from questions.serializers import QuestionSerializer
from users.models import CustomUser


class AnswersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'text')


class AnswersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('text', 'user', 'question')

    @transaction.atomic()
    def create(self, validated_data):
        user = CustomUser.objects.get_or_create(id=validated_data['user'].id)
        print(user)
        validated_data['user'] = user[0]
        return super().create(validated_data)
