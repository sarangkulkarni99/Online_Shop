from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Home Page
    path('', views.CategoryList.as_view(), name='index'),

    # All Posts
    path('categories/', views.CategoryList.as_view(), name='home'),

    # All Comments
    path('categories/<int:category_id>/', views.shop_list, name='shop_list'),


    # page for all replies
    path('products/<shop_id>', views.product_list, name='product_list'),
]