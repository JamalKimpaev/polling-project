from rest_framework import serializers

from .models import Poll
from ..questions.serializers import QuestionSerializer


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        field = ('title', 'description', 'start_date', 'end_date', 'questions')
