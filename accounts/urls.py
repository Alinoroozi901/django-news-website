from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
]