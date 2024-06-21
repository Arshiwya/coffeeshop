from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


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
