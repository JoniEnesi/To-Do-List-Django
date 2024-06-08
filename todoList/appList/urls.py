from django.urls import path
from .views import HomeView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('edit/<str:pk>/', UpdateTaskView.as_view(), name='edit'),
    path('check/<str:pk>/', DeleteTaskView.as_view(), name='check'),
]
