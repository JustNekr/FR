import json
import random
import string
import zoneinfo

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from noticeapp.models import Client, Tag, PhoneCode, Timezone


class Command(BaseCommand):
    User.objects.all().delete()
    User.objects.create_superuser('nekr', password='123')

    def handle(self, *args, **options):
        for i in range(5):
            tag = Tag(f'tag_{i}')
            tag.save()

        for i in range(5):
            code = PhoneCode(i * 300)
            code.save()

        for tz in tuple(zoneinfo.available_timezones()):
            zone = Timezone(tz)
            zone.save()

        tags = Tag.objects.all()
        codes = PhoneCode.objects.all()
        tz = Timezone.objects.all()
        for j in range(50):
            client = Client(
                phone_number=70000000000,
                mobile_code=codes[j//10],
                tag=tags[j//10],
                tz=tz[j//10]
            )
            client.save()

        for k in range(20):
            'Europe/Budapest'
            client = Client(
                phone_number=70000000000,
                mobile_code=codes[j // 10],
                tag=tags[j // 10],
                tz=Timezone.objects.get(id='Europe/Budapest')
            )
            client.save()
