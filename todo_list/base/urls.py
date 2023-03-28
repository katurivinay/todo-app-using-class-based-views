from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,RegisterPage,TaskReorder
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'),
    path('register/',RegisterPage.as_view(),name = 'register'),
    path('',TaskList.as_view(),name='tasks'),
    path('taskview/<int:pk>/',TaskDetail.as_view(),name = 'task-view'),
    path('create-task/',TaskCreate.as_view(),name = 'task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name = 'task-update'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name = 'task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

]