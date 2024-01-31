from django.urls import path
from .views import CategoryListView, BrandListView, ProductListView, IndexView

app_name = "products"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/brands/', BrandListView.as_view(), name='brand-list'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
]
