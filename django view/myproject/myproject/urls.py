from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scrolling_text.urls')),  # Добавьте эту строку
]
