from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm

class HomeView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Task
    login_url = 'login'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {'form':form}
        return self.get(request, context ,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

class UpdateTaskView(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
        context = {'form': form}
        return render(request, 'index.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST, user=request.user, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {'form': form}
        return render(request, 'index.html', context)

class DeleteTaskView(View):

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('index')
