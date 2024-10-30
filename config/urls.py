from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path("management/", admin.site.urls),
    path('', include('expenses_mate.urls')),
    path('accounts/', include('allauth.urls'))
]
