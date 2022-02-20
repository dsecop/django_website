from statistics import mode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from employers.models import Task
from django.views import generic
from django.views.generic.edit import FormView
from applicants.forms import TaskEnrollForm


class ApplicantDashboardView(LoginRequiredMixin, generic.ListView):
    template_name = 'applicants/dashboard.html'
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        qs  =super(ApplicantDashboardView, self).get_queryset()
        return qs.filter(applicants__in=[self.request.user])

class TaskListView(LoginRequiredMixin, generic.ListView):
    template_name = 'applicants/task_list.html'
    model = Task
    context_object_name = 'tasks'


class ApplicantEnrollTaskView(LoginRequiredMixin, FormView):
    task = None
    form_class = TaskEnrollForm

    def form_valid(self, form):
        self.task = form.cleaned_data['task']
        self.task.applicants.add(self.request.user)
        return super(ApplicantEnrollTaskView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('applicants:applicant-task-detail', args=[self.task.id])


class ApplicantTaskDetailView(generic.DetailView):
    template_name = 'applicants/task_detail.html'
    model = Task
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = super(ApplicantTaskDetailView, self).get_queryset()
        return qs.filter(applicants__in=[self.request.user])
