from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('products/', views.products, name='products'),
    path('register_course/', views.register_course, name='register_course'),
    path('list_course/', views.list_course, name='list_course'),
    path('admin_index/', views.admin_index, name='admin_index'),
    path('admin_signin/', views.admin_signin, name='admin_signin'),
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('admin_signout/', views.admin_signout, name='admin_signout'),
]
