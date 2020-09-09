from django import forms
from .models import Status, Task, Type, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'descriptions', 'status', 'type']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['start_data', 'end_date', 'name', 'descriptions', 'users']
        widgets = {'users': forms.CheckboxSelectMultiple}


class UserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['users']
        widgets = {'users': forms.CheckboxSelectMultiple}


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


