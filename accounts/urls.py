from django.urls import path
from .views import (SignUserView, LoginPageView,
                    LogoutUserView, ContactView)

app_name = 'accounts'

urlpatterns = [
    path('signin/', SignUserView.as_view(), name='signin'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),

    path('contact_page/', ContactView.as_view(), name='contact-page'),

]
