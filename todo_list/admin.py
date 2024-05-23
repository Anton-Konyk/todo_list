from django.contrib import admin

from todo_list.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content", "created_at", "deadline", "tags")
    list_filter = ("content", "created_at", "deadline", "is_done", "tags",)
