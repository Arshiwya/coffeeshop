from django.urls import path, include
from .views import (SignUserView, LoginPageView,
                    LogoutUserView, ContactView,
                    AboutView)

from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import path, reverse_lazy




app_name = 'accounts'

urlpatterns = [
    path('signin/', SignUserView.as_view(), name='signin'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html',
                                                                 success_url=reverse_lazy('accounts:password_reset_done'),
                                                                 email_template_name='accounts/password_reset_email.html'),
                                                                 name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
                                                                          name='password_reset_done'),

    path('password/reset/confirm/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
                                                                                                        success_url=reverse_lazy('accounts:password_reset_complete')),
                                                                                name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name= 'password_reset_complete'),

    path('contact_page/', ContactView.as_view(), name='contact-page'),
    path('about_us/',AboutView.as_view(), name='about us' )

    ]


