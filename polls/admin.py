from django.contrib import admin
from .models import Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    readonly_fields = ('start_date',)

