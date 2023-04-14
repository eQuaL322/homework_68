from django import forms
from headhunter.models import Resume, Education, Experience


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('title', 'sex', 'vacancy', 'about', 'salary', 'phone', 'email', 'telegram', 'linkedin', 'facebook')

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('education_form', 'education','profession' ,'start_date', 'end_date')

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('company', 'vacancy', 'start_date', 'end_date')