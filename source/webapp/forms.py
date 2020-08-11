from django import forms
from .models import Status, Task, Type


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'descriptions', 'status', 'type']


