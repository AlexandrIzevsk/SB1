from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import (
    Machine, TO,
)


class MachineList(ListView):
    # logger.info('INFO')
    queryset = Machine.objects.all()
    template_name = 'Machine.html'
    context_object_name = 'machine'
    paginate_by = 10



class TOList(PermissionRequiredMixin,ListView):
    # logger.info('INFO')
    raise_exception = True
    permission_required = ('serviceBook.view_TO',)
    queryset = TO.objects.all()
    template_name = 'TO.html'
    context_object_name = 'TO'
    paginate_by = 10


# class
