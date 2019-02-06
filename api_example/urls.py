from django.urls import path
from .views import names

urlpatterns = [
    path('', names)
]
