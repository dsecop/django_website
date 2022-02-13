
from django.contrib import admin
from employers.models import Task, Tag


class CustomUserTask(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('id', 'name', 'author', 'created_at', 'updated_at', 'valid_until', 'is_published')
    list_display_links = ('name',)
    list_editable = ('is_published',)
    search_fields = ('name',)

admin.site.register(Task, CustomUserTask)
admin.site.register(Tag)
