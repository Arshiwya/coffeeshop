from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import User
from .forms import SignUserForm
from .mixins import AnonymousUserMixin


class SignUserView(AnonymousUserMixin, CreateView):
    model = User
    template_name = 'accounts/signin-page.html'
    form_class = SignUserForm

    def form_valid(self, form):

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        password2 = form.cleaned_data["password2"]
        email = form.cleaned_data["email"]

        if password == password2:
            try:
                validate_password(password=password)
                user = User.objects.create_user(username=username, password=password, email=email)
                auth_login(self.request, user)
                return HttpResponseRedirect(self.get_success_url())

            except ValidationError as error:
                for e in error:
                    form.add_error(field='password', error=e)

                return self.form_invalid(form)

        else:
            form.add_error(field="password", error='Passwords are not match .')
            return self.form_invalid(form)

    def get_success_url(self):
        return '/'


class LoginPageView(LoginView):
    template_name = 'accounts/login-page.html'

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return '/'


class LogoutUserView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect(reverse_lazy('home:home'))

        return super().dispatch(request, *args, **kwargs)
