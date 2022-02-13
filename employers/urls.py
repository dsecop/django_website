from django.urls import path
from employers import views

app_name = 'employers'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create/', views.CreateNewTaskView.as_view(), name='task-create'),
    path('<int:id>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('<int:id>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('<int:id>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
]
