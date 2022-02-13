from django import forms
from employers.models import Task


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class CreateNewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'valid_until', 'status', 'is_published', 'tags')
        labels = {
            'name': 'Nazwa projektu',
            'description': 'Opis projektu',
            'valid_until': 'Zadanie aktywne do',
            'status': 'Status zadania',
            'is_published': 'Opublikuj',
            'tags': 'Tagi',
        }
        widgets = {
            'valid_until': DatePickerInput(),
        }


class TaskEnrollForm(forms.Form):
    task = forms.ModelChoiceField(queryset=Task.objects.all(), widget=forms.HiddenInput)
