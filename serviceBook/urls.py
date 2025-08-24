from django.urls import include, path
from rest_framework import routers
from serviceBook import viewsets

from .views import (
    MachineList, TOList, ReclamationList, MachineCreate, MachineUpdate,
    OneMachineDetail, OneManualDetail, TOCreate, OneTODetail, TOUpdate,
    ReclamationCreate, OneReclamationDetail, ReclamationUpdate
)


router = routers.DefaultRouter()
router.register(r'machine', viewsets.MachineViewset)
router.register(r'TO', viewsets.TOViewset)
router.register(r'reclamation', viewsets.ReclamationViewset)
router.register(r'manual', viewsets.ManualViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('machine/', MachineList.as_view(), name='machine_list'),
    path('machine/<int:pk>', OneMachineDetail.as_view(), name='machine_detail'),
    path('machine/create/', MachineCreate.as_view(), name='machine_create'),
    path('machine/<int:pk>/edit', MachineUpdate.as_view(), name='machine_update'),
    path('manual/<int:pk>', OneManualDetail.as_view(), name='manual_detail'),
    path('TO/', TOList.as_view(), name='TO_list'),
    path('TO/create/', TOCreate.as_view(), name='TO_create'),
    path('TO/<int:pk>', OneTODetail.as_view(), name='TO_detail'),
    path('TO/<int:pk>/edit', TOUpdate.as_view(), name='TO_update'),
    path('reclamation/', ReclamationList.as_view(), name='Reclamation_list'),
    path('reclamation/create/', ReclamationCreate.as_view(), name='Reclamation_create'),
    path('reclamation/<int:pk>', OneReclamationDetail.as_view(), name='Reclamation_detail'),
    path('reclamation/<int:pk>/edit', ReclamationUpdate.as_view(), name='Reclamation_update'),
]
