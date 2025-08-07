from django.db import models
# from django.contrib.auth.models import User


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
    shipDate = models.DateTimeField(auto_now_add=True)
    recipient = models.CharField(max_length=100)
    deliveryAddress = models.CharField(max_length=150)
    package = models.TextField(blank=True)
    client = models.CharField(max_length=150)
    serviceCompany = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='serviceCompany')

    def __str__(self):
        return f'{self.modelMachine}. Зав.№{self.zavNumberMachine}'

# class TO(models.Model):
#     id = models.ForeignKey(Machine, to_fieild='zavNumberMachine')
#     typeTO = models.ForeignKey(Manual, on_delete=models.CASCADE, related_name='typeTO')


# Create your models here.
