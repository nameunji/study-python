from django.contrib import admin
from django.urls import path, include
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include(urls)),
    path("api/", include("ebooks.api.urls"))
]
