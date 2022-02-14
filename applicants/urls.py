from django.urls import path
from applicants import views

app_name = 'applicants'

urlpatterns = [
    path('dashboard/', views.ApplicantDashboardView.as_view(), name='applicant-dashboard'),
]
