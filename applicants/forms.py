from django import forms
from employers.models import Task


class TaskEnrollForm(forms.Form):
    task = forms.ModelChoiceField(queryset=Task.objects.all(), widget=forms.HiddenInput)
