from django.urls import path
from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleAssignDoneToNotDone,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create",),
    path("task/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update",),
    path("manufacturers/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete",),
    path(
        "tag/<int:pk>/<int:current_page>/toggle-assign/",
        ToggleAssignDoneToNotDone.as_view(),
        name="toggle-assign"
    ),

    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create",),
    path("tag/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update",),
    path("tag/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete",),
]

app_name = "todo_list"
