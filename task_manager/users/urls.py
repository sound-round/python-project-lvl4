from django.urls import path, include
from task_manager.users import views

urlpatterns = [
    path('', views.UsersList.as_view(), name='users-list')
]