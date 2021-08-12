from rest_framework import serializers

from answers.models import Answer
from questions.serializers import QuestionSerializer


class AnswerSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Answer
        fields = ('question', 'text')
