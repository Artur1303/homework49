from django.db.models import Q
from django.views.generic import ListView


class SearchView(ListView):
    model = None
    context_key = 'objects'

