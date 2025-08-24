from rest_framework import viewsets
from .serializers import *
from .models import *


class MachineViewset(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class TOViewset(viewsets.ModelViewSet):
    queryset = TO.objects.all()
    serializer_class = TOSerializer


class ReclamationViewset(viewsets.ModelViewSet):
    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer


class ManualViewset(viewsets.ModelViewSet):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer
