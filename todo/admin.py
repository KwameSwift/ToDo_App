from django.contrib import admin
from .models import Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_by_username', 'created_at', 'done_on', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'category',)
    search_fields = ('created_by_username',)


admin.site.register(Task, TaskAdmin)
