from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusesList.as_view(), name='statuses-list'),
    path('create/', views.StatusCreate.as_view(), name='create-status'),
    path(
        '<int:pk>/update/',
        views.StatusUpdate.as_view(),
        name='update-status',
    ),
    path(
        '<int:pk>/delete/',
        views.StatusDelete.as_view(),
        name='delete-status',
    ),
]
