from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import (
    Machine, TO, Reclamation, Manual
)
from .filters import MachineFilter, TOFilter, ReclamationFilter
from .forms import MachineForm


class MachineList(ListView):
    queryset = Machine.objects.order_by('-shipDate')
    template_name = 'Machine.html'
    context_object_name = 'machine'
    paginate_by = 4

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = MachineFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список машин
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class MachineCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('serviceBook.add_machine',)
    form_class = MachineForm
    model = Machine
    template_name = 'machine_edit.html'


class MachineUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('serviceBook.change_machine',)
    form_class = MachineForm
    model = Machine
    template_name = 'machine_edit.html'

class OneMachineDetail(DetailView):
    queryset = Machine.objects.all()
    template_name = 'one_machine.html'
    context_object_name = 'machine'


class TOList(PermissionRequiredMixin,ListView):
    # logger.info('INFO')
    raise_exception = True
    permission_required = ('serviceBook.view_to',)
    queryset = TO.objects.order_by('-dateTO')
    template_name = 'TO.html'
    context_object_name = 'TO'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = TOFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список машин
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class ReclamationList(PermissionRequiredMixin,ListView):
    # logger.info('INFO')
    raise_exception = True
    permission_required = ('serviceBook.view_reclamation',)
    queryset = Reclamation.objects.order_by('-dateFailure')
    template_name = 'Reclamation.html'
    context_object_name = 'reclamation'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = ReclamationFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список машин
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset

        return context


class OneManualDetail(DetailView):
    queryset = Manual.objects.all()
    template_name = 'one_manual.html'
    context_object_name = 'manual'
