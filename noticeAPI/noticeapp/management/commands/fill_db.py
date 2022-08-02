import json
import random
import string

from django.core.management.base import BaseCommand
from noticeapp.models import Client, Tag, PhoneCode


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(5):
            tag = Tag(f'tag_{i}')
            tag.save()

        for i in range(5):
            code = PhoneCode(i * 300)
            code.save()

        tags = Tag.objects.all()
        codes = PhoneCode.objects.all()
        for j in range(50):
            client = Client(
                phone_number=70000000000,
                mobile_code=codes[j//10],
                tag=tags[j//10]
            )
            client.save()