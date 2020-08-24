"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.veiws.project_views import ProjectIndexView,ProjectView, ProjectCreat, ProjectUpdate
from webapp.veiws.task_views import TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectIndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('project/<int:pk>/tasks/add/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('project/<int:pk>/project_view/', ProjectView.as_view(), name='project_view'),
    path('project/add/', ProjectCreat.as_view(), name='project_create'),
    path('project/update/<int:pk>/project_update/', ProjectUpdate.as_view(), name='project_update'),

]


