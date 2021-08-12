from rest_framework.response import Response
from rest_framework import generics
from django.utils import timezone

from .models import Poll
from .serializers import PollSerializer


class PollView(generics.ListAPIView):
    serializer_class = PollSerializer

    def get_queryset(self):
        current_time = timezone.now()
        return Poll.objects.filter(start_date__lte=current_time, end_time__gte=current_time)

