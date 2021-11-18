from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersList.as_view(), name='users-list'),
    path('create/', views.UserCreate.as_view(), name='create-user'),
]