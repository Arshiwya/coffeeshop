from django.urls import path
from .views import LoginPageView, LogoutUserView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
