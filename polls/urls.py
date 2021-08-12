from django.urls import path

from . import views


urlpatterns = [
    path('polls/', views.PollView.as_view())
]
