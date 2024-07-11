from django.urls import path
from .views import (
  TaskCreateView,
  TaskListView,
  TaskDetailView,
)

urlpatterns = [
  path('', TaskListView.as_view()),
  path('<int:pk>/', TaskDetailView.as_view()),
  path('create/', TaskCreateView.as_view()),
]
