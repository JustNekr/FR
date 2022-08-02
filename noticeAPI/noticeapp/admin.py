from django.contrib import admin
from .models import Sending, Message, Client


admin.site.register(Sending)
admin.site.register(Message)
admin.site.register(Client)