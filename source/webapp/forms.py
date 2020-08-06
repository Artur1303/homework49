from django import forms
from .models import Status, Task, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=100, verbose_name='Заголовок')
    descriptions = forms.CharField(max_length=3000, required=False, label='Описание')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Тип')


