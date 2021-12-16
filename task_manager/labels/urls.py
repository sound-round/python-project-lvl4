from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelsList.as_view(), name='labels-list'),
    path('create/', views.LabelCreate.as_view(), name='create-label'),
    path(
        '<int:pk>/update/',
        views.LabelUpdate.as_view(),
        name='update-label',
    ),
    path(
        '<int:pk>/delete/',
        views.LabelDelete.as_view(),
        name='delete-label',
    ),
]
