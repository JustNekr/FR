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
    """
    Сущность "рассылка" имеет атрибуты:
    •уникальный id рассылки
    •дата и время запуска рассылки
    •текст сообщения для доставки клиенту
    •фильтр свойств клиентов, на которых должна быть произведена рассылка (код мобильного оператора, тег)
    •дата и время окончания рассылки: если по каким-то причинам не успели разослать все сообщения - никакие сообщения клиентам после этого времени доставляться не должны
    """
    #id = models.BigIntegerField(primary_key=True)
    sending_start = models.DateTimeField()
    text = models.TextField()
    client_code = models.ManyToManyField(PhoneCode)
    client_tag = models.ManyToManyField(Tag)
    sending_end = models.DateTimeField()
    # status = models.CharField()


class Client(models.Model):
    """
    Сущность "клиент" имеет атрибуты:
    •уникальный id клиента
    •номер телефона клиента в формате 7 XXX XXX XX XX (X - цифра от 0 до 9)
    •код мобильного оператора
    •тег (произвольная метка)
    •часовой пояс
    """
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    #id = models.BigIntegerField(primary_key=True)
    phone_number = models.IntegerField()
    mobile_code = models.ForeignKey(PhoneCode, on_delete=models.CASCADE, unique=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, unique=False)
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC')


class Message(models.Model):
    """
    Сущность "сообщение" имеет атрибуты:
    •уникальный id сообщения
    •дата и время создания (отправки)
    •статус отправки
    •id рассылки, в рамках которой было отправлено сообщение
    •id клиента, которому отправили
    """

    STATUSES = [
        ('PR', 'в процессе'),
        ('SG', 'отправлено'),
        ('ER', 'ошибка'),
    ]
    #id = models.BigIntegerField(primary_key=True)
    sending_date = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUSES)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, unique=False)
    sending_id = models.ForeignKey(Sending, on_delete=models.CASCADE, unique=False)



