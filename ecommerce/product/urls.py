from django.urls import path

from . import views


urlpatterns = [
    path('product/', views.ProductView.as_view(), name='products'),
    path('products/search/', views.search, name='search'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product-detail'),    
    path('products/<slug:category_slug>/', views.CategoryDetailView.as_view(), name='categories'),
]