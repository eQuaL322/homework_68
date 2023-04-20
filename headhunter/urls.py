from django.urls import path

from headhunter.views.resume import ResumeUpdateDateView, ResumeDetailView, CreateResumeView, CreateExperienceView, \
    EducationCreateView

urlpatterns = [
    path('resume/<int:pk>/update/date/', ResumeUpdateDateView.as_view(), name='resume_update_date'),
    path('resume/<int:pk>/detail', ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/create/', CreateResumeView.as_view(), name='resume_create'),
    path('resume/<int:pk>/experience/add/', CreateExperienceView.as_view(), name='experience_add'),
    path('resume/<int:pk>/education/add/', EducationCreateView.as_view(), name='education_add')
]
