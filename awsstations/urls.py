# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_predictions, name='get_predictions'),
]
