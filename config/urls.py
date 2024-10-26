from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("management/", admin.site.urls),
    path('', include('expenses_mate.urls')),
]
