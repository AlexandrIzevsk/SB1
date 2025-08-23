from django import forms
from django.core.exceptions import ValidationError

from .models import Machine


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
