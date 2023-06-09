from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    login = forms.CharField()
    hasło = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()


        user = authenticate(**cleaned_data)
        if user is None:
            raise ValidationError('niepoprawne dane logowania')
        cleaned_data['user'] = user
        return cleaned_data


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Hasła się nie zgadzają')
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email']