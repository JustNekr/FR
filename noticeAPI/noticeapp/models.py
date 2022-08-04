import pytz
from django.db import models


# Create your models here.
class PhoneCode(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return f'{self.id}'


class Tag(models.Model):

    def __str__(self):
        return f'{self.id}'

    id = models.CharField(primary_key=True, max_length=120)


class Sending(models.Model):

    STATUSES = [
        ('A', 'active'),
        ('P', 'in progress'),
        ('D', 'done'),
    ]
    #id = models.BigIntegerField(primary_key=True)
    sending_start = models.DateTimeField()
    text = models.TextField()
    client_code = models.ManyToManyField(PhoneCode)
    client_tag = models.ManyToManyField(Tag)
    sending_end = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUSES, default='A')


class Client(models.Model):

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    STATUSES = [
        ('A', 'active'),
        ('P', 'in progress'),
        ('D', 'done'),
    ]

    phone_number = models.IntegerField()
    mobile_code = models.ForeignKey(PhoneCode, on_delete=models.CASCADE, unique=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, unique=False)
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC')


class Message(models.Model):

    STATUSES = [
        ('CR', 'created'),
        ('SG', 'send'),
        ('ER', 'error'),
    ]

    sending_date = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUSES, default='CR')
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, unique=False)
    sending_id = models.ForeignKey(Sending, on_delete=models.CASCADE, unique=False)



