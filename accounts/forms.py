from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

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
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar'
        )


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    old_password = forms.CharField(
        label="Старый пароль",
        strip=False,
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неверный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']