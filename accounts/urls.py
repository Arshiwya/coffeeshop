from django.urls import path
from .views import SignUserView, LoginPageView, LogoutUserView

app_name = 'accounts'

urlpatterns = [
    path('signin/', SignUserView.as_view(), name='signin'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
