from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('register/',views.register_view, name='register'),
    path('logout/',views.logout_view, name='logout'),
    path('forget-password/',views.forget_pass,name='forget'),
    path('new-password/',views.set_new_password,name='new-pass'),
]