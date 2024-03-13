from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('blog_detail/', views.blog_detail, name="blog_detail"),

]