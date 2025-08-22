from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
# from django.forms import DateTimeInput
from .models import Machine, Manual, Service


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


class TOFilter(FilterSet):
    machine = ModelChoiceFilter(
        field_name='machine',
        queryset=Machine.objects.all(),
        label='ZavNumberMachine',
        empty_label='Любой',
    )
    typeTO = ModelChoiceFilter(
        field_name='typeTO',
        queryset=Manual.objects.filter(nameClass='TTO'),
        label='TypeTO',
        empty_label='Любой',
    )
    serviceTO = ModelChoiceFilter(
        field_name='serviceTO',
        queryset=Service.objects.all(),
        label='ServiceTO',
        empty_label='Любой',
    )


class ReclamationFilter(FilterSet):
    serviceCompanyR = ModelChoiceFilter(
        field_name='serviceCompanyR',
        queryset=Service.objects.all(),
        label='ServiceCompanyR',
        empty_label='Любая',
    )
