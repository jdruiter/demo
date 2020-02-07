from django.contrib import admin
from django.urls import path

from zaaksysteem import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.compute),
    path('<path:input_str>', views.compute),
]
