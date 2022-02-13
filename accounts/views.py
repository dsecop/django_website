from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login
from accounts.models import User
from django.contrib.auth.models import Group
from accounts.forms import UserRegistrationForm


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = UserRegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('employers:home-page')

    def form_valid(self, form):
        user = form.save()
        if user.user_type == User.DEVELOPER:
            group = Group.objects.get(name='developers')
            user.groups.add(group)
        elif user.user_type == User.EMPLOYER:
            group = Group.objects.get(name='employers')
            user.groups.add(group)
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)
