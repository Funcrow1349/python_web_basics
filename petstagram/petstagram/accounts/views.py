from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm
from petstagram.accounts.models import PetstagramUser
from django.contrib.auth import views as auth_views


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('profile login')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('profile login')


def profile_details(request):
    return render(request, 'accounts/profile-details-page.html')


def profile_edit(request):
    return render(request, 'accounts/profile-edit-page.html')


def profile_delete(request):
    return render(request, 'accounts/profile-delete-page.html')
