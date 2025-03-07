from django import forms
from .models import Tasks


class TaskForms(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'due_date', 'is_completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }