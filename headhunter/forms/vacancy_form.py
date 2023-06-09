from django import forms

from headhunter.models.vacancy import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'requirements', 'description', 'salary', 'category', 'exp_from', 'exp_to')
