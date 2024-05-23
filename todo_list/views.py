from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.views import generic, View

from todo_list.forms import TaskForm, ToggleAssignDoneToNotDoneForm, TagForm
from todo_list.models import Task, Tag


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_list/task_list.html"
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class ToggleAssignDoneToNotDone(LoginRequiredMixin, View):
    def post(self, request, pk, current_page):
        form = ToggleAssignDoneToNotDoneForm(request.POST)

        if form.is_valid():
            task = Task.objects.get(id=pk)
            if task.is_done:
                task.is_done = False
            else:
                task.is_done = True
            task.save()
        return HttpResponseRedirect(reverse_lazy(
            "todo_list:task-list") + f"?page={current_page}"
        )


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo_list/tag_list.html"
    paginate_by = 5


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
