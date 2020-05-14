from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('quiz_app/', include('quiz_app.urls')),
    path('admin/', admin.site.urls),
]