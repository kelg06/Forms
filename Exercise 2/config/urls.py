from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path("front",front_times),
    path("teen",fix_teen),
    path("xyz",xyz),
    path("center",centered),
    path('admin/', admin.site.urls),
]
