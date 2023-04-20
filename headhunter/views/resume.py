from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from headhunter.forms.resume import ResumeForm, ExperienceForm, EducationForm
from headhunter.models import Resume, Experience, Education


class CreateResumeView(LoginRequiredMixin, CreateView):
    template_name = 'resume_create.html'
    model = Resume
    form_class = ResumeForm

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.author = request.user
                resume.save()
                return redirect('resume_detail', pk=resume.pk)
            else:
                context = {'form': form}
                return self.render_to_response(context)
        else:
            return HttpResponseForbidden()

    def get_success_url(self):
        return reverse_lazy('resume_detail', kwargs={'pk': self.request.user.pk})


class UpdateResumeView(UpdateView):
    template_name = 'resume_update.html'
    form_class = ResumeForm
    model = Resume

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateResumeView, self).get_context_data()
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        context['resume'] = resume
        return context

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})


class ResumeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'resume_detail.html'
    model = Resume
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        experiences = Experience.objects.filter(resume_id=self.object.pk)
        education = Education.objects.filter(resume_id=self.object.pk)
        context['experiences'] = experiences
        context['education'] = education
        return context


class CreateExperienceView(CreateView):
    template_name = 'experience_create.html'
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


# class ExperienceUpdateView(PermissionRequiredMixin, UpdateView):
#     template_name = 'experience_update.html'
#     model = Experience
#     form_class = ExperienceForm
#     permission_required = 'webapp.change_experience'
#
#     def get_success_url(self):
#         return reverse('resume', kwargs={'pk': self.object.pk})
#
#     def has_permission(self):
#         return super().has_permission() and self.get_object().author == self.request.user \
#             or self.request.user.is_superuser
#

class EducationCreateView(CreateView):
    template_name = 'education_create.html'
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


# class EducationUpdateView(PermissionRequiredMixin, UpdateView):
#     template_name = 'education_update.html'
#     model = Education
#     form_class = EducationForm
#     permission_required = 'webapp.change_education'
#
#     def get_success_url(self):
#         return reverse('resume', kwargs={'pk': self.object.pk})
#
#     def has_permission(self):
#         return super().has_permission() and self.get_object().author == self.request.user \
#             or self.request.user.is_superuser


class ResumeUpdateDateView(UpdateView):
    model = Resume

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(id=kwargs['pk'])
        resume.updated_at = datetime.now()
        resume.save()
        return redirect('profile', resume.author.pk)
