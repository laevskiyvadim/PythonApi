from django.urls import path, include
from .views import *

urlpatterns = [
    path('tasks/', TasksView.as_view()),
    path('tasks/<int:pk>/', TasksView.as_view()),
]
