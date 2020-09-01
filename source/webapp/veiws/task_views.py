from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View,  FormView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskView(DetailView):
    template_name = 'task/task_view.html'
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task/task_create.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        project = get_object_or_404(Project, pk = self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('task_view', pk=task.pk)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'task/task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'task/delete_view.html'
    model = Task
    success_url = reverse_lazy('index')