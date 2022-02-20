from django.urls import path
from applicants import views

app_name = 'applicants'

urlpatterns = [
    path('dashboard/', views.ApplicantDashboardView.as_view(), name='applicant-dashboard'),
    path('enroll-task/', views.ApplicantEnrollTaskView.as_view(), name='applicant-enroll-task'),
    path('task/<int:id>/', views.ApplicantTaskDetailView.as_view(), name='applicant-task-detail'),
    path('task-list/', views.TaskListView.as_view(), name='all-task-list'),
]
