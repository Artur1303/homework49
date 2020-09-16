from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

from .models import Profile


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super(MyUserCreationForm, self).clean()
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")

        if not last_name and not first_name:
            raise forms.ValidationError("Заполните поли хотябы  одно  поле Last_name или First_name")

        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']