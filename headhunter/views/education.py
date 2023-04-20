from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from headhunter.forms.education_form import EducationForm
from headhunter.models import Education, Resume


class EducationCreateView(CreateView):
    template_name = 'education/education_create.html'
    model = Education
    form_class = EducationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = get_object_or_404(Resume, pk=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        resume = get_object_or_404(Resume, pk=self.kwargs['pk'])
        if form.is_valid():
            education = form.save(commit=False)
            education.resume = resume
            education.save()
            return redirect('resume_detail', pk=resume.pk)
        context = {'form': form, 'resume': resume}
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy('resume_detail', kwargs={'pk': self.request.user.pk})


class EducationUpdateView(UpdateView):
    template_name = 'education/education_update.html'
    model = Education
    form_class = EducationForm

    def get_context_data(self, **kwargs):
        context = super(EducationUpdateView, self).get_context_data(**kwargs)
        education = self.get_object()
        context['education'] = education
        return context

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})
