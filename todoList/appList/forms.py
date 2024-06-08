from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    task = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'task_field', 'placeholder': 'Add your task here...'}))
    class Meta:
        model = Task
        fields = ['task']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        instance.task = self.data['task']

        if commit:
            instance.save()
        return instance