from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task-api', include('api.urls')),
    path('', include('api2.urls')),
]
