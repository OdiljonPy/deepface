from django.urls import path
from .views import verify_view, test_view

urlpatterns = [
    path('verify', verify_view),
    path('test', test_view),
]
