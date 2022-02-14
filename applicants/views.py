from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from employers.models import Task
from django.views import generic


class ApplicantDashboardView(LoginRequiredMixin, generic.ListView):
    template_name = 'applicants/dashboard.html'
    model = Task
