from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from .models import Sending, Message, Client, Tag, PhoneCode
from .serializers import SendingModelSerializer, MessageModelSerializer, ClientModelSerializer


class SendingModelViewSet(ModelViewSet):
    queryset = Sending.objects.all()
    serializer_class = SendingModelSerializer


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer


class ClientModelViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
