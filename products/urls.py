from django.contrib import admin
from django.urls import path
from .views import CreateProductView, UpdateProductView, DeleteProductView, CreateCategoryView, UpdateCategoryView, \
    DeleteCategoryView, ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailView.as_view(), name='details'),
    path('create/', CreateProductView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete'),
    path('category/create/', CreateCategoryView.as_view(), name='category-creat'),
    path('category/update/<int:pk>/', UpdateCategoryView.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', DeleteCategoryView.as_view(), name='category-delete'),
]
