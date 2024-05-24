from django import forms


from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4, "cols": 40}),
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": forms.SelectMultiple(attrs={
                "size": 10,
                "style": "height: 150px; "
                         "overflow-y: scroll;"
            })
        }


class ToggleAssignDoneToNotDoneForm(forms.Form):
    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ["name"]
