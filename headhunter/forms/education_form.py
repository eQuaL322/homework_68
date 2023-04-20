from django import forms

from headhunter.models import Education


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('education_form', 'education', 'profession', 'start_date', 'end_date')
