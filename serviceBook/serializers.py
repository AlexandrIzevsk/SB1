from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


# class MachineSerializer(serializers.HyperlinkedModelSerializer):
class MachineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Machine
        fields = [
            'id',
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
            # 'serviceCompany',
        ]
        # extra_kwargs = {
        #     'modelMachine': {'lookup_field': 'name'}
        # }


class TOSerializer(serializers.HyperlinkedModelSerializer):
    typeTO = serializers.HyperlinkedRelatedField(
        view_name='manual-detail',
        # lookup_field='id',
        # many=True,
        read_only=True
    )
    class Meta:
        model = TO
        fields = [
            'machine',
            'typeTO',
            'dateTO',
            'runTime',
            'numberOrder',
            'dateOrder',
            # 'serviceTO',
        ]

class ReclamationSerializer(serializers.HyperlinkedModelSerializer):
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
            # 'serviceCompanyR',
        ]


class ManualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manual
        fields = [
            'nameClass',
            'name',
            'descriptions',
        ]
