from django.urls import path

from headhunter.views.resume import ResumeUpdateDateView, ResumeDetailView, CreateResumeView, UpdateResumeView
from headhunter.views.education import EducationCreateView, EducationUpdateView
from headhunter.views.experience import CreateExperienceView, ExperienceUpdateView
from headhunter.views.vacancy import CreateVacancyView, VacancyDetailView, UpdateVacancyView

urlpatterns = [
    path('resume/<int:pk>/update/date/', ResumeUpdateDateView.as_view(), name='resume_update_date'),
    path('resume/<int:pk>/detail', ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/create/', CreateResumeView.as_view(), name='resume_create'),
    path('resume/<int:pk>/experience/add/', CreateExperienceView.as_view(), name='experience_add'),
    path('resume/<int:pk>/education/add/', EducationCreateView.as_view(), name='education_add'),
    path('resume/<int:pk>/edit', UpdateResumeView.as_view(), name='resume_edit'),
    path('resume/<int:pk>/experience/edit/', ExperienceUpdateView.as_view(), name='experience_edit'),
    path('resume/<int:pk>/education/edit/', EducationUpdateView.as_view(), name='education_edit'),
    path('vacancy/<int:pk>/update/date/', UpdateVacancyView.as_view(), name='vacancy_edit'),
    path('vacancy/<int:pk>/detail', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/create/', CreateVacancyView.as_view(), name='vacancy_create'),
]
