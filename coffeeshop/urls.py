from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('storage/', include('storage.urls')),
    path('products/', include('products.urls')),
]
