from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView

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
        context['task'] = get_object_or_404(Task, pk=kwargs['task_id'])
        return context


class TaskCreateView(View):
    def get(self, request):
        return render(request, 'task_create.html', context={
            'form': TaskForm()
        })

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            data = {}
            for key, value in form.cleaned_data.items():
                if value is not None:
                    data[key] = value
            task = Task.objects.create(**data)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={
                'form': form
            })
# Create your views here.
