from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
# Create your views here.

class CustomLoginView(LoginView):
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Welcome, {self.request.user.get_full_name()}!')
        return response


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get_success_url(self):
        messages.success(self.request, 'Registration successful. You can login now.')
        return reverse('login')