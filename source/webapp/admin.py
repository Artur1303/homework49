from django.contrib import admin
from webapp.models import Status, Type, Task, Project


admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Task)
admin.site.register(Project)