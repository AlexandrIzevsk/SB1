from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class RegUser(User):
    serviceCompany = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)


class Service(models.Model):
    name = models.CharField(max_length=20)
    descriptions = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Manual(models.Model):
    modelMachine = 'MMC'
    modelMotor = 'MMT'
    modelTransmission = 'MT'
    modelDriveAxile = 'MDA'
    modelControllAxile = 'MCA'
    typeTO = 'TTO'
    failureNode = 'FND'
    wayToRecover = 'WTR'

    CHOICES = [
        (modelMachine, 'Модель техники'),
        (modelMotor, 'Модель двигателя'),
        (modelTransmission, 'Модель трансмиссии'),
        (modelDriveAxile, 'Модель ведущего моста'),
        (modelControllAxile, 'Модель управляемого моста'),
        (typeTO, 'Вид ТО'),
        (failureNode, 'Узел отказа'),
        (wayToRecover, 'Способ восстановления'),
    ]

    nameClass = models.CharField(max_length=3, choices=CHOICES, default=modelMachine)
    name = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_detail', args=[str(self.id)])


class Machine(models.Model):
    zavNumberMachine = models.CharField(max_length=20, unique=True)
    modelMachine = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE,
        limit_choices_to={'nameClass': 'MMC'},
        related_name='modelMachine')
    modelMotor = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE,
        limit_choices_to={'nameClass': 'MMT'},
        related_name='modelMotor')
    zavNumberMotor = models.CharField(max_length=20)
    modelTransmission = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE,
        limit_choices_to={'nameClass': 'MT'},
        related_name='modelTransmission')
    zavNumberTransmission = models.CharField(max_length=20)
    modelDriveAxile = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE,
        limit_choices_to={'nameClass': 'MDA'},
        related_name='modelDriveAxile')
    zavNumberDA = models.CharField(max_length=20)
    modelControllAxile = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE,
        limit_choices_to={'nameClass': 'MCA'},
        related_name='modelControllAxile')
    zavNumberCA = models.CharField(max_length=20)
    deliveryContract = models.CharField(max_length=50)
    shipDate = models.DateTimeField(default=datetime.today)
    recipient = models.CharField(max_length=100)
    deliveryAddress = models.CharField(max_length=150)
    package = models.TextField(blank=True)
    client = models.CharField(max_length=150)
    serviceCompany = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='serviceCompany')

    def get_absolute_url(self):
        return reverse('machine_detail' , args=[str(self.id)])

    def __str__(self):
        return f'{self.modelMachine}. Зав.№{self.zavNumberMachine}'

class TO(models.Model):
    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        primary_key=True
    )
    typeTO = models.ForeignKey(
        Manual,
        limit_choices_to={'nameClass': 'TTO'},
        on_delete=models.CASCADE,
        related_name='typeTO')
    dateTO = models.DateTimeField(default=datetime.today)
    runTime = models.IntegerField(default=0)
    numberOrder = models.CharField(max_length=50, default=1)
    dateOrder = models.DateTimeField(default=datetime.today)
    serviceTO = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='serviceTO', default=1)

    def __str__(self):
        return f'ТО по заказ-наряду №{self.numberOrder}'


class Reclamation(models.Model):
    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        default=1
    )
    dateFailure = models.DateTimeField(default=datetime.today)
    runTime = models.IntegerField(default=0)
    failureNode = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE,
        limit_choices_to={'nameClass': 'FND'},
        related_name='failureNode')
    descriptionFailure = models.TextField()
    wayToRecover = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE,
        limit_choices_to={'nameClass': 'WTR'},
        related_name='wayToRecover')
    spareParts = models.TextField()
    dateRetraiding = models.DateTimeField(default=datetime.today)
    serviceCompanyR = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='serviceCompanyR', default=1)

    @property
    def duration(self):
        day = (self.dateRetraiding - self.dateFailure).days
        print(day)
        return day

