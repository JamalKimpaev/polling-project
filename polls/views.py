from django.utils import timezone
from rest_framework import generics

from polls.models import Poll
from polls.serializers import PollSerializer


class PollListView(generics.ListAPIView):
    serializer_class = PollSerializer

    def get_queryset(self):
        current_time = timezone.now()
        return Poll.objects.filter(start_date__lte=current_time, end_date__gte=current_time)


