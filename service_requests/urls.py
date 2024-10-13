from django.urls import path
from .views import submit_request, request_success

urlpatterns = [
    path('', submit_request, name='submit_request'),  # Make sure this is the correct path
    path('success/', request_success, name='request_success'),
]
