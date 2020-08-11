from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView, FormView
from django.urls import reverse
from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskCreateView(FormView):
    template_name = 'task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})


class TaskUpdateView(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_initial(self):
        initial = {}
        for key in 'summary', 'descriptions', 'status':
            initial[key] = getattr(self.task, key)
        initial['type'] = self.task.type.all()
        return initial

    def form_valid(self, form):
        type = form.cleaned_data.pop('type')
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.task, key, value)
        self.task.save()
        self.task.type.set(type)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)


class TaskDeleteView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        print(task)
        return render(request, 'delete_view.html', context={'task': task})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')

