from django import forms
from django.core.exceptions import ValidationError

from .models import Machine, TO, Reclamation


class MachineForm(forms.ModelForm):
    # text = forms.CharField(min_length=20)

    class Meta:
        model = Machine
        fields = [
            'zavNumberMachine',
            'modelMachine',
            'modelMotor',
            'zavNumberMotor',
            'modelTransmission',
            'zavNumberTransmission',
            'modelDriveAxile',
            'zavNumberDA',
            'modelControllAxile',
            'zavNumberCA',
            'deliveryContract',
            'shipDate',
            'recipient',
            'deliveryAddress',
            'package',
            'client',
            'serviceCompany',
        ]


class TOForm(forms.ModelForm):
    class Meta:
        model = TO
        fields = [
            'machine',
            'typeTO',
            'dateTO',
            'runTime',
            'numberOrder',
            'dateOrder',
            'serviceTO',
        ]


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = [
            'machine',
            'dateFailure',
            'runTime',
            'failureNode',
            'descriptionFailure',
            'wayToRecover',
            'spareParts',
            'dateRetraiding',
            'serviceCompanyR',
        ]
