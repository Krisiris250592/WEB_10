from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('kristina.urls')),
    path('admin/', admin.site.urls),
    path('users/', include("users.urls"))
]
