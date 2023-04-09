from django import forms
from accounts.models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label= 'Password', widget=forms.PasswordInput)


class CustomUserCreationForm(forms.ModelForm):
    type = forms.ChoiceField( widget=forms.RadioSelect)
    avatar = forms.ImageField(required=False)
    password = forms.CharField(label='Password', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', strip=False, required=True,
                                       widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_confirm', 'type', 'phone', 'avatar']

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

