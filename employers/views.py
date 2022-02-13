from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views import generic
from employers.models import Task
from django.views import generic
from employers.forms import CreateNewTaskForm, TaskEnrollForm
from django.urls import reverse_lazy
from employers.mixins import AccessRestrictedMixin


class HomePageView(generic.TemplateView):
    template_name = 'employers/index.html'


class CreateNewTaskView(AccessRestrictedMixin, PermissionRequiredMixin, generic.CreateView):
    template_name = 'employers/task_create.html'
    permission_required = 'employers.add_task'
    form_class = CreateNewTaskForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateNewTaskView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employers:dashboard')


class DashboardView(AccessRestrictedMixin, generic.ListView):
    template_name = 'employers/dashboard.html'
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        qs = super(DashboardView, self).get_queryset()
        return qs.filter(author=self.request.user)


class TaskDetailView(AccessRestrictedMixin, generic.DetailView):
    template_name = 'employers/task_detail.html'
    model = Task
    context_object_name = 'task'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = super(TaskDetailView, self).get_queryset()
        return qs.filter(author=self.request.user)


class TaskUpdateView(AccessRestrictedMixin, generic.UpdateView):
    template_name = 'employers/task_update.html'
    permission_required = 'employers.change_task'
    model = Task
    form_class = CreateNewTaskForm
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = super(TaskUpdateView, self).get_queryset()
        return qs.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('employers:dashboard')


class TaskDeleteView(AccessRestrictedMixin, generic.DeleteView):
    template_name = 'employers/task_delete.html'
    permission_required = 'employers.delete_task'
    model = Task
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = super(TaskDeleteView, self).get_queryset()
        return qs.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('employers:dashboard')
