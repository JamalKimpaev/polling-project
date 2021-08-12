from rest_framework.response import Response
from rest_framework import generics
from django.utils import timezone

from polls.models import Poll
from polls.serializers import PollSerializer
from drf_yasg.utils import swagger_auto_schema


class PollView(generics.ListAPIView):
    serializer_class = PollSerializer


    # @swagger_auto_schema(method='get', responses={200: PollSerializer})
    def get_queryset(self):
        current_time = timezone.now()
        return Poll.objects.filter(start_date__lte=current_time, end_date__gte=current_time)

