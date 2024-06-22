from django.urls import path
from .views import MaterialHomePageView, UpdateMaterialView

app_name = 'storage'

urlpatterns = [
    path('', MaterialHomePageView.as_view(), name="materials"),
    path('update/<int:pk>/', UpdateMaterialView.as_view(), name="update-material"),
]
