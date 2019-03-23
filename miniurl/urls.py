from django.contrib import admin
from django.urls import path
from miniurl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.generate_url, name='generate_url'),    
    path('url/<pk>/', views.url_detail, name='url_detail'),
    path('<tiny_url>/', views.url_redirect, name='url_redirect'),
]