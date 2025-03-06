from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Tasks


class TaskAdmin(MPTTModelAdmin):
    list_display = (
        'title', 'description', 'is_completed', 'due_date'
    )


admin.site.register(Tasks, TaskAdmin)