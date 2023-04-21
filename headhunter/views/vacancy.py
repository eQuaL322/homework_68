from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from headhunter.forms.vacancy_form import VacancyForm
from headhunter.models.vacancy import Vacancy


class CreateVacancyView(LoginRequiredMixin, CreateView):
    template_name = 'vacancy/vacancy_create.html'
    model = Vacancy
    form_class = VacancyForm

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                vacancy = form.save(commit=False)
                vacancy.author = request.user
                vacancy.save()
                return redirect('vacancy_detail', pk=vacancy.pk)
            else:
                context = {'form': form}
                return self.render_to_response(context)
        else:
            return HttpResponseForbidden()

    def get_success_url(self):
        return reverse_lazy('vacancy_detail', kwargs={'pk': self.request.user.pk})


class UpdateVacancyView(LoginRequiredMixin, UpdateView):
    template_name = 'vacancy/vacancy_update.html'
    form_class = VacancyForm
    model = Vacancy

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateVacancyView, self).get_context_data()
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs.get('pk'))
        context['vacancy'] = vacancy
        return context

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})


class VacancyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'vacancy/vacancy_detail.html'
    model = Vacancy
    context_object_name = 'vacancy'

class VacancyUpdateDateView(UpdateView):
    model = Vacancy

    def post(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.get(id=kwargs['pk'])
        vacancy.updated_at = datetime.now()
        vacancy.save()
        return redirect('profile', vacancy.author.pk)


