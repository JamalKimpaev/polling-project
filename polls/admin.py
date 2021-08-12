from django.contrib import admin
from polls.models import Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return ['start_date',] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return []
