from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


# CHOICES = [('1v', '1 v'), ('2v', '2 v'), ('3v', '3 v')]
#
#
# class TrainingForm(forms.Form):
#     select_field = forms.ChoiceField(choices=[('1v', '1 v'), ('2v', '2 v'), ('3v', '3 v')])
#     radio_field = forms.ChoiceField(widget=forms.RadioSelect, choices=(('Yes', 'Да'), ('No', 'Нет')))
#     checkbox_field = forms.BooleanField(required=False)


class ChooseTargetForm(forms.Form):
    def __init__(self, colums, *args, **kwargs):
        super(ChooseTargetForm, self).__init__(*args, **kwargs)
        self.fields['target'] = forms.ChoiceField(widget=forms.RadioSelect, choices=colums)


class MyForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    email = forms.CharField(label='Почта')
    filename = forms.ChoiceField(choices=[("Lite", "Lite"), ("Pro", "Pro"), ("Master", "Master")], label='Услуга')
