from django.contrib import admin
from .models import Sending, Message, Client, PhoneCode, Tag


admin.site.register(Sending)
admin.site.register(Message)
admin.site.register(Client)
admin.site.register(Tag)
admin.site.register(PhoneCode)
