from django.views.generic import TemplateView, ListView

from headhunter.models import Resume
from headhunter.models.vacancy import Vacancy


class VacancyView(ListView):
    template_name = 'vacancy/vacancy_list.html'
    model = Vacancy
    context_object_name = 'vacancies'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_hidden=False)
        queryset = queryset.order_by('-updated_at')
        return queryset


class ResumeListView(ListView):
    model = Resume
    context_object_name = 'resumes'
    template_name = 'resume/resume_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_hidden=False)
        queryset = queryset.order_by('-updated_at')
        return queryset
