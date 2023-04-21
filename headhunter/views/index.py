from django.views.generic import ListView

from headhunter.models import Resume
from headhunter.models.resume import VacancyChoices
from headhunter.models.vacancy import Vacancy


class VacancyView(ListView):
    template_name = 'vacancy/vacancy_list.html'
    model = Vacancy
    context_object_name = 'vacancies'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.checks = self.request.GET.getlist('checks')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_hidden=False)
        queryset = queryset.order_by('-updated_at')
        if self.checks:
            search_category_list = [choice[0] for choice in VacancyChoices.choices if choice[1] in self.checks]
            queryset = queryset.filter(category__in=search_category_list)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = [(choice.value, choice.name) for choice in VacancyChoices]
        return context


class ResumeListView(ListView):
    model = Resume
    context_object_name = 'resumes'
    template_name = 'resume/resume_list.html'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.checks = self.request.GET.getlist('checks')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_hidden=False)
        queryset = queryset.order_by('-updated_at')
        if self.checks:
            search_category_list = [choice[0] for choice in VacancyChoices.choices if choice[1] in self.checks]
            queryset = queryset.filter(vacancy__in=search_category_list)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = [(choice.value, choice.name) for choice in VacancyChoices]
        return context
