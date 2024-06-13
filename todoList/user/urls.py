from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, RegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="registration/reset_password.html"), name='reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset.html"), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/reset_password_complete.html"), name='password_reset_complete'),
]