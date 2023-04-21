from datetime import datetime

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from headhunter.forms.resume_form import ResumeForm
from headhunter.models import Resume, Experience, Education


class CreateResumeView(LoginRequiredMixin, CreateView):
    template_name = 'resume/resume_create.html'
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


class UpdateResumeView(LoginRequiredMixin, UpdateView):
    template_name = 'resume/resume_update.html'
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
    template_name = 'resume/resume_detail.html'
    model = Resume
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        experiences = Experience.objects.filter(resume_id=self.object.pk)
        education = Education.objects.filter(resume_id=self.object.pk)
        context['experiences'] = experiences
        context['education'] = education
        return context


class ResumeUpdateDateView(UpdateView):
    model = Resume

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(id=kwargs['pk'])
        resume.updated_at = datetime.now()
        resume.save()
        return redirect('profile', resume.author.pk)


class SearchResumeListView(ListView):
    template_name = 'resume/resume_search.html'
    model = Resume
    context_object_name = 'resumes'
    search_value = ''

    def get(self, request, *args, **kwargs):
        self.search_value = request.GET.get('search')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__iregex=self.search_value)
            )
        return queryset


def toggle_resume_visibility(request, pk):
    resume = get_object_or_404(Resume, pk=pk)

    resume.is_hidden = not resume.is_hidden
    resume.save()

    return redirect('profile', pk=resume.author.pk)
