from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import (
    Machine, TO, Reclamation
)
from .filters import MachineFilter


class MachineList(ListView):
    # logger.info('INFO')
    queryset = Machine.objects.order_by('-shipDate')
    template_name = 'Machine.html'
    context_object_name = 'machine'
    paginate_by = 10

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = MachineFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context



class TOList(PermissionRequiredMixin,ListView):
    # logger.info('INFO')
    raise_exception = True
    permission_required = ('serviceBook.view_to',)
    queryset = TO.objects.order_by('-dateTO')
    template_name = 'TO.html'
    context_object_name = 'TO'
    paginate_by = 10


class ReclamationList(PermissionRequiredMixin,ListView):
    # logger.info('INFO')
    raise_exception = True
    permission_required = ('serviceBook.view_reclamation',)
    queryset = Reclamation.objects.order_by('-dateFailure')
    template_name = 'Reclamation.html'
    context_object_name = 'reclamation'
    paginate_by = 10


