from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
# from django.forms import DateTimeInput
from .models import Machine, Manual


class MachineFilter(FilterSet):
    modelMachine = ModelChoiceFilter(
        field_name='modelMachine',
        queryset=Manual.objects.filter(nameClass='MMC'),
        label='ModelMachine',
        empty_label='Любая',
    )
    modelMotor = ModelChoiceFilter(
        field_name='modelMotor',
        queryset=Manual.objects.filter(nameClass='MMT'),
        label='ModelMotor',
        empty_label='Любая',
    )
    modelTransmission = ModelChoiceFilter(
        field_name='modelTransmission',
        queryset=Manual.objects.filter(nameClass='MT'),
        label='ModelTransmission',
        empty_label='Любая',
    )
    modelDriveAxile = ModelChoiceFilter(
        field_name='modelDriveAxile',
        queryset=Manual.objects.filter(nameClass='MDA'),
        label='ModelDriveAxile',
        empty_label='Любая',
    )
    modelControllAxile = ModelChoiceFilter(
        field_name='modelControllAxile',
        queryset=Manual.objects.filter(nameClass='MCA'),
        label='ModelControllAxile',
        empty_label='Любая',
    )
    class Meta:
        model = Machine
        fields = {
            'zavNumberMachine': ['icontains'],
        }
