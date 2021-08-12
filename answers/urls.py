from django.urls import path

from answers import views


urlpatterns = [
    path('create/<int:user_id>', views.AnswerCreateView.as_view()),
    path('<int:user_id>', views.AnswerListView.as_view())
]
