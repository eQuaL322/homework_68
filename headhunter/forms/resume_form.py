from django import forms
from headhunter.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('title', 'sex', 'vacancy', 'about', 'salary', 'phone', 'email', 'telegram', 'linkedin', 'facebook')
