from django.contrib.auth.forms import UserCreationForm
from django import forms


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    def clean(self):
        cleaned_data = super(MyUserCreationForm, self).clean()
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")

        if last_name in first_name == '':
            raise forms.ValidationError("Заполните поли хотябы  одно  поле Last_name или First_name")

        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']



