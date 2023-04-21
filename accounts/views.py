from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from accounts.forms import CustomUserCreationForm, LoginForm, PasswordChangeForm, UserChangeForm
from accounts.models import UserTypeChoice
from headhunter.models import Resume
from headhunter.models.vacancy import Vacancy


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, "Incorrect Data")
            return redirect('index')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.warning(request, "User Not Found")
            return redirect('index')
        login(request, user)
        if request.user.type == UserTypeChoice.COMPANY:
            return redirect('resume_list')
        else:
            return redirect('vacancy_list')


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.user.type == UserTypeChoice.COMPANY:
                return redirect('resume_list')
            else:
                return redirect('vacancy_list')
        context = {'form': form}
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        account = self.get_object()
        resumes = Resume.objects.filter(author=account)
        vacancy = Vacancy.objects.filter(author=account)
        kwargs['form'] = UserChangeForm(instance=account)
        kwargs['resumes'] = resumes
        kwargs['vacancy'] = vacancy
        return super().get_context_data(**kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        account = self.get_object()
        if account.type == UserTypeChoice.COMPANY:
            self.template_name = 'company_page.html'
        else:
            self.template_name = 'profile.html'
        return super().get(request, *args, **kwargs)


class ProfileChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'profile_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.object)
        return response
