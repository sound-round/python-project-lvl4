from django.urls import path
from task_manager.tasks import views

urlpatterns = [
    path('', views.TasksList.as_view(), name='tasks-list'),
    # path('<int:pk>/', views.TaskDetail.as_view(), name='detail-task'),
    path('create/', views.TaskCreate.as_view(), name='create-task'),
    path(
        '<int:pk>/update/',
        views.TaskUpdate.as_view(),
        name='update-task',
    ),
    path(
        '<int:pk>/delete/',
        views.TaskDelete.as_view(),
        name='delete-task',
    ),
]
