from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect

from django.utils.http import urlencode
from django.views.generic import ListView,  FormView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.forms import SimpleSearchForm, ProjectForm, UserForm
from webapp.models import Project


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    paginate_by = 2
    paginate_orphans = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        kwargs['form'] = form
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Project.objects.all().filter(is_deleted=False)
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(name__icontains=search) | Q(descriptions__icontains=search))
        return data.order_by('end_date')


@login_required
def project_mass_action_view(request):
    if request.method == 'POST':
        ids = request.POST.getlist('project_select', [])
        if 'delete' in request.POST:
            Project.objects.filter(id__in=ids).delete()
    return redirect('index')


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project
    paginate_tasks_by = 5
    paginate_tasks_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        if project.is_deleted:
            raise Http404("Проект не найден")
        tasks = project.tasks.all()
        context['tasks'] = tasks
        tasks, page, is_paginated = self.paginate_tasks(self.object)
        context['tasks'] = tasks
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_tasks(self, project):
        tasks = project.tasks.all()
        if tasks.count() > 0:
            paginator = Paginator(tasks, self.paginate_tasks_by, orphans=self.paginate_tasks_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1  # page.has_other_pages()
            return page.object_list, page, is_paginated
        else:
            return tasks, None, False


class ProjectCreat(PermissionRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'webapp.add_project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_project'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted=True
        self.object.save()
        return HttpResponseRedirect(success_url)


class UserView(PermissionRequiredMixin, UpdateView):
    template_name = 'project/users.html'
    form_class = UserForm
    model = Project
    # permission_required = ('auth.add_user', 'auth.delete_user')

    def has_permission(self):
        project = self.get_object()
        user1=self.request.user
        print(user1)
        return user1.groups.filter(name__in=('Project Manager', 'Team Lead')) and user1 in project.users.all()

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})
