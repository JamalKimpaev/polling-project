from rest_framework import serializers

from polls.models import Poll
from questions.serializers import QuestionSerializer


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('title', 'description', 'start_date', 'end_date', 'questions')
