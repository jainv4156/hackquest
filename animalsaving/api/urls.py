from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createComplain/', views.createComplain, name='createComplain'),
    path('getComplain/', views.getComplain, name='getComplain')
]
