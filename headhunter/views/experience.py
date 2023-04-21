from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from headhunter.forms.experience_form import ExperienceForm
from headhunter.models import Experience, Resume


class CreateExperienceView(LoginRequiredMixin, CreateView):
    template_name = 'experience/experience_create.html'
    model = Experience
    form_class = ExperienceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = get_object_or_404(Resume, pk=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        resume = get_object_or_404(Resume, pk=self.kwargs['pk'])
        if form.is_valid():
            experience = form.save(commit=False)
            experience.resume = resume
            experience.save()
            return redirect('resume_detail', pk=resume.pk)
        context = {'form': form, 'resume': resume}
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy('resume_detail', kwargs={'pk': self.request.user.pk})


class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'experience/experience_update.html'
    model = Experience
    form_class = ExperienceForm

    def get_context_data(self, **kwargs):
        context = super(ExperienceUpdateView, self).get_context_data(**kwargs)
        experience = self.get_object()
        context['experience'] = experience
        return context

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})
