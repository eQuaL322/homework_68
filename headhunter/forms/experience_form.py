from django import forms

from headhunter.models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('company', 'vacancy', 'about', 'start_date', 'end_date')
