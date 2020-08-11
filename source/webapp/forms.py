from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from .models import Status, Task, Type


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'descriptions', 'status', 'type']


