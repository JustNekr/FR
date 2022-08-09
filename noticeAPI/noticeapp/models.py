import zoneinfo

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

    id = models.CharField(primary_key=True, max_length=100)


class Timezone(models.Model):
    def __str__(self):
        return f'{self.id}'

    id = models.CharField(primary_key=True, max_length=100)



class Sending(models.Model):

    STATUSES = [
        ('A', 'active'),
        ('P', 'in progress'),
        ('D', 'done'),
    ]
    #id = models.BigIntegerField(primary_key=True)
    sending_start = models.DateTimeField()
    text = models.TextField()
    client_code = models.ManyToManyField(PhoneCode, related_query_name='sending')
    client_tag = models.ManyToManyField(Tag, related_query_name='sending')
    sending_end = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUSES, default='A')


class Client(models.Model):

    #TIMEZONES = tuple(zip(zoneinfo.available_timezones(), zoneinfo.available_timezones()))
    STATUSES = [
        ('A', 'active'),
        ('P', 'in progress'),
        ('D', 'done'),
    ]

    phone_number = models.IntegerField()
    mobile_code = models.ForeignKey(PhoneCode, on_delete=models.CASCADE, unique=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, unique=False)
    tz = models.ForeignKey(Timezone, on_delete=models.CASCADE, unique=False)


class Message(models.Model):

    STATUSES = [
        ('CR', 'created'),
        ('SG', 'send'),
        ('ER', 'error'),
    ]

    sending_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUSES, blank=True, default=None, null=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, unique=False)
    sending_id = models.ForeignKey(Sending, on_delete=models.CASCADE, unique=False)


