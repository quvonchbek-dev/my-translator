from django.contrib import admin
from django.urls import path, include

from main.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/', include('api.urls'))
]
