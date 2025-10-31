# alx_travel_app/listings/urls.py
from django.urls import path
from .views import health

urlpatterns = [ path('health/', health) ]

