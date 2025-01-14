from django.urls import path
from .views import LoginView
from .views import UserRegistrationView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
