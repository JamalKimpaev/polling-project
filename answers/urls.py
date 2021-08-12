from django.urls import path

from answers import views


urlpatterns = [
    path('', views.PollAnswerView.as_view())
]