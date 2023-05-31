
from django.contrib import admin
from django.urls import path
from interpolation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('interpolation', views.interpolation_route)
]
