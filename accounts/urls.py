from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, ProfileChangeView, PasswordChangeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change/', ProfileChangeView.as_view(), name='profile_change'),
    path('profile/password-change/', PasswordChangeView.as_view(), name='password_change'),
]
