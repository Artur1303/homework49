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
    # summary = forms.CharField(max_length=100, label='Заголовок', validators=[MinLengthValidator(10)])
    # descriptions = forms.CharField(max_length=3000, required=False, label='Описание',widget=forms.Textarea)
    # status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус')
    # type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=True, label='Тип')

    # def clean(self):
    #         cleaned_data = super().clean()
    #         errors = []
    #         valid = ('mat','fack','han')
    #         descriptions = cleaned_data.get('descriptions')
    #         for valids in valid:
    #             if descriptions == valids:
    #                 errors.append(ValidationError("You used a bad word in the description"))
    #                 raise ValidationError(errors)
    #         return cleaned_data


