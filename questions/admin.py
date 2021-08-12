from django.contrib import admin
from questions.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    # readonly_fields = ('pub_date',)
