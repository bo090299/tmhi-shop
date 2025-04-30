from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.index, name='home'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('product/<int:id>/', views.product, name='product'),
    path('products/', views.products, name='products'),
    path('create-order/', views.create_order, name='create-order'),
    path('create-product/', views.create_product, name='create-product'),
    path('orders/', views.orders, name='orders'),
    path('salon/', views.salon, name='salon'),
    path('appointment/<int:stylist_id>/', views.appointment, name='appointment'),
    path('stylist/<int:stylist_id>/', views.stylist_detail, name='stylist_detail'),
]