from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')),
                  path('users/', include('accounts.urls')),
                  path('orders/', include('orders.urls')),
                  path('storage/', include('storage.urls')),
                  path('products/', include('products.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
