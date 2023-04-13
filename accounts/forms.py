from django import forms
from django.contrib.auth import get_user_model

from accounts.models import UserTypeChoice


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя пользователя'})
    )
    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль'})
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='',
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )
    password_confirm = forms.CharField(
        label='',
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}),
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password_confirm', 'type', 'phone', 'avatar']
        labels = {
            'username': '',
            'email': '',
            'type': '',
            'phone': '',
            'avatar': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'type': forms.Select(choices=UserTypeChoice.choices),
            'phone': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'avatar': forms.ClearableFileInput(attrs={'required': False}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Wrong Password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
