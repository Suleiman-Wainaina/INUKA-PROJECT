from django.contrib import admin
from django.urls import path, include
from landingPage import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('concept', views.concept_view, name='concept'),
    path('cause', views.cause_view, name='cause'),
    path('ourcrew', views.ourcrew_view, name='ourcrew'),
    path('donate', views.donate_view, name='donate'),
    path('aboutus', views.aboutus_view, name='aboutus'),
    path('login', views.login_view, name='login'),
    path('admin', views.admin_view, name='admin')
]